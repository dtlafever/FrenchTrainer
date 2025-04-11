import { useState } from 'react';
import { searchAdjectives, FrenchAdjective } from '../services/api';

interface AdjectiveSearchProps {
  onAdjectiveFound: (adjective: FrenchAdjective) => void;
}

const AdjectiveSearch: React.FC<AdjectiveSearchProps> = ({ onAdjectiveFound }) => {
  const [searchTerm, setSearchTerm] = useState('');
  const [isSearching, setIsSearching] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleSearch = async (e: React.FormEvent) => {
    e.preventDefault();
    
    if (!searchTerm.trim()) {
      setError('Please enter an adjective to search');
      return;
    }
    
    setIsSearching(true);
    setError(null);
    
    try {
      const results = await searchAdjectives(searchTerm);
      if (results) {
        onAdjectiveFound(results);
        setSearchTerm('');
      } else {
        setError(`Adjective "${searchTerm}" not found. Please check spelling.`);
      }
    } catch (err: any) {
      if (err.response && err.response.status === 404) {
        setError(`Adjective "${searchTerm}" not found. Please check spelling.`);
      } else {
        setError('Failed to search for adjective. Please try again.');
      }
      console.error('Error searching adjective:', err);
    } finally {
      setIsSearching(false);
    }
  };

  return (
    <form onSubmit={handleSearch} className="flex items-center">
      <div className="relative">
        <input
          type="text"
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          className="w-full p-2 pr-10 border rounded-l focus:border-blue-500 focus:ring-1 focus:ring-blue-500"
          placeholder="Search for an adjective"
        />
        {error && (
          <div className="absolute left-0 right-0 top-full mt-1 p-2 bg-red-100 text-red-700 rounded text-sm z-10">
            {error}
          </div>
        )}
      </div>
      <button
        type="submit"
        disabled={isSearching}
        className={`bg-blue-500 text-white px-4 py-2 rounded-r hover:bg-blue-600 ${
          isSearching ? 'opacity-50 cursor-not-allowed' : ''
        }`}
      >
        {isSearching ? (
          <span className="flex items-center">
            <svg className="animate-spin -ml-1 mr-2 h-4 w-4 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
              <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
              <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
            </svg>
            Searching...
          </span>
        ) : (
          <span>Search</span>
        )}
      </button>
    </form>
  );
};

export default AdjectiveSearch;