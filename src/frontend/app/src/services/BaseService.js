import { logout } from "./AuthService";

export function handleResponse(response) {
  const data = response.data;
  if (data[0] != 200 || response.status != 200) {
    if (data[0] == 401 || response.status == 401) {
      logout();
    }
    const error = data.Error || response.statusText;

    return Promise.reject(error);
  }

  return Promise.resolve(data);
}
