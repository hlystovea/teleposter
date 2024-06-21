const Form = ({id, buttons, onSubmit, textValue, setTextValue}) => {
  const rows = textValue.split('\n').length;
  const onTextChange = (event) => {
    const input = event.target;
    setTextValue(input.value);
    input.style.height = '1px';
    input.style.height = input.scrollHeight + 'px';
  };
  return (
    <>
      <form id={id} onSubmit={onSubmit}>
        <textarea
          className='text-input'
          rows={rows}
          name='text'
          value={textValue}
          onChange={onTextChange}
          autoFocus
        />
      </form>
      {buttons}
    </>
  );
}

export default Form;
