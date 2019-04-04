import { HTTP } from "../APIBase";
import { handleResponse } from "./BaseService";

export function getPost(postId) {
  return HTTP.get("postdetails/" + postId + "/")
    .then(handleResponse)
    .then(response => {
      return response[1];
    })
    .catch(e => {
      return Promise.reject(e);
    });
}

export function searchPost(query) {
  return HTTP.get("postdetails/search/" + query)
    .then(handleResponse)
    .catch(e => {
      return Promise.reject(e);
    });
}

export function createPost(data) {
  return HTTP.post("postdetails/create/" + localStorage.getItem("token") + "/", data)
    .then(handleResponse)

    .catch(e => {
      return Promise.reject(e);
    });
}

export function getHomepagePosts(numOfPosts) {
  return HTTP.get("homepage/" + numOfPosts + "/")
    .then(handleResponse)
    .then(response => {
      return response.data;
    })
    .catch(e => {
      return Promise.reject(e);
    });
}
