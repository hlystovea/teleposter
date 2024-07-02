const baseUrl = process.env.REACT_APP_API_URL + 'files/';

const uploadFiles = async (data) => {
    return fetch(baseUrl + 'upload/', {
        method: 'POST',
        body: data
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(response.text());
        }
        return response.json();
    })
    .catch(error => {
        console.log('Error: ', error);
        return null;
    });
}

export default uploadFiles;
