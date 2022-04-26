
import Cookies from "js-cookie";




const csrftoken = Cookies.get("csrftoken");



export const BASEURL = "";
// export const BASEURL = "http://0.0.0.0:8000";
export const postheader = {
    "X-CSRFToken": csrftoken,
  };