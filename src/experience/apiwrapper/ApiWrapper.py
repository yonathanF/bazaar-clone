"""
API Wrapper for the model layer so the experience layer can
communicate with it.
"""

import json
from kafka import KafkaProducer
from elasticsearch import Elasticsearch

import requests

BASE_URL = "http://models-api:8000/api/v1"
ES_URL = 'elasticsearch'


class API(object):
    """
    Wraps the URL and provides basic methods to communicate to it
    """

    def __init__(self, base_url=BASE_URL, es_url=ES_URL):
        self.base_url = base_url
        self.STATUS_FAIL = 400
        self.es_url = ES_URL
        self.es = Elasticsearch([self.es_url])
    
    def get_es(self, body, doc_type, index, size=10):
        return self.es.search(index=index, doc_type=doc_type, body=body, size=size)

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

    # def comment_top_n(self, category, num_comments):
    #     url = self.comment_endpoint + "byCategory/" + str(category)\
    #                 + "/" + str(num_posts)+"/"

    #     _, response = self.server.get(url)

    #     return response

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
            result = self.server.get_es(query, "post", "bazaar", 10)
            posts = []
            for source in result['hits']['hits']:
                post = source['_source']
                post['post_id'] = source['_id']
                posts.append(post)
            print("*************************************************")
            print(len(posts))
            return posts
        except Exception as e:
            return []
        

    def post_get(self, post_id):
        """
        Gets the post specified by post_id
        """
        url = self.post_endpoint + str(post_id)
        response = self.server.get(url)
        return response

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
        producer = KafkaProducer(bootstrap_servers='kafka:9092')
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
        if(status_code == 200):
            prodres = producer.send('new-posts', json.dumps(response).encode('utf-8'))
            print(prodres.get())
        else:
            print("We are not producing anything")
        return response


    def post_top_n(self, category, num_posts):
        url = self.post_endpoint + "byCategory/" + str(category)\
                    + "/" + str(num_posts)+"/"

        _, response = self.server.get(url)

        return response

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

        # TODO: Finish up routing to model, create model view calls, link frontend buttons for logging in and out
        url = self.login_endpoint + "login/"
        return self.server.post(url, data)

    def login_logout(self, token):
        url = self.login_endpoint + "logout/" + str(token)
        _, response = self.server.get(url)
        return response
