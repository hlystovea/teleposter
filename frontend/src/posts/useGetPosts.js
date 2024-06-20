import { useQuery } from 'react-query';
import { getPosts } from './apiClient';

export const useGetPosts = () => {
  return useQuery('posts', getPosts);
}
