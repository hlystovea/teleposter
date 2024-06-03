import PostsFeed from "./posts/PostFeed"
import PostForm from "./posts/PostForm"

function Main() {
  return (
    <main>
      <section>
        <h2>Новости</h2>
        <PostForm />
        <PostsFeed />
      </section>
    </main>
  );
}

export default Main;
