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
}

// Render the posts
const renderPosts = function(posts) {
    const postsBlock = document.querySelector('.posts');
    postsBlock.replaceChildren();

    posts.forEach(post => {
        postsBlock.appendChild(createPost(post));
    });
}

// Return a new post
const createPost = function(post) {
    const template = document.querySelector('#post-template').content;
    const newPost = template.querySelector('div').cloneNode(true);
    const publishButton = newPost.querySelector('.btn-post-publish');
    const editButton = newPost.querySelector('.btn-post-edit');
    const deleteButton = newPost.querySelector('.btn-post-delete');

    newPost.classList.add(post.status);
    newPost.id = post.id;
    newPost.querySelector('.post-text').textContent = post.text;

    publishButton.onclick = () => publishPost(newPost);
    editButton.onclick = () => editPost(newPost);
    deleteButton.onclick = () => deletePost(newPost);

    return newPost;
}

// Publish a post
async function publishPost(post) {
    await fetch(`api/v1/posts/${post.id}/publish`, {
        method: 'POST',
    }).then(response => {
        if (!response.ok) {
            throw new Error('Ошибка запроса');
        }
        post.remove();
    }).catch(error => {
        console.log(error);
    });
}

// Edit a post
async function editPost(post) {
    const form = document.querySelector('#post-form').content.cloneNode(true);
    const textInput = form.querySelector('.text-input');

    textInput.value = post.querySelector('.post-text').textContent;
    post.replaceChildren(form);
}

// Delete a post
async function deletePost(post) {
    fetch(`api/v1/posts/${post.id}`, {
        method: 'DELETE',
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Ошибка запроса');
        }
        post.remove();
    })
    .catch(error => {
        console.log(error);
    });
}
