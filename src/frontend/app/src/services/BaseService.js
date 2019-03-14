import { logout } from "./AuthService";

export function handleResponse(response) {
  const data = response.data;
  if (response.status != 200) {
    if (response.status == 401) {
      logout();
    }
    const error = data.Error || response.statusText;

    return Promise.reject(error);
  }

  return Promise.resolve(data);
}
