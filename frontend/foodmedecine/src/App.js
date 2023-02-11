import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { Home } from './pages/Home';
import { Suggestion } from './pages/Suggestion';



function App() {
  return (
    <div>
      <Router>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/Suggestions" element={<Suggestion/>} />
          </Routes>
      </Router>
    </div>
  );
}

export default App;
