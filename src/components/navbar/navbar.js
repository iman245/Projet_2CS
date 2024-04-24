import React, { useState, useEffect } from 'react'
import TopNav from './top-nav'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faBars, faCircleUser, faXmark , faGlobe , faMagnifyingGlass } from '@fortawesome/free-solid-svg-icons'
import logo from '../../assets/images/logo_esi1.svg'
import { Link } from 'react-router-dom'
import listItem from './NavbarItems'
import navImg from '../../assets/images/navImg.jpg'

const Navbar = () => {
    
    const [navSmallSize, setNavSmallSize] = useState(false);
    const [openMenuSmallNav, setOpenMenuSmallNav] = useState(false);
    useEffect(() => {
        const handleResize = () => {
          setNavSmallSize(window.innerWidth < 920);
        };
    
        handleResize();
    
        window.addEventListener('resize', handleResize);
    
        return () => {
          window.removeEventListener('resize', handleResize);
        };
      }, []);
  return (
    <div className='navbar-full-container'>
            {!navSmallSize? (
                <div className='navbar-totale'>
                    <div className='navbar-container'>
                        <img className='navbarLogo' src={logo} alt=''></img>
                        <div className='navbar-links'>
                            <div className='navPart1'>
                                <TopNav/>
                            </div>
                            <div className='navPart2'>
                                <ul>
                                    {listItem.map((item)=>{
                                        return(
                                            <li className='navItem'>{item.label}</li>
                                        )
                                    })}
                                    <li><Link to='/Auth'><FontAwesomeIcon icon={faCircleUser} className='NavUserIcon'/></Link></li>
                                </ul>
                            </div>
                        </div>
                    </div>
                    <div className='hoverNavMenuItem'>
                        <div className='sectionHoverMenu'>
                            <img src={navImg} alt='' className='navImg'></img>
                            <div className='navItem-contact'>Contactez-Nous</div>
                            <div className='navItem-Text'>Pour toute question ou demande d'information, n'hésitez pas à nous contacter.</div>
                        </div>
                        <ul className='sectionHoverMenu'>
                                <li className='navItem-title'>Recherche</li>
                                <li className='hoverNavItem'>LMCS</li>
                                <li className='hoverNavItem'>LCSI</li>
                        </ul>
                        <ul className='sectionHoverMenu'>
                                <li className='navItem-title'>Recherche</li>
                                <li className='hoverNavItem'>LMCS</li>
                                <li className='hoverNavItem'>LCSI</li>
                        </ul>
                    </div>
                </div>
            ):( 
                <div className='collapseNavbar-container'>
                    <div className='topSectionNav'>
                        <img className='navCollapLogo' src={logo} alt=''></img>
                            {!openMenuSmallNav ? (
                                <div className='toggleIocnDiv'
                                onClick={() => setOpenMenuSmallNav(!openMenuSmallNav)}
                                >
                                    <FontAwesomeIcon
                                        icon={faBars}
                                        className="toggleIcon"/>MENU
                                </div>
                                
                                ) : (
                                <div className='toggleIocnDiv'
                                onClick={() => setOpenMenuSmallNav(!openMenuSmallNav)}>
                                    <FontAwesomeIcon
                                    icon={faXmark}
                                    alt="icon"
                                    className="toggleIcon"
                                />CLOSE
                                </div>
                                )}
                    </div>
                    <div className='navCollapseListContain'>
                        {openMenuSmallNav && (
                        <div className='navCollapseList'>
                                <div className='NavUserDiv'>
                                    <Link to='/Auth'><FontAwesomeIcon icon={faCircleUser} className='NavUserCollapIcon'/></Link>
                                    <div>
                                        <FontAwesomeIcon icon={faGlobe} style={{color: "#FFFFFF",marginRight:"5px"}} />
                                        <select name="selectedFruit" defaultValue="french">
                                            <option value="french">Francais</option>
                                            <option value="english">Anglais</option>
                                            <option value="arab">Arabe</option>
                                        </select>
                                    </div>
                                    
                                </div>
                                <ul>
                                    <li className='SearchNav-coll'>
                                        <input
                                        className='SearchNav-input'
                                        type='text' placeholder='Chercher via un mot clé ...'
                                        />
                                        <FontAwesomeIcon icon={faMagnifyingGlass} />
                                    </li>
                                    <li className='Nav-coll'>L'école</li>
                                    <li className='Nav-coll'>E-Bachelier</li>
                                    <li className='Nav-coll'>Etudes & académie</li>
                                    <li className='Nav-coll'>Partenariat & Formation</li>
                                </ul>
                                <ul>
                                    <li className='topNav-coll'>
                                        <span className='sdnCollSpan'>SDN</span>
                                        E-Plateforme
                                    </li>
                                    <li className='topNav-coll'>Actualités</li>
                                    <li className='topNav-coll'>Ecole & staff</li>
                                    <li className='topNav-coll'>Evenements</li>
                                    <li className='topNav-coll'>Alumnis</li>
                                    <li className='topNav-coll'>MyESI</li>
                                </ul>
                                
                        </div>
                        )}
                    </div>
                </div>
            )}
        
    </div>
  )
}

export default Navbar