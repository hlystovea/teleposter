import { useQuery } from 'react-query';
import request from './apiClient';

function Logo() {
  const baseUrl = process.env.REACT_APP_API_URL;
  const getChatInfo = async () => {
      return request(baseUrl + 'chat/info');
  }
  const { isLoading, error, data } = useQuery('chatInfo', getChatInfo, {
      staleTime: Infinity,
  });

  if (isLoading) return <></>;

  if (error) {
    console.log(`Ошибка: ${error.message}`);
    return <></>;
  }
  
  return (
    <div className='logo'>
      <img src={baseUrl + 'files/' + data.photo.small_file_id} alt='logo' />
      <p>{data.title}</p>
    </div>
  );
}

export default Logo;
