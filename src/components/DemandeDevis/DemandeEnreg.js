import React , { useState , useEffect}from 'react';
import PropTypes from 'prop-types';
import cn from 'classnames';
import styles from './index.module.scss';

function ScrollToTop() {
  useEffect(() => {
    window.scrollTo(0, 0);
  }, []);

  return null;
}

function DemandeEnreg(props) {

   
  
    return (
      <div className={cn(styles.root, props.className, 'demande-devis')}>
       <ScrollToTop />
        <div className={styles.rect1} />
  
        <div className={styles.formDevis} >
        <div className={styles.rect2Enreg} >
        <h2 className={styles.medium_title_box2}>
           <span className={styles.medium_title}>
          <span className={styles.medium_title_span02}>Demande enregistrée avec succès !</span>
          </span>
         </h2>
        </div>
        
       
      </div>
  
  
        <div className={styles.text11}>L’Ecole Nationale Superieure d’Informatique , Tous Droits Réservés </div>
        <p className={styles.paragraph}>
          {`Ecole & staff `}
          <br />
          Nos Alumnis
          <br />
          Nos clubs
          <br />
          Annuaire des enseignants
          <br />
          Futurs Bacheliers
          <br />{' '}
        </p>
        <p className={styles.paragraph1}>
          Partenariats nationale
          <br />
          Partenariats internationale
          <br />
          Maisons d’entreprenariat
          <br />
          Theses et rapports algeriens
          <br />
          Formation continue
          <br />
          Formation Avant promotion
          <br />
          <br />{' '}
        </p>
        <h5 className={styles.highlight4_box}>
          <span className={styles.highlight4}>
            <span className={styles.highlight4_span0}>
              Notre école
              <br />
            </span>
            <span className={styles.highlight4_span1}>
              Ecole Nationale Supérieure <br />
              {`d'Informatique (ESI ex.INI)`}
              <br />
              Alger, Oued Smar 16309
              <br />
              www.esi.dz
              <br />
              023 93 91 32
              <br />
              Carte de l’école
              <br />
              Contactez-nous
            </span>
          </span>
        </h5>
        <h5 className={styles.highlight41}>Notre famille</h5>
        <h5 className={styles.highlight42}>{`partenariats & formation`}</h5>
        <img className={styles.image6} src={'/assets/french_national_assembly_logo.png'} alt="alt text" />
        <img className={styles.image7} src={'/assets/linkedin_social_icon.png'} alt="alt text" />
        <img className={styles.image8} src={'/assets/facebook_social_icon.png'} alt="alt text" />
        <img className={styles.image9} src={'/assets/instagram_social_icon.png'} alt="alt text" />
        <img className={styles.image10} src={'/assets/x_letter_icon.png'} alt="alt text" />
        <div className={styles.rect12} />
        <img className={styles.image11} src={'/assets/french_national_assembly_inverted_logo.png'} alt="alt text" />
        <img className={styles.cover1} src={'/assets/name_is_null.png'} alt="alt text" />
        <div className={styles.rect14} />
        <img className={styles.image91} src={'/assets/abstract_round_shape.png'} alt="alt text" />
        <div className={styles.rect15} />
        <div className={styles.text21}>SDN</div>
        <div className={styles.text22}>E-Plateforme</div>
        <div className={styles.text23}>Actualités</div>
        <div className={styles.text24}>{`Ecole & staff`}</div>
        <div className={styles.text25}>Evenements</div>
        <div className={styles.text26}>Alumnis</div>
        <div className={styles.text27}>MyESI</div>
        <img className={styles.image12} src={'/assets/abstract_wave_shape.png'} alt="alt text" />
        <img className={styles.image13} src={'/assets/abstract_dotted_shape.png'} alt="alt text" />
        <div className={styles.text28}>Français</div>
        <img className={styles.image14} src={'/assets/cc2504418786f2711f9593f3a9a7d2cd.png'} alt="alt text" />
        <img className={styles.image15} src={'/assets/2d5d82a9400afa1df204663b627dbf3e.png'} alt="alt text" />
        <img className={styles.image16} src={'/assets/0ed15c190e16f7fd26013bf79b2ff8cf.png'} alt="alt text" />
        <img className={styles.image17} src={'/assets/23ff70017dd90eb3bcdb62ff83f1fcf9.png'} alt="alt text" />
        <div></div><img className={styles.image18} src={'/assets/solid_circle_icon.png'} alt="alt text" />
        <img className={styles.image19} src={'/assets/pixel_robot_face.png'} alt="alt text" />
      </div>
    );
  }
  
  DemandeEnreg.propTypes = {
    className: PropTypes.string
  };
  
  export default DemandeEnreg;
  