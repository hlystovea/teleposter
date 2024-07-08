import {
  QueryClient,
  QueryClientProvider
} from 'react-query';

import Footer from './Footer'
import Header from './Header'
import Main from './Main'
import { useEffect, useState } from 'react';
import { telegramAuth } from './auth/apiClient';

const queryClient = new QueryClient();

function App() {
  const [loggedIn, setLoggedIn] = useState(null)
  const [profile, setProfile] = useState(null);

  const login = async (authData) => {
    setProfile(authData);
    localStorage.setItem('profile', JSON.stringify(authData))
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
        console.log(`Error: ${error.message}`);
        setLoggedIn(false);
      });
  };

  const logout = () => {
    localStorage.removeItem('token');
    localStorage.removeItem('profile');
    setLoggedIn(false);
    setProfile(null);
  }

  useEffect(_ => {
    const profile = localStorage.getItem('profile')
    if (profile) {
      login(JSON.parse(profile));
    }
  }, [])

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
