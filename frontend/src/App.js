import {
  QueryClient,
  QueryClientProvider,
} from 'react-query';

import Footer from './Footer'
import Header from './Header'
import Main from './Main'
import { useState } from 'react';

const queryClient = new QueryClient();

function App() {
  const [loggedIn, setLoggedIn] = useState(null)
  const [profile, setProfile] = useState(null);
  const login = (data) => {
    const {photo_url, username} = data;
    setProfile({photo_url, username});
    setLoggedIn(true);
  };
  const logout = () => {
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
