import { useState } from 'react';
import ProfileLogo from './ProfileLogo';
import LogoutItem from './LogoutItem';

function Profile({profile, logout}) {
    const [isOpenMenu, setIsOpenMenu] = useState(false);
    const onClick = () => {
      setIsOpenMenu(!isOpenMenu);
    }
    const onLogout = () => {
      setIsOpenMenu(!isOpenMenu);
      logout();
    }
    return (
      <div className='profile'>
        <ProfileLogo profile={profile} onClick={onClick} />
        <ul className={`profile__menu ${isOpenMenu ? 'show' : ''}`}>
          <li>{profile.first_name} {profile.last_name}</li>
          <li>@{profile.username}</li>
          <li className='profile__menu__item' onClick={onLogout}><LogoutItem /></li>
        </ul>
      </div>
    )
}

export default Profile;
