import Logo from './common/Logo';
import Profile from './auth/Profile';

function Header({profile, logout}) {
  return (
    <header>
      <nav className='nav-bar'>
        <ul className='nav-menu'>
          <li>
            <Logo />
          </li>
          <li>
            {profile && <Profile profile={profile} logout={logout} />}
          </li>
        </ul>
      </nav>
    </header>
  );
}

export default Header;
