function Status({date, text}) {
  return (
    <div className='status-bar'>
      <div>
          <p>{date}</p>
      </div>
      <div>
          {text}
      </div>
    </div>
  );
}

export default Status;
