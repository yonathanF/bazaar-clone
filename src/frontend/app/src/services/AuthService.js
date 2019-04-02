import { HTTP } from "../APIBase";
import { handleResponse } from "./BaseService";

export function logout() {
  HTTP.get("logout/", {
    params: {
      token: localStorage.getItem("token")
    }
  }).then(localStorage.removeItem("token"));
}

export function login(email, password) {
  return HTTP.post("login/login/", {
    email: email,
    password: password
  })
    .then(handleResponse)
    .then(token => {
      if (token) {
        localStorage.setItem("token", token["token"]);
      }
    })

    .catch(e => {
      Promise.reject(e);
    });
}

export function register(firstname, lastname, email, password) {
  HTTP.post("register/", {
    firstname: firstname,
    lastname: lastname,
    email: email,
    password: password
  })
    .then(handleResponse)
    .then(token => {
      if (token) {
        localStorage.setItem("token", JSON.stringify(token));
      }
    });
}
export function isAuthenticated() {
  const token = localStorage.getItem("token");
  return !(!token || token.length === 0);
}
