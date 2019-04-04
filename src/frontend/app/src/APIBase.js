import axios from "axios";

const token = localStorage.getItem("token");
const authHeader = { Authorization: `Bearer ${token}` };

export const HTTP = axios.create({
  baseURL: `http://localhost:8002/api/v1/`,
  headers: authHeader
});
