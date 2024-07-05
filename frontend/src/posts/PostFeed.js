import { useCreatePost } from './useCreatePost';
import Post from './Post';
import Form from './Form';
import Card from '../common/Card';
import { useGetPosts } from './useGetPosts';
import Gallery from '../common/Gallery';
import { useState } from 'react';
import postStatus from '../common/status';

function PostsFeed() {
  const { NEW, MODERATED, PUBLISHED } = postStatus;
  const [status, setStatus] = useState(NEW)
  const [textValue, setTextValue] = useState('');
  const [newFiles, setNewFiles] = useState([]);

  const createPost = useCreatePost();
  const getPosts = useGetPosts({status: status});

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
    setTextValue('');
  };
  const onClick = (status) => {
    setStatus(status)
  }

  const formId = 'newPostForm';
  const formButtons = (
    <div className='button-panel flex-end'>
      <button className='btn' name='saveButton' form={formId} type='submit'>
          Сохранить
      </button>
    </div>
  )
  const statusButtons = (
    <div className='button-panel flex-end'>
      <button
        className={`btn ${status === NEW ? 'btn-active' : ''}`}
        onClick={() => onClick(NEW)}
        type='button'
      >Новые</button>
      <button
        className={`btn ${status === MODERATED ? 'btn-active' : ''}`}
        onClick={() => onClick(MODERATED)}
        type='button'
      >Модерированные</button>
      <button
        className={`btn ${status === PUBLISHED ? 'btn-active' : ''}`}
        onClick={() => onClick(PUBLISHED)}
        type='button'
      >Опубликованные</button>
    </div>
  )
  return (
    <div className='posts'>
      {statusButtons}
      <Card>
        <Gallery newFiles={newFiles} setNewFiles={setNewFiles} />
        <Form
          id={formId}
          buttons={formButtons}
          onSubmit={onSubmit}
          textValue={textValue}
          setTextValue={setTextValue}
        />
      </Card>
      {postCards.length !== 0 ? postCards : emptyMessage}
    </div>
  );
}

export default PostsFeed;
