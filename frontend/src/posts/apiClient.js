const baseUrl = process.env.REACT_APP_API_URL + 'posts/';

const getPosts = async () => {
    return postRequest(baseUrl);
}

const retrievePost = async (id) => {  
    return postRequest(baseUrl + id);
}

const createPost = async (data) => {
    return postRequest(baseUrl, 'POST', data);
}

const updatePost = async (id, data) => {
    return postRequest(baseUrl + id, 'PATCH', data);
}

const publishPost = async (id) => {
    return postRequest(baseUrl + id + '/publish', 'POST');
}

const deletePost = async (id) => {
    return postRequest(baseUrl + id, 'DELETE');
}

const postRequest = async(url, method = 'GET', data = undefined) => {
    const options = {
        method: method,
        headers: {
            'Content-Type': 'application/json'
        }
    };
    if (data) {
        options.body = JSON.stringify(data);
    }
    return fetch(url, options)
    .then(response => {
        if (!response.ok) {
            throw new Error(response.text());
        }
        return (response.status !== 204 ? response.json() : undefined);
    });
};

export { getPosts, retrievePost, createPost, updatePost, publishPost, deletePost };
