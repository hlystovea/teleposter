import { useState } from 'react';
import ProfileLogo from './ProfileLogo';
import LogoutLink from './LogoutLink';

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
        {isOpenMenu && (
          <ul className={`profile__menu ${isOpenMenu ? 'show' : ''}`}>
            <LogoutLink onClick={onLogout}/>
          </ul>
        )}
      </div>
    )
}

export default Profile;
