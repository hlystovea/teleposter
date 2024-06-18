import React, { useState } from 'react';
import { useDeletePost } from './useDeletePost';
import { usePublishPost } from './usePublishPost';
import { useUpdatePost } from './useUpdatePost';
import Card from '../common/Card';
import Gallery from '../common/Gallery';

const mediaUrl = process.env.REACT_APP_MEDIA_URL;


function Post({post}) {
  const [isEditing, setIsEditing] = useState(false);
  const photos = post.files.map((file, index) => {
    const key = file + index;
    const url = `${mediaUrl}${file}`;
    const alt = file;
    return {
      key: key,
      url: url,
      alt: alt,
    };
  })
  return (
    <Card>
      <Gallery photos={photos} />
      {isEditing ? (
        <EditForm post={post} setIsEditing={setIsEditing} />
      ) : (
        <PostCard post={post} setIsEditing={setIsEditing} />
      )}
    </Card>
  );
}

const EditForm = ({post, setIsEditing}) => {
  const [textValue, setTextValue] = useState(post.text) 
  const updatePost = useUpdatePost();
  const onCancelClick = () => {
    setIsEditing(false);
  }
  const onSubmit = (event) => {
    event.preventDefault();
    const formData = new FormData(event.target);
    const data = Object.fromEntries(formData.entries());
    updatePost.mutate({postId: post.id, data: data});
    setIsEditing(false);
  };
  const onTextChange = (event) => {
    setTextValue(event.target.value);
  };
  return (
    <form action="" method="POST" onSubmit={onSubmit}>
      <textarea className="text-input" name="text" value={textValue} onChange={onTextChange} autoFocus />
      <button className="btn-save" name="saveButton" type="submit">
          Сохранить
      </button>
      <button className="btn-cancel" name="cancelButton" type="button" onClick={onCancelClick}>
          Отмена
      </button>
    </form>
  )
}
const PostCard = ({post, setIsEditing}) => {
  const { id, text, status, photo, caption, files } = post;
  const deletePost = useDeletePost();
  const publishPost = usePublishPost();
  const onPublishClick = () => {
    publishPost.mutate(post.id);
  };
  const onEditClick = () => {
    setIsEditing(true);
  }
  const onDeleteClick = () => {
    deletePost.mutate(post.id);
  };
  return (
    <>
      <p className="post-text">{text || caption}</p>
      <span className="post-status">{status}</span>
      <button className="btn-publish" name="publishButton" type="button" onClick={onPublishClick}>
        Опубликовать
      </button>
      <button className="btn-edit" name="editButton" type="button" onClick={onEditClick}>
        Редактировать
      </button>
      <button className="btn-delete" name="deleteButton" type="button" onClick={onDeleteClick}>
        Удалить
      </button>
    </>
  )
}

export default Post;
