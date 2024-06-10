import { Sidebar, Menu, MenuItem, SubMenu } from 'react-pro-sidebar';
import styles from './SidebarAdm.module.scss';
import Box from '@mui/material/Box';


function textMenu(icon, text) {
  return (
    <div className={styles.MenuItemContainer}>
      <img src={icon} alt="icon" className={styles.icon} />
      <div className={styles.menuText}>{text}</div>
    </div>
  )
  }
export default function SidebarAdm() {
  return (
    <div className={styles.container}>
      <Sidebar className={styles.sidebarContainer}>
       
        <Menu className={styles.menuContainer}>
        <img src='/assets/logoSidebar.svg' alt="logo" className={styles.logo} />
          <SubMenu label="Main Boards"  className={styles.SubMenu}>
            <MenuItem className={styles.widthMenu}>{textMenu('/assets/dashoard.svg','Dashboard')}</MenuItem>
          </SubMenu>
          <SubMenu label="Publication"  className={styles.SubMenu}>
            <MenuItem className={styles.widthMenu}>{textMenu('/assets/pubIcon.svg','Publication')}</MenuItem>
            <MenuItem className={styles.widthMenu}>{textMenu('/assets/hourglass.svg','Publication en attente')}</MenuItem>
            <MenuItem className={styles.widthMenu}>{textMenu('/assets/publierIcon.svg','Publier')}</MenuItem>
            <MenuItem className={styles.widthMenu}>{textMenu('/assets/trash.svg','Demande suppression')}</MenuItem>
            <MenuItem className={styles.widthMenu}>{textMenu('/assets/history.svg','Historique de publication')}</MenuItem>
          </SubMenu>

          <SubMenu label="Parametres"  className={styles.SubMenu}>
            <MenuItem className={styles.widthMenu}>{textMenu('/assets/profile.svg','Profil')}</MenuItem>
            <MenuItem className={styles.widthMenu}>{textMenu('/assets/deconnect.svg','Se Deconnecter')}</MenuItem>
          </SubMenu>
        </Menu>
      </Sidebar>
    </div>
  );
}
