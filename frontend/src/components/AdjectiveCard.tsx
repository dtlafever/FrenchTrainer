import { FrenchAdjective, playAudio } from '../services/api';

interface AdjectiveCardProps {
  adjective: FrenchAdjective;
  onNext: () => void;
}

const AdjectiveCard: React.FC<AdjectiveCardProps> = ({ adjective, onNext }) => {
  const handlePlayAudio = async (text: string) => {
    try {
      await playAudio(text);
    } catch (error) {
      console.error('Error playing audio:', error);
    }
  };

  return (
    <div className="bg-white rounded-lg shadow-md overflow-hidden">
      <div className="p-6">
        <div className="mb-4">
          <h3 className="text-2xl font-bold text-gray-800 mb-2">
            {adjective.masc_french_singular}
            <button
              onClick={() => handlePlayAudio(adjective.masc_french_singular)}
              className="ml-2 text-blue-500 hover:text-blue-700"
              aria-label="Play pronunciation"
            >
              <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM9.555 7.168A1 1 0 008 8v4a1 1 0 001.555.832l3-2a1 1 0 000-1.664l-3-2z" clipRule="evenodd" />
              </svg>
            </button>
          </h3>
          <p className="text-gray-600 italic">{adjective.english_text}</p>
        </div>

        <div className="grid grid-cols-2 gap-4 mb-6">
          <div className="bg-blue-50 p-4 rounded">
            <h4 className="font-semibold text-blue-800 mb-2">Masculine</h4>
            <div className="mb-2">
              <span className="block text-sm text-gray-500">Singular:</span>
              <div className="flex items-center">
                <span className="font-medium">{adjective.masc_french_singular}</span>
                <button
                  onClick={() => handlePlayAudio(adjective.masc_french_singular)}
                  className="ml-2 text-blue-500 hover:text-blue-700"
                  aria-label="Play pronunciation"
                >
                  <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4" viewBox="0 0 20 20" fill="currentColor">
                    <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM9.555 7.168A1 1 0 008 8v4a1 1 0 001.555.832l3-2a1 1 0 000-1.664l-3-2z" clipRule="evenodd" />
                  </svg>
                </button>
              </div>
            </div>
            <div>
              <span className="block text-sm text-gray-500">Plural:</span>
              <div className="flex items-center">
                <span className="font-medium">{adjective.masc_french_plural}</span>
                <button
                  onClick={() => handlePlayAudio(adjective.masc_french_plural)}
                  className="ml-2 text-blue-500 hover:text-blue-700"
                  aria-label="Play pronunciation"
                >
                  <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4" viewBox="0 0 20 20" fill="currentColor">
                    <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM9.555 7.168A1 1 0 008 8v4a1 1 0 001.555.832l3-2a1 1 0 000-1.664l-3-2z" clipRule="evenodd" />
                  </svg>
                </button>
              </div>
            </div>
          </div>

          <div className="bg-pink-50 p-4 rounded">
            <h4 className="font-semibold text-pink-800 mb-2">Feminine</h4>
            <div className="mb-2">
              <span className="block text-sm text-gray-500">Singular:</span>
              <div className="flex items-center">
                <span className="font-medium">{adjective.fem_french_singular}</span>
                <button
                  onClick={() => handlePlayAudio(adjective.fem_french_singular)}
                  className="ml-2 text-blue-500 hover:text-blue-700"
                  aria-label="Play pronunciation"
                >
                  <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4" viewBox="0 0 20 20" fill="currentColor">
                    <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM9.555 7.168A1 1 0 008 8v4a1 1 0 001.555.832l3-2a1 1 0 000-1.664l-3-2z" clipRule="evenodd" />
                  </svg>
                </button>
              </div>
            </div>
            <div>
              <span className="block text-sm text-gray-500">Plural:</span>
              <div className="flex items-center">
                <span className="font-medium">{adjective.fem_french_plural}</span>
                <button
                  onClick={() => handlePlayAudio(adjective.fem_french_plural)}
                  className="ml-2 text-blue-500 hover:text-blue-700"
                  aria-label="Play pronunciation"
                >
                  <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4" viewBox="0 0 20 20" fill="currentColor">
                    <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM9.555 7.168A1 1 0 008 8v4a1 1 0 001.555.832l3-2a1 1 0 000-1.664l-3-2z" clipRule="evenodd" />
                  </svg>
                </button>
              </div>
            </div>
          </div>
        </div>

        <div className="flex justify-end">
          <button
            onClick={onNext}
            className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
          >
            Next Adjective
          </button>
        </div>
      </div>
    </div>
  );
};

export default AdjectiveCard;