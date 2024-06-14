import { useMutation, useQueryClient } from 'react-query';
import { deletePost } from './apiClient';

export const useDeletePost = () => {
  const queryClient = useQueryClient();

  return useMutation((postId) => deletePost(postId), {
    onSuccess: () => {
      queryClient.invalidateQueries('posts');
    },
  });
};
