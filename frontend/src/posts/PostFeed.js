import { useQuery } from 'react-query';
import { postList } from './apiClient';
import Post from './Post';
import PostForm from './PostForm';

function PostsFeed() {
  const { isLoading, error, data } = useQuery('posts', postList);

  if (isLoading) return <p>Загрузка...</p>;
    
  if (error) return <p>Ошибка: {error.message}</p>;

  const emptyMessage = <p>Нет доступных публикаций</p>;
  const postCards = data.map((post) => (
    <Post
      key={post.id}
      post={post}
    />
  ));

  return (
    <div className="posts">
      <PostForm />
      {postCards.length !== 0 ? postCards : emptyMessage}
    </div>
  );
}

export default PostsFeed;
