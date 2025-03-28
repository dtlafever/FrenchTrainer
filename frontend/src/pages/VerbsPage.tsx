import { useState, useEffect } from 'react';
import { getRandomVerb, FrenchVerb } from '../services/api';
import VerbCard from '../components/VerbCard';
import VerbForm from '../components/VerbForm';

const VerbsPage = () => {
  const [verb, setVerb] = useState<FrenchVerb | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const fetchRandomVerb = async () => {
    setLoading(true);
    setError(null);
    try {
      const data = await getRandomVerb();
      setVerb(data);
    } catch (err) {
      console.error('Error fetching verb:', err);
      setError('Failed to load verb. Please try again.');
      setVerb(null);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchRandomVerb();
  }, []);

  const handleNext = () => {
    fetchRandomVerb();
  };

  const handleVerbCreated = () => {
    // Fetch a new verb after creation
    fetchRandomVerb();
  };

  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="text-3xl font-bold mb-6 text-center">French Verb Conjugations</h1>
      
      <VerbForm onVerbCreated={handleVerbCreated} />
      
      {loading ? (
        <div className="text-center py-8">
          <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-blue-500 mx-auto"></div>
          <p className="mt-4">Loading verb...</p>
        </div>
      ) : error ? (
        <div className="text-center py-8 text-red-600">
          <p>{error}</p>
          <button 
            onClick={fetchRandomVerb}
            className="mt-4 bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
          >
            Try Again
          </button>
        </div>
      ) : verb ? (
        <VerbCard verb={verb} onNext={handleNext} />
      ) : (
        <div className="text-center py-8">
          <p>No verbs available. Please add some verbs using the form above.</p>
        </div>
      )}
    </div>
  );
};

export default VerbsPage;