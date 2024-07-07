import {
  QueryClient,
  QueryClientProvider
} from 'react-query';

import Footer from './Footer'
import Header from './Header'
import Main from './Main'
import { useState } from 'react';
import { telegramAuth } from './auth/apiClient';

const queryClient = new QueryClient();

function App() {
  const [loggedIn, setLoggedIn] = useState(null)
  const [profile, setProfile] = useState(null);

  const login = async (authData) => {
    const {photo_url, username} = authData;
    setProfile({photo_url, username});
    telegramAuth(authData)
      .then(response => {
        if (response.token) {
          localStorage.setItem('token', response.token);
          setLoggedIn(true);
        } else {
          setLoggedIn(false);
        }
      })
      .catch(error => {
        console.log(`Ошибка: ${error.message}`);
        setLoggedIn(false);
      });
  };

  const logout = () => {
    localStorage.removeItem('token');
    setLoggedIn(false);
    setProfile(null);
  }

  return (
    <>
      <QueryClientProvider client={queryClient}>
        <Header profile={profile} logout={logout} />
        <Main loggedIn={loggedIn} login={login} />
        <Footer />
      </QueryClientProvider>
    </>
  );
}

export default App;
