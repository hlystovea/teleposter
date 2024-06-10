import { useMutation, useQueryClient } from 'react-query';
import { postPublish, postDelete } from '../api/posts';

const baseUrl = process.env.REACT_APP_API_URL;

function Post({post}) {
  const { id, text, status, photo, caption } = post;

  const queryClient = useQueryClient();

  const publishMutation = useMutation(postPublish, {
    onSuccess: () => {
      queryClient.invalidateQueries('posts');
    },
  });

  const deleteMutation = useMutation(postDelete, {
    onSuccess: () => {
      queryClient.invalidateQueries('posts');
    },
  });

  const onPublish = () => {
    publishMutation.mutate(id);
  };

  const onDelete = () => {
    deleteMutation.mutate(id);
  };

  return (
    <div className="post">
      <div className="post-photo">
        <img src={photo && `${baseUrl}files/${photo.at(-1).file_id}`} alt="Фото" /> 
      </div>
      <p className="post-text">{text || caption}</p>
      <span className="post-status">{status}</span>
      <button className="btn-publish" name="publishButton" type="button" onClick={onPublish}>
        Опубликовать
      </button>
      <button className="btn-edit" name="editButton" type="button">
        Редактировать
      </button>
      <button className="btn-delete" name="deleteButton" type="button" onClick={onDelete}>
        Удалить
      </button>
    </div>
  );
}

export default Post;
