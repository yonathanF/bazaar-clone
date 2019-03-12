import { logout } from "./AuthService";

export function handleResponse(response) {
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
