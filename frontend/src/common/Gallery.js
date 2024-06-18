function Gallery({photos = [], className = 'image-gallery'}) {
  switch (photos.length) {
    case 0:
      return ;

    case 1:
      return (
        <img className='post-image' key={photos[0].key} src={photos[0].url} alt={photos[0].alt} />
      );

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
