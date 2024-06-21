function FileForm ({onChange}) {
  return (
    <form encType='multipart/form-data'>
      <input name='file' type='file' accept='image/*' onChange={onChange} />
    </form>
  )
}

export default FileForm;
