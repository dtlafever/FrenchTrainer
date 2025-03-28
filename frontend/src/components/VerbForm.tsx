import { useState } from 'react';
import { createVerb } from '../services/api';

interface VerbFormProps {
  onVerbCreated: () => void;
}

const VerbForm: React.FC<VerbFormProps> = ({ onVerbCreated }) => {
  const [verb, setVerb] = useState('');
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    
    if (!verb.trim()) {
      setError('Verb is required');
      return;
    }
    
    setIsSubmitting(true);
    setError(null);
    
    try {
      await createVerb(verb);
      setVerb('');
      onVerbCreated();
    } catch (err: any) {
      if (err.response && err.response.status === 404) {
        setError('Verb not found in the dictionary. Please check spelling.');
      } else {
        setError('Failed to create verb. Please try again.');
      }
      console.error('Error creating verb:', err);
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
        <label htmlFor="verb" className="block text-gray-700">French Verb (infinitive form)</label>
        <input
          id="verb"
          type="text"
          value={verb}
          onChange={(e) => setVerb(e.target.value)}
          className="w-full p-2 border rounded focus:border-blue-500 focus:ring-1 focus:ring-blue-500"
          placeholder="e.g. parler"
          required
        />
        <p className="mt-1 text-sm text-gray-500">
          Enter the infinitive form of a French verb (e.g. parler, manger, finir)
        </p>
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
        {isSubmitting ? 'Looking up verb...' : 'Add Verb'}
      </button>
    </form>
  );
};

export default VerbForm;