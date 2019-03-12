import { HTTP } from "../APIBase";

function handleResponse(response) {
  return response.text().then(text => {
    const data = text && JSON.parse(text);
    if (!response.ok) {
      // invalid login creds
      if (response.status == 401) {
        logout();
      }

      // TODO handle expired tokens by checking
      // status code and the value of isAuthenticated

      const error = (data && data.Error) || response.statusText;
      return Promise.reject(error);
    }

    return data;
  });
}

function logout() {
  HTTP.get("logout/", {
    params: {
      token: localStorage.getItem("token")
    }
  }).then(localStorage.removeItem("token"));
}

function login(email, password) {
  HTTP.post("login/", {
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

function register(firstname, lastname, email, password) {
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
