import uploadFile from '../files/apiClient';
import FileForm from '../files/fileForm';

const mediaUrl = process.env.REACT_APP_MEDIA_URL;

function Gallery({newFiles, setNewFiles, files = [], setFiles = () => undefined, className = 'image-gallery', isEditing = true}) {
  const photos = [...files, ...newFiles].map((file, index) => {
    return {
      key: file + index,
      name: file,
      url: `${mediaUrl}${file}`,
      alt: file,
    };
  })
  const onChangeFileInput = async (event) => {
    event.preventDefault();
    const form = event.target.closest('form');
    const data = new FormData(form);
    const uploadedFile = await uploadFile(data);
    if (!uploadedFile) {
      console.log('File upload error');
      return ;
    }
    addFile(uploadedFile.file_name);
    form.reset();
  };
  const addFile = (file) => {
    setNewFiles([...newFiles, file]);
  };
  const removeFile = (file) => {
    setFiles(files.filter(item => item !== file));
    setNewFiles(newFiles.filter(item => item !== file))
  };
  const items = photos.map((photo) => {
    const onClick = () => {
      removeFile(photo.name);
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
      {isEditing && <FileForm onChange={onChangeFileInput} />}
    </div>
  );
}

export default Gallery;
