import { useMutation, useQueryClient } from 'react-query';
import { publishPost } from './apiClient';

export const usePublishPost = () => {
  const queryClient = useQueryClient();

  return useMutation((postId) => publishPost(postId), {
    onSuccess: () => {
      queryClient.invalidateQueries('posts');
    },
  });
};
