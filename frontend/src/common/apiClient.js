const request = async(url, method = 'GET', data = undefined) => {
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

export default request;
