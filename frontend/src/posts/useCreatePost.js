import { useMutation, useQueryClient } from 'react-query';
import { createPost } from './apiClient';

export const useCreatePost = () => {
  const queryClient = useQueryClient();

  return useMutation((data) => createPost(data), {
    onSuccess: () => {
      queryClient.invalidateQueries('posts');
    },
  });
};
