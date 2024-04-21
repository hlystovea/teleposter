class PostData {
    static baseUrl = 'api/v1/posts/';

    static async list () {
        return this._request(PostData.baseUrl);
    }

    static async retrieve (id) {  
        return this._request(PostData.baseUrl + id);
    }

    static async update (id, data) {  
        return this._request(PostData.baseUrl + id, 'PATCH', data);
    }

    static async publish (id) {
        return this._request(PostData.baseUrl + id + '/publish', 'POST');
    }

    static async delete (id) {
        return this._request(PostData.baseUrl + id, 'DELETE');
    }

    static async _request (url, method = 'GET', data = undefined) {
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
            return response.json();
        })
        .catch(error => {
            console.log('Error: ', error);
            return null;
        });
    }
}