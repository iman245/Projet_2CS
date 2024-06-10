import {React, useState} from 'react';
import  './Post.css';
import Lcsiback from '../../Images/Lcsiback.png';
import lcsib from '../../Images/lcsib.png';
import a from '../../Images/a.png';
import icon from '../../Images/icon.png'
import cardData from '../../db/services.json'
import blog_image from '../../Images/blog_image.png';
import partenaire1 from '../../Images/partenaire1.png';
import partenaire2 from '../../Images/partenaire2.png';
import partenaire3 from '../../Images/partenaire3.png';
import partenaire4 from '../../Images/partenaire4.png';
import partenaire5 from '../../Images/partenaire5.png';
import cardData1 from '../../db/blog.json';




const pageSize = 4; 
// const pageSize1=2;

function Lcsi () {
  const [currentPage, setCurrentPage] = useState(0); 
  const getCurrentPageCards = () => {
    const startIndex = currentPage * pageSize;
    const endIndex = startIndex + pageSize;
    return cardData.slice(startIndex, endIndex);
  };
  const getCurrentPageCard = () => {
    const startIndex = currentPage * pageSize;
    const endIndex = startIndex + pageSize;
    return cardData1.slice(startIndex, endIndex);
  };
  return (
    <section className='lcsi-container'>

      <img className='cover' src={Lcsiback} alt="alt text" />
      <img className='cover' src={lcsib} alt="alt text" />
      <h1 className='hero_title'>Post-Graduation et Recherche</h1>
       
       <div className='ep1'>
       <img className='image' src={a} alt="alt text" />
      <svg className='image1' xmlns="http://www.w3.org/2000/svg"  width="3rem" height="2em" viewBox="0 0 24 24">
        <path fill="currentColor" d="M7 2h10v7.85q0 .575-.25 1.025t-.7.725l-3.55 2.1l.7 2.3H17l-3.1 2.2l1.2 3.8l-3.1-2.35L8.9 22l1.2-3.8L7 16h3.8l.7-2.3l-3.55-2.1q-.45-.275-.7-.725T7 9.85zm4 2v7.05l1 .6l1-.6V4z">
             </path>
       </svg>
      <div className='info'>Excellence</div> 
       </div>

       <div className='ep2'>
       <img className='image' src={a} alt="alt text" />
       <svg  className='image1' xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 48 48" color="#0061B1"  ><g fill="none" stroke="#0061B1" strokeLinecap="round" strokeLinejoin="round" strokeWidth={4}   color="red"><path d="M21 6H9C7.34315 6 6 7.34315 6 9V31C6 32.6569 7.34315 34 9 34H39C40.6569 34 42 32.6569 42 31V21"></path><path d="M24 34V42"></path><path d="M32 6L28 10L32 14"></path><path d="M38 6L42 10L38 14"></path><path d="M14 42L34 42"></path></g></svg>
       <p className='info2'>
           Qualité <br />
           méthodologique
      </p>
       
       </div>
       <div className='ep3'>
       <img className='image' src={a} alt="alt text" />
       <svg className='image1' xmlns="http://www.w3.org/2000/svg" color="#0061B1" width="1em" height="1em" viewBox="0 0 24 24" ><path fill="currentColor" d="M13 3c3.9 0 7 3.1 7 7c0 2.8-1.6 5.2-4 6.3V21H9v-3H8c-1.1 0-2-.9-2-2v-3H4.5c-.4 0-.7-.5-.4-.8L6 9.7C6.2 5.9 9.2 3 13 3m0-2C8.4 1 4.6 4.4 4.1 8.9L2.5 11c-.6.8-.6 1.8-.2 2.6c.4.7 1 1.2 1.7 1.3V16c0 1.9 1.3 3.4 3 3.9V23h11v-5.5c2.5-1.7 4-4.4 4-7.5c0-5-4-9-9-9m-3 9c-.6 0-1-.4-1-1s.4-1 1-1s1 .4 1 1s-.4 1-1 1m3 0c-.6 0-1-.4-1-1s.4-1 1-1s1 .4 1 1s-.4 1-1 1m3 0c-.5 0-1-.4-1-1s.5-1 1-1s1 .4 1 1s-.5 1-1 1"></path></svg>
       <p className='info2'>
      Pensée <br />
        innovante
      </p>
       
       </div>


      <div className='post_rect'>
      <h2 className='post_medium_title'>Prochaine soutenance 2024  </h2>
	<svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 256 256" ><path fill="currentColor" d="m251.76 88.94l-120-64a8 8 0 0 0-7.52 0l-120 64a8 8 0 0 0 0 14.12L32 117.87v48.42a15.9 15.9 0 0 0 4.06 10.65C49.16 191.53 78.51 216 128 216a130 130 0 0 0 48-8.76V240a8 8 0 0 0 16 0v-40.49a115.6 115.6 0 0 0 27.94-22.57a15.9 15.9 0 0 0 4.06-10.65v-48.42l27.76-14.81a8 8 0 0 0 0-14.12M128 200c-43.27 0-68.72-21.14-80-33.71V126.4l76.24 40.66a8 8 0 0 0 7.52 0L176 143.47v46.34c-12.6 5.88-28.48 10.19-48 10.19m80-33.75a97.8 97.8 0 0 1-16 14.25v-45.57l16-8.53Zm-20-47.31l-.22-.13l-56-29.87a8 8 0 0 0-7.52 14.12L171 128l-43 22.93L25 96l103-54.93L231 96Z"></path></svg>

      </div> 
  
      

    </section>
  );
}

export default Lcsi;
