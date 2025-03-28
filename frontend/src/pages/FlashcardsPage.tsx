import { useState, useEffect } from 'react';
import { getRandomFlashcard, Flashcard } from '../services/api';
import FlashcardComponent from '../components/FlashCard';
import FlashcardForm from '../components/FlashcardForm';

const FlashcardsPage = () => {
  const [flashcard, setFlashcard] = useState<Flashcard | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const fetchRandomFlashcard = async () => {
    setLoading(true);
    setError(null);
    try {
      const data = await getRandomFlashcard();
      setFlashcard(data);
    } catch (err) {
      console.error('Error fetching flashcard:', err);
      setError('Failed to load flashcard. Please try again.');
      setFlashcard(null);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchRandomFlashcard();
  }, []);

  const handleNext = () => {
    fetchRandomFlashcard();
  };

  const handleFlashcardCreated = () => {
    // Fetch a new flashcard after creation
    fetchRandomFlashcard();
  };

  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="text-3xl font-bold mb-6 text-center">French Flashcards</h1>
      
      <FlashcardForm onFlashcardCreated={handleFlashcardCreated} />
      
      {loading ? (
        <div className="text-center py-8">
          <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-blue-500 mx-auto"></div>
          <p className="mt-4">Loading flashcard...</p>
        </div>
      ) : error ? (
        <div className="text-center py-8 text-red-600">
          <p>{error}</p>
          <button 
            onClick={fetchRandomFlashcard}
            className="mt-4 bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
          >
            Try Again
          </button>
        </div>
      ) : flashcard ? (
        <FlashcardComponent flashcard={flashcard} onNext={handleNext} />
      ) : (
        <div className="text-center py-8">
          <p>No flashcards available. Please add some flashcards using the form above.</p>
        </div>
      )}
    </div>
  );
};

export default FlashcardsPage;