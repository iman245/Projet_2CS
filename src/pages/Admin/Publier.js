import React, { useState, useMemo, useEffect } from "react";
import PropTypes from "prop-types";
import { Link } from 'react-router-dom';
import cn from "classnames";
import SidebarAdm from "../../components/Sidebar/SidebarAdm";
import styles from "./Publier.module.scss";
function ScrollToTop() {
  useEffect(() => {
    window.scrollTo(0, 0);
  }, []);

  return null;
}

function Publier(props) {
 

  return (
    <div className={styles.publierContainer}>
       <SidebarAdm />
       <div>
      
       </div>
       
    </div>
  );
}

Publier.propTypes = {
  className: PropTypes.string,
};

export default Publier;
