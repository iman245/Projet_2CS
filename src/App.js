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
import NavbarAdmin from './components/navbar/NavbarAdmin';


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
        < Route path ="/coucou" element={<Sidebar/>}/>
      </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
/*
<Navbar/>
      
*/
