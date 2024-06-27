import Logo from './common/Logo';

function Header() {
  return (
    <header>
      <nav className='nav-bar'>
        <ul className='nav-menu'>
          <li>
            <Logo />
          </li>
          <li><a href='/auth/logout'>Выход</a></li>
        </ul>
      </nav>
    </header>
  );
}

export default Header;
