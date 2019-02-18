import axios from 'axios';

export const HTTP = axios.create({
  baseURL: `http://localhost:8001/api/v1/`,
  headers: {
	"content-type": "application/x-www-form-urlencoded",
	"accept": "application/json"
	},
})

