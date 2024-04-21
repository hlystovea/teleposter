class Post {
    #status;
    #id;

    constructor ({id, status, text}) {
        this.#id = id;
        this.#status = status;
        this.text = text;
    }

    renderPost () {
        const post = document.querySelector('#post-template').content.cloneNode(true);
        const publishButton = post.querySelector('.btn-publish');
        const editButton = post.querySelector('.btn-edit');
        const deleteButton = post.querySelector('.btn-delete');
    
        post.querySelector('.post-text').textContent = this.text;
        publishButton.onclick = this.publishButtonHandler.bind(this);
        editButton.onclick = this.editButtonHandler.bind(this);
        deleteButton.onclick = this.deleteButtonHandler.bind(this);
    
        return post;
    }

    renderForm () {
        const form = document.querySelector('#post-form').content.cloneNode(true);
        const saveButton = form.querySelector('.btn-save');
        const cancelButton = form.querySelector('.btn-cancel');
    
        form.querySelector('.text-input').value = this.text;
        saveButton.onclick = this.submitFormHandler.bind(this);
        cancelButton.onclick = this.cancelButtonHandler.bind(this);
    
        return form;
    }

    appendTo (parent) {
        parent.appendChild(this.renderPost());
    }

    editButtonHandler (event) {
        const post = event.target.closest('.post');
        post.replaceChildren(this.renderForm());
    }

    cancelButtonHandler (event) {
        const post = event.target.closest('.post');
        post.replaceWith(this.renderPost());
    }

    async submitFormHandler (event) {
        event.preventDefault();

        const form = event.target.closest('form');
        const formData = new FormData(document.querySelector('form'));
        const data = Object.fromEntries(formData.entries());

        try {
            const post = await PostData.update(this.#id, data);
            Object.assign(this, { ...post });
            form.parentNode.replaceWith(this.renderPost());
        } catch {
            console.log('Error: ', error);
        };
    }

    async deleteButtonHandler (event) {
        const post = event.target.closest('.post');
        try {
            await PostData.delete(this.#id);
            post.remove();
        } catch (error) {
            console.log('Error: ', error);
        }
    }

    async publishButtonHandler (event) {
        const post = event.target.closest('.post');
        try {
            await PostData.publish(this.#id);
            this.#status = 'published';
            post.replaceWith(this.renderPost());
        } catch (error) {
            console.log('Error: ', error);
        }
    }
}