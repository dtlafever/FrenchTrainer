import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Layout from './components/Layout';
import FlashcardsPage from './pages/FlashcardsPage';
import VerbsPage from './pages/VerbsPage';
import Adjectives from './pages/Adjectives';
import './index.css';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<FlashcardsPage />} />
          <Route path="verbs" element={<VerbsPage />} />
          <Route path="adjectives" element={<Adjectives />} />
        </Route>
      </Routes>
    </Router>
  );
}

export default App;
