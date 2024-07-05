import { useQuery } from 'react-query';
import { getPosts } from './apiClient';

export const useGetPosts = (params = {}) => {
  return useQuery(['posts', params], () => getPosts(params));
}
