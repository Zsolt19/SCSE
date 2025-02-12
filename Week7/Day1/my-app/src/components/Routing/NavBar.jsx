import React from 'react';
import {Link} from 'react-router-dom';

const NavBar = () =>{
    return(
        <>
        <ul>
            <Link to='/'><li>Homepage</li></Link>
            <Link to='/SecondPage'><li>Second Page</li></Link>
            <li></li>
        </ul>
        </>
    )
}

export default NavBar;