import axios from 'axios'

//Lebensmittel
export async function getAllLebensmittel() {
    const response = await axios.get('http://127.0.0.1:5000/getalllebensmittel');
    return response.data;
}

export async function getlebensmittelbyinput(input, username) {
    const response = await axios.get('http://127.0.0.1:5000/getlebensmittelbyinput/'+input+'/'+username);
    return response.data;
}


//Nutzer
export async function getuserbyname(username) {
    const response = await axios.get('http://127.0.0.1:5001/getuserbyname/'+ username);
    return response.data;
}

export async function authuser(username, userauth) {
    const response = await axios.get('http://127.0.0.1:5001/authuser/' +username+ '/' +userauth);
    return response.data;
}

export async function updateuser(username, data) {
    const response = await axios.put('http://127.0.0.1:5001/updateuser/' +username, data);
    return response.data;
}

export async function createuser(username, data) {
    const response = await axios.post('http://127.0.0.1:5001/createuser', data);
    return response.data;
}

//Plan
export async function addtoplan(planid, username, barcodeid) {
    const response = await axios.put('http://127.0.0.1:5002/addtoplan/' +planid+ '/' +username+ '/'+barcodeid);
    return response.data;
}

export async function createnewplan(username) {
    const response = await axios.post('http://127.0.0.1:5002/createnewplan/' +username);
    return response.data;
}

export async function getplansbyuser(username) {
    const response = await axios.get('http://127.0.0.1:5002/getplansbyuser/' +username);
    return response.data;
}

export async function getplanbyidsnduser(planid, username) {
    const response = await axios.get('http://127.0.0.1:5002/getplanbyidsnduser/' +planid+ '/' +username);
    return response.data;
}

export async function setstarsandcomments(planid, username, data) {
    const response = await axios.put('http://127.0.0.1:5002/setstarsandcomments/' +planid+ '/' +username, data);
    return response.data;
}

export async function deleteplan(planid) {
    const response = await axios.delete('http://127.0.0.1:5002/deleteplan/' +planid);
    return response.data;
}

export async function removefromplan(planid, barcodeid) {
    const response = await axios.delete('http://127.0.0.1:5002/removefromplan/' +planid+ '/' +barcodeid);
    return response.data;
}
