import { HTTP } from "../APIBase";
import { handleResponse } from "./BaseService";

export function getPost(postId) {
  return HTTP.get("postdetails/" + postId + "/")
    .then(handleResponse)
    .then(response => {
      return response[1];
    })
    .catch(e => {
      Promise.reject(e);
    });
}
