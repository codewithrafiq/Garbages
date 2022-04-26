import axios from "axios";

const instance = axios.create({
  baseURL: "http://localhost:2800",
  // baseURL: "http://192.168.1.7:2800",
  
});

export default instance;
