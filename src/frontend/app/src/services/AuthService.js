import { HTTP } from "../APIBase";
import { handleResponse } from "./BaseService";

export function logout() {
  HTTP.get("auth/logout/", {
    params: {
      token: localStorage.getItem("token")
    }
  }).then(localStorage.removeItem("token"));
}

export function login(email, password) {
  return HTTP.post("auth/login/", {
    email: email,
    password: password
  })
    .then(handleResponse)
    .then(token => {
      if (token["token"]) {
        localStorage.setItem("token", token["token"]);
      } else if (token["Status"]) {
        return Promise.reject(token["Status"]);
      }
    })
    .catch(e => {
      return Promise.reject(e);
    });
}

export function register(firstname, lastname, email, password){
  return HTTP.post("auth/create/", {
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
      return response.data;
  })
  .catch(e => {
    console.log(e);
    Promise.reject(e);
  });
}

export function isAuthenticated() {
  const token = localStorage.getItem("token");
  return !(!token || token.length === 0);
}
