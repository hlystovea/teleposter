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
    return {
      key: file + index,
      url: `${mediaUrl}${file}`,
      alt: file,
    };
  })
  const updatePost = useUpdatePost();
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
  const onSubmit = (event) => {
    event.preventDefault();
    const formData = new FormData(event.target);
    const data = Object.fromEntries(formData.entries());
    updatePost.mutate({postId: post.id, data: data});
    setIsEditing(false);
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
      <button className='btn-cancel' name='cancelButton' type='button' onClick={() => setIsEditing(false)}>
        Отмена
      </button>
    </>
  )
  return (
    <Card>
      <Gallery photos={photos} />
      {isEditing ? (
        <Form post={post} buttons={formButtons} onSubmit={onSubmit} />
      ) : (
        <Content post={post} buttons={postButtons} />
      )}
    </Card>
  );
}

const Form = ({post, buttons, onSubmit}) => {
  const [textValue, setTextValue] = useState(post.text || post.caption || '');
  const rows = textValue.split('\n').length;
  const onTextChange = (event) => {
    const input = event.target;
    setTextValue(input.value);
    input.style.height = '1px';
    input.style.height = input.scrollHeight + 'px';
  };
  return (
    <>
      <form id={post.id} onSubmit={onSubmit}>
        <textarea className='text-input' rows={rows} name='text' value={textValue} onChange={onTextChange} autoFocus />
      </form>
      {buttons}
    </>
  );
}
const Content = ({post, buttons}) => {
  return (
    <>
      <p className='post-text'>{post.text || post.caption}</p>
      {buttons}
    </>
  );
}

export default Post;
