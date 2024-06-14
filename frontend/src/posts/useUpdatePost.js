import { useMutation, useQueryClient } from 'react-query';
import { updatePost } from './apiClient';

export const useUpdatePost = () => {
  const queryClient = useQueryClient();

  return useMutation(({postId, data}) => updatePost(postId, data), {
    onSuccess: () => {
      queryClient.invalidateQueries('posts');
    },
  });
};
