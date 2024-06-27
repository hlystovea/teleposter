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
      <QueryClientProvider client={queryClient}>
        <Header />
        <Main />
        <Footer />
      </QueryClientProvider>
    </>
  );
}

export default App;
