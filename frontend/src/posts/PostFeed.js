import { useQuery } from 'react-query';
import Post from './Post';

function PostsFeed() {
  const { isLoading, error, data } = useQuery(
    'posts',
    () =>
      fetch(
        'http://127.0.0.1/api/v1/posts/'
      ).then((response) => response.json())
  );

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
      {postCards.length !== 0 ? postCards : emptyMessage}
    </div>
  );
}

export default PostsFeed;
