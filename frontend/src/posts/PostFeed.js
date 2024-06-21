import { useCreatePost } from './useCreatePost';
import Post from './Post';
import Form from './Form';
import Card from '../common/Card';
import { useGetPosts } from './useGetPosts';
import Gallery from '../common/Gallery';
import { useState } from 'react';

function PostsFeed() {
  const [newFiles, setNewFiles] = useState([]);
  const createPost = useCreatePost();
  const getPosts = useGetPosts();
  const { isLoading, error, data } = getPosts;

  if (isLoading) return <p>Загрузка...</p>;
    
  if (error) return <p>Ошибка: {error.message}</p>;

  const emptyMessage = <p>Нет доступных публикаций</p>;
  const postCards = data.map((post) => (
    <Post key={post.id} post={post} />
  ));

  const onSubmit = (event) => {
    event.preventDefault();
    const formData = new FormData(event.target);
    const data = Object.fromEntries(formData.entries());
    data.files = [...newFiles];
    createPost.mutate(data);
    setNewFiles([]);
  };
  const addFile = (file) => {
    setNewFiles([...newFiles, file]);
  };
  const deleteFile = (file) => {
    setNewFiles(newFiles.filter(item => item !== file))
  };
  const formId = 'newPostForm';
  const formButtons = (
    <>
      <button className='btn-save' name='saveButton' form={formId} type='submit'>
          Сохранить
      </button>
    </>
  )
  return (
    <div className='posts'>
      <Card>
        <Gallery photos={[]} deletePhoto={deleteFile} addPhoto={addFile} isEditing={true} />
        <Form id={formId} buttons={formButtons} onSubmit={onSubmit}  />
      </Card>
      {postCards.length !== 0 ? postCards : emptyMessage}
    </div>
  );
}

export default PostsFeed;
