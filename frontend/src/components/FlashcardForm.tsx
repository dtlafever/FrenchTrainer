import { useState } from 'react';
import { createFlashcard } from '../services/api';

interface FlashcardFormProps {
  onFlashcardCreated: () => void;
}

const FlashcardForm: React.FC<FlashcardFormProps> = ({ onFlashcardCreated }) => {
  const [question, setQuestion] = useState('');
  const [answer, setAnswer] = useState('');
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    
    if (!question.trim() || !answer.trim()) {
      setError('Both question and answer are required');
      return;
    }
    
    setIsSubmitting(true);
    setError(null);
    
    try {
      await createFlashcard({ question, answer });
      setQuestion('');
      setAnswer('');
      onFlashcardCreated();
    } catch (err) {
      setError('Failed to create flashcard. Please try again.');
      console.error('Error creating flashcard:', err);
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <form 
      onSubmit={handleSubmit} 
      className="mb-6 bg-white p-4 rounded shadow"
    >
      <div className="mb-4">
        <label htmlFor="question" className="block text-gray-700">Question (French)</label>
        <input
          id="question"
          type="text"
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          className="w-full p-2 border rounded focus:border-blue-500 focus:ring-1 focus:ring-blue-500"
          placeholder="e.g. Bonjour"
          required
        />
      </div>
      
      <div className="mb-4">
        <label htmlFor="answer" className="block text-gray-700">Answer (English)</label>
        <input
          id="answer"
          type="text"
          value={answer}
          onChange={(e) => setAnswer(e.target.value)}
          className="w-full p-2 border rounded focus:border-blue-500 focus:ring-1 focus:ring-blue-500"
          placeholder="e.g. Hello"
          required
        />
      </div>
      
      {error && (
        <div className="mb-4 p-2 bg-red-100 text-red-700 rounded">
          {error}
        </div>
      )}
      
      <button
        type="submit"
        disabled={isSubmitting}
        className={`bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 ${
          isSubmitting ? 'opacity-50 cursor-not-allowed' : ''
        }`}
      >
        {isSubmitting ? 'Adding...' : 'Add Flashcard'}
      </button>
    </form>
  );
};

export default FlashcardForm;