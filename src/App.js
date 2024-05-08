import React from 'react';
import './App.css';
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Annuaire from './Pages/Annuaire/Annuaire';
import Enseignants from'./Pages/Annuaire/Enseignants'
import Alumni from './Pages/Annuaire/Alumni';
import Projets from './Pages/Lmcs/Projets';
import Equipe from './Pages/Lmcs/Equipe';
import Lcsi from './Pages/LCSI/Lcsi';
import Chercheur from './Pages/Chercheur/Chercheur';
import Publications from './Pages/Chercheur/Publications'
import Post from './Pages/Postgraduation/Post'
// import Postgraduation from './Pages/Postgraduation/Postgraduation'

function App() {
  return (
    <Router>
     <Routes>
      < Route path ="/" element ={<Annuaire/>}/>
      < Route path ="Enseignants" element={<Enseignants/> }/>
      < Route path ="Alumni" element ={<Alumni/>}/>
      <Route path="Projets" element={<Projets/>}/>
      <Route path="Equipe" element={<Equipe/>}/>
      <Route path="Lcsi" element={<Lcsi/>}/>
      <Route path="Chercheur" element={<Chercheur/>}/>
      <Route path="Publications" element={<Publications/>}/>
      <Route path="Post" element={<Post/>}/>
      {/* <Route path="Postgraduation" element={<Postgraduation/>}/> */}

      {/* <Route path="AvantPromo" element={<AvantPromo/>}/> */}
    </Routes>
    </Router>
  
    
  );
}

export default App;
