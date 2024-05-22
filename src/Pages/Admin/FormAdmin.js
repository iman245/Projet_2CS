import React from 'react';
import PropTypes from 'prop-types';
import cn from 'classnames';
import  './FormAdmin.css';

function Admin2(props) {
  return (
    <div className={cn('AdminRoot', props.className, 'admin2')}>
      
      <h1 className="AdminTitle">Publier </h1>
          <div className="AdminIconCircle">
          <svg className="AdminImage1" xmlns="http://www.w3.org/2000/svg" width="0.5em" height="0.5em" viewBox="0 0 24 24"><path fill="currentColor" d="M17 19.22H5V7h7V5H5c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2v-7h-2z"></path><path fill="currentColor" d="M19 2h-2v3h-3c.01.01 0 2 0 2h3v2.99c.01.01 2 0 2 0V7h3V5h-3zM7 9h8v2H7zm0 3v2h8v-2h-3zm0 3h8v2H7z"></path></svg>
          </div>
           
          <div className="AdminContainer">
             <h4 className="AdminHighlight1">Sujet*</h4>
             <div className="AdminRect5">
              <input type="text" className="AdminInput" placeholder="Ecrire le sujet" />
          </div>
          </div>

          <div className="AdminDescriptionContainer">
          <h4 className="AdminHighlight11">Description*</h4>
          <div className="AdminRect6">
        <textarea className="AdminTextarea" placeholder="Ecrire la description"></textarea>
      </div>
      </div>

      <div className="AdminFileContainer">
       <div className=" AdminHighlight">Joindre des fichiers</div>
      {/* <div className="AdminFileIcon"> */}
        <div className='AdminTextRect'>
    <h4 className="AdminText">Déposer un fichier ici</h4>
    <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 36 36" {...props}>
      <path fill="currentColor" d="M31 31H5a1 1 0 0 0 0 2h26a1 1 0 0 0 0-2M8.81 15L17 6.83v20.65a1 1 0 0 0 2 0V6.83L27.19 15a1 1 0 0 0 1.41-1.41L18 3L7.39 13.61A1 1 0 1 0 8.81 15" className="clr-i-outline clr-i-outline-path-1"></path>
      <path fill="none" d="M0 0h36v36H0z"></path>
    </svg>
    </div>
  {/* </div> */}
</div>

<div className="AdminTextContainer">
  <div className="AdminRect3" />
  <div className="AdminText1">Envoyer</div>
</div>

<div className="AdminTextContainer2">
  <div className="AdminRect4" />
  <div className="AdminText2">Annuler</div>
</div>

     










{/*       
      <div className="AdminRect4" />
      <div className="AdminText2">Annuler</div> */}
     
     

    </div>
  );
}

Admin2.propTypes = {
  className: PropTypes.string
};

export default Admin2;
