// Update the posts
async function updatePosts() {
    await fetch('api/v1/posts')
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
    const postsBlock = document.querySelector('.posts');
    postsBlock.replaceChildren();

    posts.forEach(post => {
        postsBlock.appendChild(createPost(post));
    });
};

// Return a new post
const createPost = function(post) {
    const template = document.querySelector('#post-template').content;
    const newPost = template.querySelector('div').cloneNode(true);

    newPost.classList.add(post.status);
    newPost.id = post.id;
    newPost.querySelector('.post-text').textContent = post.text;

    newPost.querySelector('.btn-post-delete').onclick = () => {
        deletePost(post.id)
    }

    return newPost;
};

// Delete a post
async function deletePost(id) {
    post = document.getElementById(id);
    if (post) {
        post.remove();
        await fetch('api/v1/posts/' + id, {
            method: 'DELETE',
        })
    }
};
