// Update the posts
async function updatePosts() {
    await fetch('http://localhost/api/v1/posts')
        .then(response => response.json())
        .then(data => {
            renderPosts(data);
        })
        .catch(error => {
            console.log('Error: ', error);
        });
};

// Render the posts
const renderPosts = function(posts) {
    const postsSection = document.querySelector('.posts');
    postsSection.replaceChildren();

    posts.forEach(post => {
        postsSection.appendChild(createPost(post));
    });
};

const createPost = function(post) {
    const template = document.querySelector('#post-template').content;
    const newPost = template.querySelector('div').cloneNode(true);

    newPost.classList.add(post.status);
    newPost.querySelector('.post-text').textContent = post.text;

    return newPost;
}