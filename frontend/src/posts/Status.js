function Status({date, text}) {
  return (
    <div class='status-bar'>
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
