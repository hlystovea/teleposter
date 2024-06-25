import React, { useState } from 'react';
import { useDeletePost } from './useDeletePost';
import { usePublishPost } from './usePublishPost';
import { useUpdatePost } from './useUpdatePost';
import Card from '../common/Card';
import Gallery from '../common/Gallery';
import Form from './Form';
import formatDate from '../common/formatDate';
import Status from './Status';

function Post({post}) {
  const [isEditing, setIsEditing] = useState(false);
  const [textValue, setTextValue] = useState(post.text || post.caption || '');
  const [files, setFiles] = useState(post.files);
  const [newFiles, setNewFiles] = useState([]);
  const status = {
    'non-moderated': 'Не модерирован',
    'moderated': 'Прошел модерацию',
    'published': 'Опубликован',
  }

  const updatePost = useUpdatePost();
  const deletePost = useDeletePost();
  const publishPost = usePublishPost();

  const onPublishClick = () => {
    publishPost.mutate(post.id);
  };
  const onEditClick = () => {
    setIsEditing(true);
  };
  const onDeleteClick = () => {
    deletePost.mutate(post.id);
  };
  const onCancelClick = () => {
    setIsEditing(false);
    setNewFiles([]);
    setFiles(post.files)
  };
  const onSubmit = (event) => {
    event.preventDefault();
    const formData = new FormData(event.target);
    const data = Object.fromEntries(formData.entries());
    data.files = [...files, ...newFiles];
    updatePost.mutate({postId: post.id, data: data});
    setIsEditing(false);
    setFiles([...files, ...newFiles]);
    setNewFiles([]);
  };
  const postButtons = (
    <>
      <button className='btn-publish' name='publishButton' type='button' onClick={onPublishClick}>
        Опубликовать
      </button>
      <button className='btn-edit' name='editButton' type='button' onClick={onEditClick}>
        Редактировать
      </button>
      <button className='btn-delete' name='deleteButton' type='button' onClick={onDeleteClick}>
        Удалить
      </button>
    </>
  )
  const formButtons = (
    <>
      <button form={post.id} className='btn-save' name='saveButton' type='submit'>
        Сохранить
      </button>
      <button className='btn-cancel' name='cancelButton' type='button' onClick={onCancelClick}>
        Отмена
      </button>
    </>
  )
  return (
    <Card>
      <Status date={formatDate(post.created_at)} text={status[post.status]} />
      <Gallery
        files={files}
        newFiles={newFiles}
        setFiles={setFiles}
        setNewFiles={setNewFiles}
        isEditing={isEditing}
      />
      {isEditing ? (
        <Form
          id={post.id}
          buttons={formButtons}
          onSubmit={onSubmit}
          textValue={textValue}
          setTextValue={setTextValue}
        />
      ) : (
        <>
          <p className='post-text'>{post.text || post.caption}</p>
          {postButtons}
        </>
      )}
    </Card>
  );
}

export default Post;
