import {
  QueryClient,
  QueryClientProvider,
} from 'react-query';

import Footer from './Footer'
import Header from './Header'
import Main from './Main'

const queryClient = new QueryClient();

function App() {
  return (
    <>
      <Header />
      <QueryClientProvider client={queryClient}>
        <Main />
      </QueryClientProvider>
      <Footer />
    </>
  );
}

export default App;
