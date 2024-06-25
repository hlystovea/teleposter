import request from '../common/apiClient';

const baseUrl = process.env.REACT_APP_API_URL + 'posts/';

const getPosts = async () => {
    return request(baseUrl);
}

const retrievePost = async (id) => {  
    return request(baseUrl + id);
}

const createPost = async (data) => {
    return request(baseUrl, 'POST', data);
}

const updatePost = async (id, data) => {
    return request(baseUrl + id, 'PATCH', data);
}

const publishPost = async (id) => {
    return request(baseUrl + id + '/publish', 'POST');
}

const deletePost = async (id) => {
    return request(baseUrl + id, 'DELETE');
}

export { getPosts, retrievePost, createPost, updatePost, publishPost, deletePost };
