import { useState } from 'react';
import { FrenchAdjective, playAudio } from '../services/api';

interface AdjectiveCardProps {
  adjective: FrenchAdjective;
  onNext: () => void;
}

const AdjectiveCard: React.FC<AdjectiveCardProps> = ({ adjective, onNext }) => {
  const [isFlipped, setIsFlipped] = useState(false);
  const [showEnglishFirst, setShowEnglishFirst] = useState(false);
  const [showForms, setShowForms] = useState(false);

  const handleFlip = () => {
    setIsFlipped(!isFlipped);
  };

  const toggleLanguage = () => {
    setShowEnglishFirst(!showEnglishFirst);
    setIsFlipped(false); // Reset the card to non-flipped state
  };

  const toggleForms = () => {
    setShowForms(!showForms);
  };

  const handlePlayAudio = (e: React.MouseEvent, text: string = '', lang: string = '') => {
    e.stopPropagation();
    // If no specific text is provided, use the front text
    if (!text) {
      text = showEnglishFirst ? adjective.english_text : adjective.french_masculine;
      lang = showEnglishFirst ? 'en-US' : 'fr-FR';
    }
    playAudio(text, lang);
  };

  // Content for front and back of card
  const frontText = showEnglishFirst ? adjective.english_text : adjective.french_masculine;
  const backTitle = showEnglishFirst ? adjective.english_text : adjective.french_masculine;
  const backTranslation = showEnglishFirst ? adjective.french_masculine : adjective.english_text;

  return (
    <div className="flex flex-col items-center">
      {/* Display options with flag icons */}
      <div className="mb-6 flex justify-center">
        <button 
          onClick={toggleLanguage}
          className="bg-blue-500 text-white px-3 py-2 rounded hover:bg-blue-600 flex items-center gap-2"
          title={showEnglishFirst ? "Switch to French first" : "Switch to English first"}
        >
          {showEnglishFirst ? (
            <>
              <svg className="w-6 h-4" viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg">
                {/* UK Flag */}
                <rect width="512" height="512" fill="#012169"/>
                <path d="M0 0 L512 512 M512 0 L0 512" stroke="#fff" strokeWidth="36"/>
                <path d="M256 0 V512 M0 256 H512" stroke="#fff" strokeWidth="60"/>
                <path d="M0 0 L512 512 M512 0 L0 512" stroke="#C8102E" strokeWidth="24"/>
                <path d="M256 0 V512 M0 256 H512" stroke="#C8102E" strokeWidth="36"/>
              </svg>
            </>
          ) : (
            <>
              <svg className="w-6 h-4" viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg">
                {/* French Flag */}
                <rect width="170.667" height="512" fill="#002654"/>
                <rect x="170.667" width="170.667" height="512" fill="#FFFFFF"/>
                <rect x="341.333" width="170.667" height="512" fill="#CE1126"/>
              </svg>
            </>
          )}
        </button>
      </div>

      {/* Adjective Flashcard */}
      <div 
        className={`flip-card bg-white rounded shadow ${isFlipped ? 'flipped' : ''}`} 
        onClick={handleFlip}
      >
        {/* Audio Button */}
        <div className="absolute top-2 right-2 z-10">
          <button 
            onClick={handlePlayAudio}
            className="bg-blue-500 hover:bg-blue-600 text-white p-2 rounded"
          >
            🔊
          </button>
        </div>
        
        <div className="flip-card-inner">
          <div className="flip-card-front bg-white">
            <p className="text-xl">{frontText}</p>
          </div>
          <div className="flip-card-back bg-white">
            <div className="text-center">
              <p className="text-xl mb-1">{backTitle}</p>
              <p className="text-xl font-semibold">{backTranslation}</p>
            </div>
          </div>
        </div>
      </div>
      
      {/* Next Adjective Button */}
      <button 
        onClick={onNext}
        className="mt-4 bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600"
      >
        Next Adjective
      </button>

      {/* Forms Toggle Button */}
      <button 
        onClick={toggleForms}
        className="mt-4 bg-purple-500 text-white px-4 py-2 rounded hover:bg-purple-600"
      >
        {showForms ? 'Hide Forms' : 'Show All Forms'}
      </button>

      {/* Adjective Forms Detail */}
      {showForms && (
        <div className="mt-8 bg-white rounded shadow p-6 w-full max-w-4xl">
          <h2 className="text-2xl font-bold mb-4">
            {adjective.french_masculine} ({adjective.english_text})
          </h2>
          
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {/* Forms Table */}
            <div className="col-span-2">
              <h3 className="text-xl font-bold mb-2">Adjective Forms</h3>
              <table className="w-full border-collapse bg-indigo-50">
                <thead>
                  <tr>
                    <th className="border border-indigo-200 p-2 bg-indigo-100 text-left">Form</th>
                    <th className="border border-indigo-200 p-2 bg-indigo-100 text-left">French</th>
                    <th className="border border-indigo-200 p-2 bg-indigo-100 text-left">Audio</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td className="border border-indigo-200 p-2 font-medium">Masculine Singular</td>
                    <td className="border border-indigo-200 p-2">{adjective.french_masculine}</td>
                    <td className="border border-indigo-200 p-2 text-center">
                      <button 
                        onClick={(e) => handlePlayAudio(e, adjective.french_masculine, 'fr-FR')}
                        className="text-blue-500 hover:text-blue-700"
                      >
                        🔊
                      </button>
                    </td>
                  </tr>
                  <tr>
                    <td className="border border-indigo-200 p-2 font-medium">Feminine Singular</td>
                    <td className="border border-indigo-200 p-2">{adjective.french_feminine}</td>
                    <td className="border border-indigo-200 p-2 text-center">
                      <button 
                        onClick={(e) => handlePlayAudio(e, adjective.french_feminine, 'fr-FR')}
                        className="text-blue-500 hover:text-blue-700"
                      >
                        🔊
                      </button>
                    </td>
                  </tr>
                  <tr>
                    <td className="border border-indigo-200 p-2 font-medium">Masculine Plural</td>
                    <td className="border border-indigo-200 p-2">{adjective.french_masculine_plural}</td>
                    <td className="border border-indigo-200 p-2 text-center">
                      <button 
                        onClick={(e) => handlePlayAudio(e, adjective.french_masculine_plural, 'fr-FR')}
                        className="text-blue-500 hover:text-blue-700"
                      >
                        🔊
                      </button>
                    </td>
                  </tr>
                  <tr>
                    <td className="border border-indigo-200 p-2 font-medium">Feminine Plural</td>
                    <td className="border border-indigo-200 p-2">{adjective.french_feminine_plural}</td>
                    <td className="border border-indigo-200 p-2 text-center">
                      <button 
                        onClick={(e) => handlePlayAudio(e, adjective.french_feminine_plural, 'fr-FR')}
                        className="text-blue-500 hover:text-blue-700"
                      >
                        🔊
                      </button>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>

            {/* Usage Examples Section */}
            <div className="col-span-2">
              <h3 className="text-xl font-bold mb-2">Usage Examples</h3>
              <div className="bg-yellow-50 p-4 rounded border border-yellow-200">
                <p className="mb-2">
                  <span className="font-medium">Masculine:</span> Un <span className="text-blue-600">{adjective.french_masculine}</span> garçon
                </p>
                <p className="mb-2">
                  <span className="font-medium">Feminine:</span> Une <span className="text-blue-600">{adjective.french_feminine}</span> fille
                </p>
                <p className="mb-2">
                  <span className="font-medium">Masculine Plural:</span> Des <span className="text-blue-600">{adjective.french_masculine_plural}</span> garçons
                </p>
                <p>
                  <span className="font-medium">Feminine Plural:</span> Des <span className="text-blue-600">{adjective.french_feminine_plural}</span> filles
                </p>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default AdjectiveCard;
