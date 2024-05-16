import React from 'react';
import './Chercheur.css';
import Cherch from '../../Images/Cherch.png';
import { BsTwitterX } from "react-icons/bs";
import { FaLinkedinIn } from "react-icons/fa"; 
import { MdMailOutline } from "react-icons/md"; 




function Chercheur() {
  return (
    <div className="Rechercheur_container">
         <section className='section2'>
     
      <div className='rect3' />
      <img className='image4'src={Cherch} alt="alt text" />
      <img className='image41' src={Cherch} alt="alt text" />
      <h2 className='medium_title'>Linda SAID-ELHAJ</h2>
      <h2 className='medium_title1'>Linda SAID-ELHAJ </h2>
      <div className='text2'>Chercheuse depuis  2014</div>
      <h5 className='highlight'>Maitre de conférence classe B </h5>
   
      {/* <div className='rect4' /> */}
      <div className="menu">
      <a href="#" className="highlight1">Profile</a>
      <a href="#"  className="highlight1">Publication</a>
      <a href="#"  className="highlight1">Projet Recherche</a>
</div>

      <hr className='line' size={1} />
      <h3
        className={
          'subtitle'
        }>{`Darine ELINA, diplômé de l'ESI en 2014, est un entrepreneur accompli dans le domaine de l'intelligence artificielle. Passionné par ce domaine dès ses études, il développe un chatbot performant pour son mémoire de fin d'études. Convaincu du potentiel de sa technologie, il fonde la start-up IA-Solutions avec deux amis, également anciens élèves de l'ESI.`}</h3>
      <h3 className='subtitle1'>Résumé</h3>
      <hr className='rect5' size={1} />
      <h2 className='medium_title11_box'>
        <span className='medium_title11'>
          <span className='medium_title11_span0'>
            Les Défis du Démarrage
            <br />
          </span>
          <span className='medium_title11_span1'></span>
          <span className='medium_title11_span2'>
            {`Les débuts n'ont pas été faciles. Nous avons dû jongler entre les défis techniques, le financement limité et les incertitudes du marché. Mais à chaque obstacle, nous avons trouvé une opportunité de grandir et d'innover. Nous avons appris de nos erreurs et nous avons continué à avancer, guidés par notre passion commune pour l'IA.`}
            <br />
            <br />
          </span>
          <span className='medium_title11_span3'>
            Réalisation du Succès
            <br />
          </span>
          <span className='medium_title11_span4'>
            {`
Aujourd'hui, je suis fier de dire que IA-Solutions est devenue une référence dans le domaine de l'IA. Nos solutions innovantes sont utilisées par des entreprises du monde entier pour résoudre des problèmes complexes et stimuler leur croissance. C'est incroyable de voir comment une simple idée, née dans les salles de classe de l'ESI, a pu se transformer en une entreprise florissante qui impacte positivement le monde.`}
            <br />
            <br />
          </span>
          <span className='medium_title11_span5'>Vers de Nouveaux Horizons</span>
          <span className='medium_title11_span6'>
            <br />
          </span>
          <span className='medium_title11_span7'>
            {`
Mon voyage n'est pas encore terminé, bien sûr. Il y aura de nouveaux défis à relever et de nouvelles innovations à découvrir. Mais je suis convaincu que, avec détermination et passion, rien n'est impossible.`}
            <br />
          </span>
          <span className='medium_title11_span8'>
            <br />
          </span>
          <span className='medium_title11_span9'>
            Motivation
            <br />
          </span>
          <span className='medium_title11_span10'>{`
À tous ceux qui poursuivent leurs rêves, je veux dire : ne laissez jamais personne vous décourager. Croyez en vous-même, suivez votre passion et n'ayez pas peur de prendre des risques. Car c'est dans les défis que se trouvent les plus grandes opportunités.`}</span>
        </span>
      </h2>
      <h5 className='highlight5'>Maitre de conférence classe 1 </h5>
      <BsTwitterX className='image5' />
      <h5 className='highlight5'>Maitre de conférence classe 1 </h5>
      < FaLinkedinIn className='image9' />
      <h5 className='highlight5'>Maitre de conférence classe B </h5>
      <MdMailOutline className='image7' />
     
    
     
     
    </section>
    
    </div>
  );
}

export default Chercheur;

