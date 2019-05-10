"""
API Wrapper for the model layer so the experience layer can
communicate with it.
"""
import ast
import json

import requests

import redis
from elasticsearch import Elasticsearch
from kafka import KafkaProducer

BASE_URL = "http://models-api:8000/api/v1"
ES_URL = 'elasticsearch'


class API(object):
    """
    Wraps the URL and provides basic methods to communicate to it
    """

    def __init__(self, base_url=BASE_URL, es_url=ES_URL):
        self.base_url = base_url
        self.STATUS_FAIL = 400
        self.kafka = KafkaProducer(bootstrap_servers='kafka:9092')
        self.es_url = ES_URL
        self.es = Elasticsearch([self.es_url])
        self.red = redis.Redis(host='redis', port=6379, db=0)

    def get_es(self, body, doc_type, index, size=10):
        return self.es.search(index=index,
                              doc_type=doc_type,
                              body=body,
                              size=size)

    def post_kafka(self, topic, data):
        kafka_response = self.kafka.send(topic, json.dumps(data).encode('utf-8'))
        '''
        f = open("tmp.txt", "a")
        f.write(str(kafka_response))
        f.close()
        '''
        return kafka_response.get()

    def post(self, endpoint, data):
        url = self.base_url + endpoint
        try:
            response = requests.post(url, data=data)
            return response.status_code, response.json()
        except Exception as e:
            return self.STATUS_FAIL, json.dumps(
                {'Status': 'Failed to process request.[ %s ]' % (str(e))})

    def get(self, endpoint):
        url = self.base_url + endpoint
        try:
            response = requests.get(url)
            return response.status_code, response.json()

        except Exception as e:
            return self.STATUS_FAIL, json.dumps(
                {'Status': 'Failed to process request.[ %s ]' % (str(e))})


class APIV1(object):
    """
    A more concrete implementation that is aware of the v1
    endpoints. Avoids coupling with the exact urls such as /posts
    """

    def __init__(self, server=None):
        if server is None:
            self.server = API()
        else:
            self.server = server

        self.post_endpoint = '/post/'
        self.comment_endpoint = '/comment/'
        self.login_endpoint = '/profile/'

    def profile_get_with_token(self, token):
        """
        Gets the profile related to the token
        """
        url = self.login_endpoint + "/authProfile/" + token + "/"
        response = self.server.get(url)
        return response

    def comment_get(self, comment_id):
        """
        Gets the post specified by post_id
        """
        url = self.comment_endpoint + str(comment_id)
        response = self.server.get(url)
        return response

    def comment_delete(self, comment_id):
        """
        Deletes the post specified by the post_id
        """
        url = self.comment_endpoint + "delete/" + str(comment_id)
        _, response = self.server.get(url)

        return response

    def comment_update(self, comment_id, post_id, user_id, title, details,
                       stars, date_posted):

        data = {
            'title': title,
            'details': details,
            'stars': stars,
            'date_posted': date_posted,
            'post': post_id,
            'user': user_id
        }

        url = self.comment_endpoint + str(comment_id) + "/"
        _, response = self.server.post(url, data)
        return response

    def comment_create(
            self,
            comment_id,
            title,
            details,
            stars,
            date_posted,
            post_id,
            user_id,
    ):

        data = {
            'title': title,
            'details': details,
            'stars': stars,
            'date_posted': date_posted,
            'post': post_id,
            'user': user_id
        }

        url = self.comment_endpoint + "create/" + str(post_id) + "/" + str(
            user_id)
        _, response = self.server.post(url, data)
        return response

    def post_search(self, keywords):
        query = {
            "query": {
                "multi_match": {
                    "query": keywords,
                    "fields": ['title', 'details']
                }
            }
        }
        try:
            result = self.server.get_es(query, "post", "models", 10)
            posts = []
            for source in result['hits']['hits']:
                post = source['_source']
                post['post_id'] = source['_id']
                posts.append(post)
            return posts
        except Exception as e:
            return []

    def post_get_and_log(self, post_id, user_id):
        """
        Gets the post and also logs it for rec system
        """
        log_data = str(user_id) + " " + str(post_id) + "\n"
        k_response = self.server.post_kafka("post-log", log_data)
        log_file = open("tmp.txt", "w")
        log_file.write(str(k_response))
        return self.post_get(post_id)

    def post_get(self, post_id):
        """
        Gets the post specified by post_id
        """
        url = self.post_endpoint + str(post_id)
        response = self.server.get(url)

        string_id = str(post_id)

        if (self.server.red.get(string_id) is None):
            self.server.red.set(string_id, str(response[1]))
            self.server.red.expire(string_id, 300)
            return response
        else:
            response = ast.literal_eval(
                self.server.red.get(string_id).decode('utf-8'))
            return (200, response)

    def post_delete(self, post_id):
        """
        Deletes the post specified by the post_id
        """
        url = self.post_endpoint + "delete/" + str(post_id)
        _, response = self.server.get(url)

        return response

    def post_update(self, post_id, title, details, category, preferred_contact,
                    deadline, zip_code, request_type, user_id):
        data = {
            'title': title,
            'details': details,
            'category': category,
            'preferred_contact': preferred_contact,
            'deadline': deadline,
            'zip_code': zip_code,
            'request_type': request_type,
            'user': user_id
        }

        url = self.post_endpoint + str(post_id) + "/"
        _, response = self.server.post(url, data)
        return response

    def post_create(self, title, details, category, preferred_contact,
                    deadline, request_type, zip_code, token):
        data = {
            'title': title,
            'details': details,
            'category': category,
            'preferred_contact': preferred_contact,
            'deadline': deadline,
            'zip_code': zip_code,
            'request_type': request_type,
            'user': 1
        }
        url = self.post_endpoint + "create/" + str(token)
        status_code, response = self.server.post(url, data)
        if (status_code == 200):
            self.server.post_kafka('new-posts', response)

        return response

    def post_top_n(self, category, num_posts):
        url = self.post_endpoint + "byCategory/" + str(category)\
                    + "/" + str(num_posts)+"/"

        _, response = self.server.get(url)

        combined_id = str(category) + "+" + str(num_posts)

        if (self.server.red.get(combined_id) is None):
            self.server.red.set(combined_id, str(response))
            self.server.red.expire(combined_id, 300)
            return response
        else:
            response = ast.literal_eval(
                self.server.red.get(combined_id).decode('utf-8'))
            return response
        '''
        f = open("tmp.txt", "a")
        f.write(str(response))
        f.close()
        '''

    def login_get(self, user_id):
        pass

    def login_create(self, first_name, last_name, email, password):

        data = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'password': password,
            'rating': 0.00,
            'description': "Please update description",
            'education': "Please update education",
            'zip_code': 00000,
        }

        url = self.login_endpoint + "create/"
        response_code, response = self.server.post(url, data)
        return response_code, response

    def login_update(self, first_name, last_name, email, password, rating,
                     description, education, zip_code):
        pass

    def login_delete(user_id):
        pass

    def login_login(self, email, password):
        data = {'email': email, 'password': password}

        url = self.login_endpoint + "login/"
        return self.server.post(url, data)

    def login_logout(self, token):
        url = self.login_endpoint + "logout/" + str(token)
        _, response = self.server.get(url)
        return response
