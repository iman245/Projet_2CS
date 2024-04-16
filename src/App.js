import './App.css';
import { BrowserRouter, Route, Routes } from "react-router-dom";
import LandingPage from './pages/LandingPage/LandingPage';
import Evenements from './pages/EventsPage/Evenements';
import Authentification from './pages/Authentification/Authentification';


function App() {
  return (
    <div className="App">
      <BrowserRouter>
      <Routes>
        <Route path='/' element={<LandingPage/>}></Route>
        <Route path='/EventList' element={<Evenements/>}></Route>
        <Route path='/Auth' element={<Authentification/>}></Route>
      </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
/*
<Navbar/>
      
*/