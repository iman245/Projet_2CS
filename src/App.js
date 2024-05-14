import './App.css';
import { BrowserRouter, Route, Routes } from "react-router-dom";
import LandingPage from './pages/LandingPage/LandingPage';
import Evenements from './pages/EventsPage/Evenements';
import Authentification from './pages/Authentification/Authentification';
import Annuaire from './pages/Annuaire/Annuaire';
import Enseignants from'./pages/Annuaire/Enseignants'
import Alumni from './pages/Annuaire/Alumni';
import Projets from './pages/Lmcs/Projets';
import Equipe from './pages/Lmcs/Equipe';
import Sidebar from './components/SidebarAdmin/Sidebar';
import Clubs from './pages/Clubs/Clubs';

import AvantPromo from './pages/AvantPromo/index'
import CatalogueFormation from './pages/CatalogueFormations/index'
import DemandeDevis from './pages/DemandeDevis/index'
import DemandeEnregistree from './pages/DemandeDevis/DemandeEnreg'
import DF from './pages/DF/index'
import DemandePartenariatFinale from './pages/DemandePartenariatFinale/DemandePartenariatFinale';
import DetailsClubsFinale from './pages/DetailsClubsFinale/DetailsClubsFinale';
import ClubsFinal from './pages/ClubsFinal/ClubsFinal';
import EsiFinal from './pages/EsiFinal/EsiFinal';
import SuccessStories from './pages/SuccessStories/SuccessStories';
import Contact from './pages/ContactRelex/Contact';
import ProgrammeFinal from './pages/Programme/ProgrammeFinal';
import DetailsPgme from './pages/DetailsPgme/DetailsPgme';
import Specialites from './pages/Specialites/Specialites';

function App() {
  return (
    <div className="App">
      <BrowserRouter>
      <Routes>
        <Route path='/' element={<LandingPage/>}></Route>
        <Route path='/EventList' element={<Evenements/>}></Route>
        <Route path='/Auth' element={<Authentification/>}></Route>
        < Route path ="/AnnuaireAdmin" element ={<Annuaire/>}/>
        < Route path ="/AnnuaireEnseignants" element={<Enseignants/> }/>
        < Route path ="/AnnuaireAlumni" element ={<Alumni/>}/>
        < Route path ="/LMCSProjects" element ={<Projets/>}/>
        < Route path ="/LMCSTeams" element ={<Equipe/>}/>


        < Route path ="/AvantPromo" element ={<AvantPromo/>}/>
        < Route path ="/CatalogueFormation" element ={<CatalogueFormation/>}/>
        < Route path ="/DemandeDevis" element ={<DemandeDevis/>}/>
        < Route path ="/DemandeEnregistree" element ={<DemandeEnregistree/>}/>
        < Route path ="/DetailsFormation" element ={<DF/>}/>
        < Route path ="/DemandePartenariatFinale" element ={<DemandePartenariatFinale/>}/>
        < Route path ="/DetailsClubsFinale" element ={<DetailsClubsFinale/>}/>
        <Route path='/Clubs' element={<Clubs/>}></Route>
        < Route path ="/ClubsFinal" element ={<ClubsFinal/>}/>
        <Route path='/EsiFinal' element={<EsiFinal/>}></Route>
        <Route path='/SuccessStories' element={<SuccessStories/>}></Route>
        <Route path='/Contact' element={<Contact/>}></Route>
        <Route path='/ProgrammeFinal' element={<ProgrammeFinal/>}></Route>
        <Route path='/DetailsPgme' element={<DetailsPgme/>}></Route>
        <Route path='/Specialites' element={<Specialites/>}></Route>
        




      </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
/*
<Navbar/>
      
*/
