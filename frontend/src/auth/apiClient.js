import request from '../common/apiClient';

const baseUrl = process.env.REACT_APP_API_URL + 'auth/';

const telegramAuth = async (data) => {
    return request(baseUrl + 'telegram-auth', 'GET', data);
}

export { telegramAuth };
