import uploadFile from '../files/apiClient';
import FileForm from '../files/fileForm';

function Gallery({photos, deletePhoto, addPhoto, className = 'image-gallery', isEditing = false}) {
  const onFileFormSubmit = async (event) => {
    event.preventDefault();
    const form = event.target.closest('form');
    const data = new FormData(form);
    const uploadedFile = await uploadFile(data);
    if (!uploadedFile) {
      console.log('File upload error');
      return ;
    }
    addPhoto(uploadedFile.file_name);
  };
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
      {isEditing && <FileForm action={onFileFormSubmit} />}
    </div>
  );
}

export default Gallery;
