function Gallery({photos = [], className = 'image-gallery'}) {
  if (photos.length === 0) {
    return ;
  }
  const items = photos.map((photo) => {
      return (
        <img key={photo.key} src={photo.url} className={photo.className} alt={photo.alt} />
      )
    });
  return (
    <div className={className}>
      {items}
    </div>
  );
}

export default Gallery;
