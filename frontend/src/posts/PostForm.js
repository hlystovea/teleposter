function PostForm({ text="", caption="" }) {
  return (
    <form action="" method="POST">
        <textarea class="text-input" name="text" autofocus>{text || caption}</textarea>
        <input type="file" accept="image/*" />
        <button class="btn-save" name="saveButton" type="button">
            Сохранить
        </button>
        <button class="btn-cancel" name="cancelButton" type="button">
            Отмена
        </button>
    </form>
  );
}

export default PostForm;
