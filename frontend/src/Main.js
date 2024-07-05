import { useState } from 'react';
import PostsFeed from './posts/PostFeed'
import postStatus from './common/status';

function Main() {
  const [status, setStatus] = useState(postStatus['non-moderated'])
  const onClick = (status) => {
    setStatus(status)
  }
  const statusButtons = (
    <div className='flex flex-end'>
      <button
        className={`btn ${status === postStatus['non-moderated'] ? 'btn-active' : ''}`}
        onClick={() => onClick('non-moderated')}
        type='button'
      >Новые</button>
      <button
        className={`btn ${status === postStatus.moderated ? 'btn-active' : ''}`}
        onClick={() => onClick('moderated')}
        type='button'
      >Модерированные</button>
      <button
        className={`btn ${status === postStatus.published ? 'btn-active' : ''}`}
        onClick={() => onClick('published')}
        type='button'
      >Опубликованные</button>
    </div>
  )
  return (
    <main>
      <section>
        <h2>Новости</h2>
          {statusButtons}
        <PostsFeed status={status}/>
      </section>
    </main>
  );
}

export default Main;
