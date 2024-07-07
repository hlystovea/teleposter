import { LoginButton } from '@telegram-auth/react';
import PostsFeed from './posts/PostFeed'

function Main({loggedIn, login}) {
  return (
    <main>
      <section>
        {loggedIn ? (
          <>
            <h2>Новости</h2>
            <PostsFeed />
          </>
        ) : (
          <>
          <h1>
            Пожалуйста, авторизуйтесь &nbsp;
            <LoginButton
              botUsername={process.env.REACT_APP_BOT_USERNAME}
              buttonSize='small'
              cornerRadius={5}
              showAvatar={false}
              lang='ru'
              onAuthCallback={login}
            />
          </h1>
          <p>
            Только избранные пользователи могут просматривать этот сайт. 
          </p>
          </>
        )}
      </section>
    </main>
  );
}

export default Main;
