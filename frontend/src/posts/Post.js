function Post({post}) {
  const { id, text, status, photo, caption } = post;
  return (
    <div className="post">
      <div className="post-photo">
        <img src={photo} alt="Фото" /> 
      </div>
      <p className="post-text">{text || caption}</p>
      <span className="post-status">{status}</span>
      <button className="btn-publish" name="publishButton" type="button">
        Опубликовать
      </button>
      <button className="btn-edit" name="editButton" type="button">
        Редактировать
      </button>
      <button className="btn-delete" name="deleteButton" type="button">
        Удалить
      </button>
    </div>
  );
}

export default Post;
