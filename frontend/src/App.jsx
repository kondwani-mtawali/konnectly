/* 
App.jsx - 11/28/2025
Manages Routing for pages -> Remove home Page when dev complete
*/
import './App.css'
import { Link, Routes, Route } from "react-router-dom";
import AfricaMap from './pages/AfricaOverview.jsx';
import AfricanCountry from './pages/CountryPage.jsx';
import InvestmentPage from './pages/Investments.jsx';
import BaseTemplate from './pages/BaseTemplate.jsx';

function App() {
  return (
    <BaseTemplate>
      <Routes>
        <Route path="/" element={<AfricaMap />} />
        <Route path="/country/:name" element={<AfricanCountry />} />
        <Route path="/investment/:name" element={<InvestmentPage />} />
      </Routes>
    </BaseTemplate>


  );
}

export default App;