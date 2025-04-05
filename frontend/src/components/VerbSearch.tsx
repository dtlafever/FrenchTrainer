import { useState } from 'react';
import { searchVerb, FrenchVerb } from '../services/api';

interface VerbSearchProps {
  onVerbFound: (verb: FrenchVerb) => void;
}

const VerbSearch: React.FC<VerbSearchProps> = ({ onVerbFound }) => {
  const [searchTerm, setSearchTerm] = useState('');
  const [isSearching, setIsSearching] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleSearch = async (e: React.FormEvent) => {
    e.preventDefault();
    
    if (!searchTerm.trim()) {
      setError('Please enter a verb to search');
      return;
    }
    
    setIsSearching(true);
    setError(null);
    
    try {
      const verb = await searchVerb(searchTerm);
      onVerbFound(verb);
      setSearchTerm('');
    } catch (err: any) {
      if (err.response && err.response.status === 404) {
        setError(`Verb "${searchTerm}" not found. Please check spelling.`);
      } else {
        setError('Failed to search for verb. Please try again.');
      }
      console.error('Error searching verb:', err);
    } finally {
      setIsSearching(false);
    }
  };

  return (
    <form 
      onSubmit={handleSearch} 
      className="mb-6 bg-white p-4 rounded shadow"
    >
      <div className="flex items-end gap-4">
        <div className="flex-grow">
          <label htmlFor="search-verb" className="block text-gray-700 mb-1">Search for a verb</label>
          <input
            id="search-verb"
            type="text"
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            className="w-full p-2 border rounded focus:border-blue-500 focus:ring-1 focus:ring-blue-500"
            placeholder="e.g. parler"
            required
          />
        </div>
        <button
          type="submit"
          disabled={isSearching}
          className={`bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 ${
            isSearching ? 'opacity-50 cursor-not-allowed' : ''
          }`}
        >
          {isSearching ? 'Searching...' : 'Search'}
        </button>
      </div>
      
      {error && (
        <div className="mt-2 p-2 bg-red-100 text-red-700 rounded text-sm">
          {error}
        </div>
      )}
    </form>
  );
};

export default VerbSearch;