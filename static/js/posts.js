async function updatePosts() {
    fetch('api/v1/posts')
    .then(response => response.json())
    .then(data => {
        renderPosts(data);
    })
    .catch(error => {
        console.log('Error: ', error);
    });
}

const renderPosts = function(posts) {
    const postsBlock = document.querySelector('.posts');
    postsBlock.replaceChildren();

    posts.forEach(post => {
        postsBlock.appendChild(createPost(post));
    });
}

const createPost = function(post) {
    const template = document.querySelector('#post-template').content;
    const newPost = template.querySelector('div').cloneNode(true);
    const publishButton = newPost.querySelector('.btn-post-publish');
    const editButton = newPost.querySelector('.btn-post-edit');
    const deleteButton = newPost.querySelector('.btn-post-delete');

    newPost.classList.add(post.status);
    newPost.id = post.id;
    newPost.querySelector('.post-text').textContent = post.text;

    publishButton.onclick = async () => publishPost(newPost);
    editButton.onclick = async () => renderForm(newPost);
    deleteButton.onclick = async () => deletePost(newPost);

    return newPost;
}

async function publishPost(post) {
    fetch(`api/v1/posts/${post.id}/publish`, {
        method: 'POST',
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(response.text());
        }
        post.remove();
    })
    .catch(error => {
        console.log('Error: ', error);
    });
}

async function renderForm(post) {
    const form = document.querySelector('#post-form').content.cloneNode(true);
    const saveButton = form.querySelector('.btn-post-save');

    const textInput = form.querySelector('.text-input');
    textInput.value = post.querySelector('.post-text').textContent;

    post.replaceChildren(form);
    saveButton.onclick = async () => editPost(form, post);
}

async function editPost(form, post) {
    const formData = new FormData(document.querySelector('form'));
    const data = Object.fromEntries(formData.entries());
    const jsonData = JSON.stringify(data);

    fetch(`api/v1/posts/${post.id}`, {
        method: 'PATCH',
        body: jsonData,
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(response.text());
        }
    })
    .catch(error => {
        console.log('Error: ', error);
    });
}


// Delete a post
async function deletePost(post) {
    fetch(`api/v1/posts/${post.id}`, {
        method: 'DELETE',
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(response.text());
        }
        post.remove();
    })
    .catch(error => {
        console.log('Error: ', error);
    });
}
