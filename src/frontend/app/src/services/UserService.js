import { HTTP } from "../APIBase";
import { handleResponse } from "./BaseService";

export function createUser(firstname, lastname, email, password){
    return HTTP.post("users/create/", {
        first_name: firstname,
        last_name: lastname,
        email: email,
        password: password,
        rating: 0.00,
        description: "",
        education: "",
        zip_code: '00000',
    })
    .then(handleResponse)
    .then(response => {
        console.log(response.status_code)
    })
    .catch(e => {
      Promise.reject(e);
    });
  }