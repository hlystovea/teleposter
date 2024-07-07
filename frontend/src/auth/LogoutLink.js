import { ReactComponent as LogoutIcon } from './logout.svg';

function LogoutLink({onClick}) {
    return (
        <li onClick={onClick}>
            <LogoutIcon width='24' height='24' fill='beige' />
            Logout
        </li>
    )
}

export default LogoutLink;
