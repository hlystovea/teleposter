function ProfileLogo({profile, onClick}) {
  return (
    <img className='profile__logo' src={profile.photo_url} alt={profile.username} onClick={onClick} />
  )
}

export default ProfileLogo;
