function FileForm ({action}) {
  return (
    <form encType='multipart/form-data'>
      <input name='file' type='file' accept='image/*' onChange={action} />
    </form>
  )
}

export default FileForm;
