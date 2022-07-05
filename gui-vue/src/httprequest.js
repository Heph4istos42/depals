import axios from 'axios'

export async function getAllLebensmittel() {
    const response = await axios.get('http://127.0.0.1:5000/getalllebensmittel');
    return response.data;
}

export async function createUser(data) {
    const response = await axios.post(`http://127.0.0.1:5000/getalllebensmittel`, {user: data});
    return response.data;
}