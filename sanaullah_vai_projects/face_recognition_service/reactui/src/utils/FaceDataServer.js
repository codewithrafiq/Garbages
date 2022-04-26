import axios from "axios";

const instance = axios.create({
   baseURL: "http://localhost:5000",
// baseURL: "http://18.140.255.142",
});

export default instance;
