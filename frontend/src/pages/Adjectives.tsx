import { useState, useEffect } from 'react';
import { FrenchAdjective, fetchAdjectives, searchAdjectives } from '../services/api';
import AdjectiveCard from '../components/AdjectiveCard';

const Adjectives: React.FC = () => {
  const [adjectives, setAdjectives] = useState<FrenchAdjective[]>([]);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [searchQuery, setSearchQuery] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  
  useEffect(() => {
    const loadAdjectives = async () => {
      setIsLoading(true);
      const data = await fetchAdjectives();
      if (data && data.length > 0) {
        setAdjectives(data);
        // Randomly select an adjective to start with
        setCurrentIndex(Math.floor(Math.random() * data.length));
      }
      setIsLoading(false);
    };
    
    loadAdjectives();
  }, []);
  
  const handleSearch = async () => {
    if (!searchQuery.trim()) {
      return;
    }
    
    setIsLoading(true);
    const results = await searchAdjectives(searchQuery.trim());
    if (results && results.length > 0) {
      setAdjectives(results);
      setCurrentIndex(0);
    } else {
      alert('No adjectives found matching your search.');
    }
    setIsLoading(false);
  };
  
  const handleNextAdjective = () => {
    // Go to the next adjective or cycle back to the first
    setCurrentIndex((prevIndex) => 
      prevIndex + 1 >= adjectives.length ? 0 : prevIndex + 1
    );
  };
  
  const handleRandomAdjective = () => {
    if (adjectives.length > 1) {
      let newIndex;
      do {
        newIndex = Math.floor(Math.random() * adjectives.length);
      } while (newIndex === currentIndex);
      setCurrentIndex(newIndex);
    }
  };
  
  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-6 text-center">French Adjectives</h1>
      
      <div className="mb-8 flex flex-col md:flex-row gap-4 items-center justify-center">
        <div className="flex w-full md:w-auto">
          <input
            type="text"
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            placeholder="Search adjectives (any form)"
            className="px-4 py-2 border border-gray-300 rounded-l focus:outline-none focus:ring-2 focus:ring-blue-500 flex-grow"
            onKeyPress={(e) => e.key === 'Enter' && handleSearch()}
          />
          <button
            onClick={handleSearch}
            disabled={isLoading}
            className="bg-blue-500 text-white px-4 py-2 rounded-r hover:bg-blue-600 disabled:bg-blue-300"
          >
            {isLoading ? 'Searching...' : 'Search'}
          </button>
        </div>
        
        <button
          onClick={handleRandomAdjective}
          disabled={adjectives.length <= 1}
          className="bg-purple-500 text-white px-4 py-2 rounded hover:bg-purple-600 disabled:bg-purple-300"
        >
          Random Adjective
        </button>
      </div>
      
      {adjectives.length > 0 ? (
        <AdjectiveCard 
          adjective={adjectives[currentIndex]}
          onNext={handleNextAdjective}
        />
      ) : isLoading ? (
        <div className="text-center py-10">
          <p className="text-lg">Loading adjectives...</p>
        </div>
      ) : (
        <div className="text-center py-10">
          <p className="text-lg">No adjectives found. Please try a different search.</p>
        </div>
      )}
      
      <div className="mt-8 text-center text-sm text-gray-500">
        <p>Showing {adjectives.length > 0 ? `${currentIndex + 1} of ${adjectives.length}` : '0'} adjectives</p>
      </div>
    </div>
  );
};

export default Adjectives;
