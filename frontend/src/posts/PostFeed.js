import { useQuery } from 'react-query';
import { postList } from '../api/posts';
import Post from './Post';

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
      {postCards.length !== 0 ? postCards : emptyMessage}
    </div>
  );
}

export default PostsFeed;
