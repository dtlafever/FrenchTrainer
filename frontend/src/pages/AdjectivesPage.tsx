import { useState, useEffect } from 'react';
import { getRandomAdjective, FrenchAdjective } from '../services/api';
import AdjectiveForm from '../components/AdjectiveForm';
import AdjectiveSearch from '../components/AdjectiveSearch';
import AdjectiveCard from '../components/AdjectiveCard';

const AdjectivesPage = () => {
  const [adjective, setAdjective] = useState<FrenchAdjective | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const fetchRandomAdjective = async () => {
    setLoading(true);
    setError(null);
    try {
      const data = await getRandomAdjective();
      setAdjective(data);
    } catch (err) {
      console.error('Error fetching adjective:', err);
      setError('Failed to load adjective. Please try again.');
      setAdjective(null);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchRandomAdjective();
  }, []);

  const handleNext = () => {
    fetchRandomAdjective();
  };

  const handleAdjectiveCreated = (newAdjective: FrenchAdjective) => {
    setAdjective(newAdjective);
  };

  const handleAdjectiveFound = (foundAdjective: FrenchAdjective) => {
    setAdjective(foundAdjective);
  };

  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="text-3xl font-bold mb-6 text-center">French Adjectives</h1>
      
      {/* Search and Random section */}
      <div className="flex justify-center space-x-4 mb-8">
        <AdjectiveSearch onAdjectiveFound={handleAdjectiveFound} />
        <button 
          onClick={fetchRandomAdjective}
          className="bg-purple-600 text-white px-4 py-2 rounded hover:bg-purple-700 flex items-center"
        >
          <span>Random Adjective</span>
        </button>
      </div>
      
      <div className="grid md:grid-cols-1 gap-4 mb-6">
        <div>
          <h2 className="text-xl font-semibold mb-2">Add a New Adjective</h2>
          <AdjectiveForm onAdjectiveCreated={handleAdjectiveCreated} />
        </div>
      </div>
      
      <div className="mt-8">
        <div className="flex justify-between items-center mb-4">
          <h2 className="text-2xl font-semibold">Adjective Details</h2>
        </div>
        
        {loading ? (
          <div className="text-center py-8">
            <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-blue-500 mx-auto"></div>
            <p className="mt-4">Loading adjective...</p>
          </div>
        ) : error ? (
          <div className="text-center py-8 text-red-600">
            <p>{error}</p>
            <button 
              onClick={fetchRandomAdjective}
              className="mt-4 bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
            >
              Try Again
            </button>
          </div>
        ) : adjective ? (
          <AdjectiveCard adjective={adjective} onNext={handleNext} />
        ) : (
          <div className="text-center py-8">
            <p>No adjectives available. Please add some adjectives using the form above.</p>
          </div>
        )}
      </div>
    </div>
  );
};

export default AdjectivesPage;