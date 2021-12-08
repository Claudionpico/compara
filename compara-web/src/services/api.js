import axios from "axios";

const requestHelper = axios.create({
      baseURL: 'http://0.0.0.0:8000/0.1',
      responseType: "json",
});

function header() {
    return {
        "Content-type":"application/json; charset=UTF-8"
    }
}

export default {
    car: {
        getOne: word => requestHelper({
            headers: header(),
            url: 'cars',
            method: 'get',
            params: {
                'q':'{"filters":[{"name": "plate", "op": "==", "val":"'+word+'"}]}'
            }
        })
    }
}
