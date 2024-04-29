import React, { useState, useMemo, useEffect } from "react";
import PropTypes from "prop-types";
import cn from "classnames";
import countryList from "react-select-country-list";
import styles from "./DetailsClubsFinale.module.scss"
import Chatbot from "../../components/chatbot/Chatbot";
import Navbar from "../../components/navbar/navbar";
import Footer from "../../components/Footer/Footer";
import CarouselItem from "./CarouselItem";
import CarouselSecond from "./carouselSecond";
import CarouselThird from "./CarouselThird";
import CarouselFeedback from "./CarouselFeedback";
import { Slide } from '@mui/material';

function ScrollToTop() {
  useEffect(() => {
    window.scrollTo(0, 0);
  }, []);

  return null;
}

function DetailsClubsFinale(props) {
 

  return (
    <div>
      <Navbar/>
       <Chatbot/>
      <div className={styles.clubsdetailscontainer}> 
      
      <div className={styles.descrContainer}>
        <div className={styles.descText}>
        <h1 className={styles.subtitle_box}>
          <span className={styles.subtitle}>
            <span className={styles.subtitle_span1}>School of {" "}</span>
            <span className={styles.subtitle_span0}>
              AI Algiers
            </span>
          </span>
        </h1>
        <h3 className={styles.descParagraph}>
        L'École de l'IA d'Alger, fondée en 2018 à l'ESI Alger, est un club scientifique rassemblant des passionnés de l'intelligence artificielle. Son objectif est de permettre aux membres d'explorer leur potentiel dans ce domaine et d'améliorer leurs compétences en IA. 
        </h3>
        </div>
      
      <img className={styles.descImg} src={'/assets/descImg.svg'} alt="alt text" />
      </div>
      <div className={styles.buttonsContainer}>
        <div className={styles.grpButton1}>
       <button className={styles.joinButton}>
        Nous rejoindre
       </button>
       <div className={styles.regarderNousContainer}>
       <img className={styles.regarderNousIcon} src={'/assets/regard.svg'} alt="alt text" />
       Regardez Nous!
       </div>

       </div>

       <div className={styles.lirePlus}>Lire Plus
       <img className={styles.lirePlusArrow} src={'/assets/arrow.svg'} alt="alt text" />
       </div>
      </div>

     <div className={styles.objEqContainer}>
      <div className={styles.eqContainer}>
      <h2 className={styles.subtitle2_box}>
          <span className={styles.subtitle2}>
            <span className={styles.subtitle2_span1}>Notre Meilleure {" "}</span>
            <span className={styles.subtitle2_span0}>
              Equipe
            </span>
          </span>
        </h2> 
        <CarouselItem/>
      </div>
      <div className={styles.objContainer}>
      <img className={styles.objClub} src={'/assets/objClub.svg'} alt="alt text" />
      </div>

      </div>

      <div className={styles.cards1Container}>
      <h2 className={styles.subtitle2_box}>
          <span className={styles.subtitle2}>
            <span className={styles.subtitle2_span1}>Discussions {" "}</span>
            <span className={styles.subtitle2_span0}>
              et cours
            </span>
          </span>
        </h2> 
       <CarouselSecond/>
      </div>

      <div className={styles.cards2Container}>
      <h2 className={styles.subtitle2_box}>
          <span className={styles.subtitle2}>
            <span className={styles.subtitle2_span1}>Principaux {" "}</span>
            <span className={styles.subtitle2_span0}>
            événements
            </span>
          </span>
        </h2> 
       <CarouselThird/>
      </div>

      <div className={styles.whiteContainer}>
        <div className={styles.feedbackContainer}>
        <h2 className={styles.subtitle2_box}>
          <span className={styles.subtitle2}>
            <span className={styles.subtitle2_span1}>Feedback des {" "}</span>
            <span className={styles.subtitle2_span0}>
            participants
            </span>
          </span>
        </h2> 
        <CarouselFeedback/>
        </div>

        <div className={styles.newsContainer}>
            <h2 className={styles.textNewsletter}>Inscrivez-vous pour recevoir notre newsletter</h2>
            <div className={styles.subscribeRow}>
            <div className={styles.input}>
  <input
    type="email"
    placeholder="Votre email"
    style={{ fontSize: '21px', fontFamily: 'Arial, sans-serif',border:'none',outline:'none',textAlign: 'center'  }} // Adjust size and font family
  />
</div>
            
            <button className={styles.subscribeButton}>
                S'inscrire
            </button>
            </div>
        </div>
      </div>
      



      </div>
      <Footer/>
    </div>
  );
}

DetailsClubsFinale.propTypes = {
  className: PropTypes.string,
};

export default DetailsClubsFinale;
