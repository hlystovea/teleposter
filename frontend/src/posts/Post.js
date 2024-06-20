import React, { useState } from 'react';
import { useDeletePost } from './useDeletePost';
import { usePublishPost } from './usePublishPost';
import { useUpdatePost } from './useUpdatePost';
import Card from '../common/Card';
import Gallery from '../common/Gallery';
import Form from './Form';
import uploadFile from '../files/apiClient';
import FileForm from '../files/fileForm';

const mediaUrl = process.env.REACT_APP_MEDIA_URL;


function Post({post}) {
  const [isEditing, setIsEditing] = useState(false);
  const [files, setFiles] = useState(post.files);
  const [newFiles, setNewFiles] = useState([]);

  const photos = [...files, ...newFiles].map((file, index) => {
    return {
      key: file + index,
      name: file,
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
  const onFileFormSubmit = async (event) => {
    event.preventDefault();
    const form = event.target.closest('form');
    const data = new FormData(form);
    const uploadedFile = await uploadFile(data);
    if (!uploadedFile) {
      console.log('File upload error');
      return ;
    }
    setNewFiles([...newFiles, uploadedFile.file_name]);
  };
  const deleteFile = (file) => {
    setFiles(files.filter(item => item !== file));
    setNewFiles(newFiles.filter(item => item !== file))
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
      <Gallery photos={photos} deletePhoto={deleteFile} isEditing={isEditing} />
      {isEditing ? (
        <>
          <FileForm action={onFileFormSubmit} />
          <Form id={post.id} buttons={formButtons} onSubmit={onSubmit} initialText={post.text || post.caption || ''} />
        </>
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
