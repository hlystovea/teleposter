import logo from './logo.png';

function Header() {
  return (
    <header>
      <nav className="nav-bar">
        <ul className="nav-menu">
          <li><a href="/"><img className="logo" src={logo} alt="logo" /></a></li>
          <li><a href="/auth/logout">Выход</a></li>
        </ul>
      </nav>
    </header>
  );
}

export default Header;
