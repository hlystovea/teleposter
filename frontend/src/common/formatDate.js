const formatDate = (dateString) => {
  const date = new Date(dateString);
  date.setMinutes(date.getMinutes() - new Date().getTimezoneOffset());
  return date.toLocaleDateString('ru-RU',  {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  });
}

export default formatDate;
