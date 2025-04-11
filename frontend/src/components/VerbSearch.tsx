import { useState, useEffect } from 'react';
import { searchVerb, FrenchVerb } from '../services/api';

interface VerbSearchProps {
  onVerbFound: (verb: FrenchVerb) => void;
}

const VerbSearch: React.FC<VerbSearchProps> = ({ onVerbFound }) => {
  const [searchTerm, setSearchTerm] = useState('');
  const [isSearching, setIsSearching] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [isModalOpen, setIsModalOpen] = useState(false);

  const handleSearch = async (e: React.FormEvent) => {
    e.preventDefault();
    
    if (!searchTerm.trim()) {
      setError('Please enter a verb to search');
      return;
    }
    
    setIsSearching(true);
    setError(null);

    if (isSearching) {
      console.log('Searching for Verb...');
    }
    
    try {
      const verb = await searchVerb(searchTerm);
      onVerbFound(verb);
      setSearchTerm('');
      setIsModalOpen(false); // Close modal after successful search
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

  const openModal = () => {
    setIsModalOpen(true);
    setSearchTerm(''); // Clear the search term when opening the modal
    setError(null); // Clear any previous errors
  };

  const closeModal = () => {
    setIsModalOpen(false);
    setError(null);
  };

  // Handle backdrop click to close modal
  const handleBackdropClick = (e: React.MouseEvent) => {
    // Only close if the click was directly on the backdrop, not on its children
    if (e.target === e.currentTarget) {
      closeModal();
    }
  };

  // Add ESC key listener
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'Escape' && isModalOpen) {
        closeModal();
      }
    };

    // Add the event listener when modal opens
    if (isModalOpen) {
      document.addEventListener('keydown', handleKeyDown);
    }
    
    // Cleanup function to remove event listener
    return () => {
      document.removeEventListener('keydown', handleKeyDown);
    };
  }, [isModalOpen]); // Dependency array includes isModalOpen to re-register listener

  return (
    <>
      {/* Compact Search Button with Text */}
      <button
        type="button"
        onClick={openModal}
        className="bg-blue-900 text-white px-4 py-2 rounded-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 flex items-center space-x-2"
        aria-label="Search for a verb"
      >
        <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
        </svg>
        <span>Search</span>
      </button>

      {/* Search Modal with semi-transparent background blue-900 */}
      {isModalOpen && (
        <div 
          className="fixed inset-0 bg-[#1c388e92] backdrop-blur-xs flex items-center justify-center z-50 p-4"
          onClick={handleBackdropClick}  // Add click handler to backdrop
        >
          <div className="bg-white rounded-lg shadow-xl w-full max-w-sm">
            <form onSubmit={handleSearch} className="p-3">
              <div className="mb-3">
                <input
                  id="search-verb"
                  type="text"
                  value={searchTerm}
                  onChange={(e) => setSearchTerm(e.target.value)}
                  className="w-full p-2 border rounded focus:border-blue-500 focus:ring-1 focus:ring-blue-500"
                  placeholder="Search Verb (any tense)"
                  required
                  autoFocus
                />
                
                {error && (
                  <div className="mt-2 p-2 bg-red-100 text-red-700 rounded text-sm">
                    {error}
                  </div>
                )}
              </div>
            </form>
          </div>
        </div>
      )}
    </>
  );
};

export default VerbSearch;