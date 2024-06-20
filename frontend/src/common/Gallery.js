function Gallery({photos, deletePhoto, className = 'image-gallery', isEditing = false}) {
  switch (photos.length) {
    case 0:
      return ;

    default:
      const items = photos.map((photo) => {
        const onClick = () => {
          deletePhoto(photo.name);
        }
        const button = <button onClick={onClick}>x</button>;
        return (
          <div key={photo.key}>
            <img src={photo.url} alt={photo.alt} />
            {isEditing && button}
          </div>
        );
      });
      return (
        <div className={className}>
          {items}
        </div>
      );
  }
}

export default Gallery;
