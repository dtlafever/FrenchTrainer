import { Link, useLocation } from 'react-router-dom';

const Navigation = () => {
  const location = useLocation();
  
  const isActive = (path: string) => {
    return location.pathname === path;
  };

  return (
    <nav className="bg-blue-600 text-white p-4">
      <div className="container mx-auto flex flex-col md:flex-row justify-between items-center">
        <Link to="/" className="text-2xl font-bold mb-4 md:mb-0">
          French Trainer
        </Link>
        
        <div className="flex space-x-4">
          <Link
            to="/"
            className={`px-3 py-2 rounded ${
              isActive('/') ? 'bg-blue-800' : 'hover:bg-blue-700'
            }`}
          >
            Flashcards
          </Link>
          
          <Link
            to="/verbs"
            className={`px-3 py-2 rounded ${
              isActive('/verbs') ? 'bg-blue-800' : 'hover:bg-blue-700'
            }`}
          >
            Verb Conjugations
          </Link>
          
          <a
            href="http://localhost:8000/chat"
            target="_blank"
            rel="noopener noreferrer"
            className="px-3 py-2 rounded hover:bg-blue-700"
          >
            Chat with LLM
          </a>
        </div>
      </div>
    </nav>
  );
};

export default Navigation;