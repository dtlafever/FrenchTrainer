import { useState } from 'react';
import { createAdjective, FrenchAdjective } from '../services/api';

interface AdjectiveFormProps {
  onAdjectiveCreated: (adjective: FrenchAdjective) => void;
}

const AdjectiveForm: React.FC<AdjectiveFormProps> = ({ onAdjectiveCreated }) => {
  const [formData, setFormData] = useState({
    masc_french_singular: '',
    fem_french_singular: '',
    masc_french_plural: '',
    fem_french_plural: '',
    english_text: ''
  });
  
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    
    // Check if required fields are filled
    if (!formData.masc_french_singular.trim() || !formData.english_text.trim()) {
      setError('Masculine singular form and English translation are required');
      return;
    }
    
    setIsSubmitting(true);
    setError(null);
    
    try {
      const adjective = await createAdjective(formData);
      
      // Reset form
      setFormData({
        masc_french_singular: '',
        fem_french_singular: '',
        masc_french_plural: '',
        fem_french_plural: '',
        english_text: ''
      });
      
      onAdjectiveCreated(adjective);
    } catch (err: any) {
      if (err.response && err.response.data) {
        setError(err.response.data.detail || 'Failed to create adjective');
      } else {
        setError('Failed to create adjective. Please try again.');
      }
      console.error('Error creating adjective:', err);
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <form 
      onSubmit={handleSubmit} 
      className="mb-6 bg-white p-4 rounded shadow"
    >
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
        <div>
          <label htmlFor="masc_french_singular" className="block text-gray-700">Masculine Singular</label>
          <input
            id="masc_french_singular"
            name="masc_french_singular"
            type="text"
            value={formData.masc_french_singular}
            onChange={handleChange}
            className="w-full p-2 border rounded focus:border-blue-500 focus:ring-1 focus:ring-blue-500"
            placeholder="e.g. grand"
            required
          />
        </div>
        
        <div>
          <label htmlFor="fem_french_singular" className="block text-gray-700">Feminine Singular</label>
          <input
            id="fem_french_singular"
            name="fem_french_singular"
            type="text"
            value={formData.fem_french_singular}
            onChange={handleChange}
            className="w-full p-2 border rounded focus:border-blue-500 focus:ring-1 focus:ring-blue-500"
            placeholder="e.g. grande"
          />
        </div>
        
        <div>
          <label htmlFor="masc_french_plural" className="block text-gray-700">Masculine Plural</label>
          <input
            id="masc_french_plural"
            name="masc_french_plural"
            type="text"
            value={formData.masc_french_plural}
            onChange={handleChange}
            className="w-full p-2 border rounded focus:border-blue-500 focus:ring-1 focus:ring-blue-500"
            placeholder="e.g. grands"
          />
        </div>
        
        <div>
          <label htmlFor="fem_french_plural" className="block text-gray-700">Feminine Plural</label>
          <input
            id="fem_french_plural"
            name="fem_french_plural"
            type="text"
            value={formData.fem_french_plural}
            onChange={handleChange}
            className="w-full p-2 border rounded focus:border-blue-500 focus:ring-1 focus:ring-blue-500"
            placeholder="e.g. grandes"
          />
        </div>
      </div>
      
      <div className="mb-4">
        <label htmlFor="english_text" className="block text-gray-700">English Translation</label>
        <input
          id="english_text"
          name="english_text"
          type="text"
          value={formData.english_text}
          onChange={handleChange}
          className="w-full p-2 border rounded focus:border-blue-500 focus:ring-1 focus:ring-blue-500"
          placeholder="e.g. big, large, tall"
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
        {isSubmitting ? 'Adding adjective...' : 'Add Adjective'}
      </button>
    </form>
  );
};

export default AdjectiveForm;