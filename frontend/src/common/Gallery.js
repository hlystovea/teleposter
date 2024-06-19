function Gallery({photos = [], className = 'image-gallery'}) {
  switch (photos.length) {
    case 0:
      return ;

    default:
      const items = photos.map((photo) => {
        return (
          <img key={photo.key} src={photo.url} alt={photo.alt} />
        )
      });
      return (
        <div className={className}>
          {items}
        </div>
      );
  }
}

export default Gallery;
