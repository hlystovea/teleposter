function FileForm ({onChange}) {
  return (
    <form encType='multipart/form-data'>
      <input name='files' type='file' accept='image/*' onChange={onChange} multiple />
    </form>
  )
}

export default FileForm;
