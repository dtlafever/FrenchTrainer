import { useState } from 'react';
import { FrenchVerb, playAudio } from '../services/api';

interface VerbCardProps {
  verb: FrenchVerb;
  onNext: () => void;
}

const VerbCard: React.FC<VerbCardProps> = ({ verb, onNext }) => {
  const [isFlipped, setIsFlipped] = useState(false);
  const [showEnglishFirst, setShowEnglishFirst] = useState(false);
  const [showConjugations, setShowConjugations] = useState(false);

  const handleFlip = () => {
    setIsFlipped(!isFlipped);
  };

  const toggleLanguage = () => {
    setShowEnglishFirst(!showEnglishFirst);
    setIsFlipped(false); // Reset the card to non-flipped state
  };

  const toggleConjugations = () => {
    setShowConjugations(!showConjugations);
  };

  const handlePlayAudio = (e: React.MouseEvent) => {
    e.stopPropagation();
    // Play audio for the front text, whether it's French or English
    const text = showEnglishFirst ? verb.english_text : verb.infinitif;
    const lang = showEnglishFirst ? 'en-US' : 'fr-FR';
    playAudio(text, lang);
  };

  // Content for front and back of card
  const frontText = showEnglishFirst ? verb.english_text : verb.infinitif;
  const backTitle = showEnglishFirst ? verb.english_text : verb.infinitif;
  const backTranslation = showEnglishFirst ? verb.infinitif : verb.english_text;

  return (
    <div className="flex flex-col items-center">
      {/* Display options */}
      <div className="mb-6 flex justify-center gap-4">
        <button 
          onClick={toggleLanguage}
          className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
        >
          {showEnglishFirst ? 'Show French First' : 'Show English First'}
        </button>
      </div>

      {/* Verb Flashcard */}
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
      
      {/* Conjugation Toggle Button */}
      <button 
        onClick={toggleConjugations}
        className="mt-4 bg-purple-500 text-white px-4 py-2 rounded hover:bg-purple-600"
      >
        {showConjugations ? 'Hide Conjugations' : 'Show Conjugations'}
      </button>
      
      {/* Next Verb Button */}
      <button 
        onClick={onNext}
        className="mt-4 bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600"
      >
        Next Verb
      </button>

      {/* Conjugation Details */}
      {showConjugations && (
        <div className="mt-8 bg-white rounded shadow p-6 w-full max-w-4xl">
          <h2 className="text-2xl font-bold mb-4">
            {verb.infinitif} ({verb.english_text})
          </h2>
          <p className="mb-4">Group: {verb.groupe} | Auxiliary: {verb.auxiliaire}</p>
          
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {/* Present Tenses */}
            <ConjugationTable
              title="Present (Présent)"
              conjugation={verb.indicatif_present}
            />
            
            {/* Imperfect Tense */}
            <ConjugationTable
              title="Imperfect (Imparfait)"
              conjugation={verb.indicatif_imparfait}
            />
            
            {/* Future Simple */}
            <ConjugationTable
              title="Future (Futur Simple)"
              conjugation={verb.indicatif_futur_simple}
            />
            
            {/* Passé Composé */}
            <ConjugationTable
              title="Past Perfect (Passé Composé)"
              conjugation={verb.indicatif_passe_compose}
            />
            
            {/* Conditional Present */}
            <ConjugationTable
              title="Conditional (Conditionnel Présent)"
              conjugation={verb.conditionnel_present}
            />
            
            {/* Subjunctive Present */}
            <ConjugationTable
              title="Subjunctive (Subjonctif Présent)"
              conjugation={verb.subjonctif_present}
            />
            
            {/* Imperative Present */}
            <div className="mb-6">
              <h3 className="text-xl font-bold mb-2">Imperative (Impératif)</h3>
              <table className="w-full border-collapse">
                <thead>
                  <tr>
                    <th className="border border-gray-200 p-2 bg-gray-50 text-left">Person</th>
                    <th className="border border-gray-200 p-2 bg-gray-50 text-left">Imperative</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td className="border border-gray-200 p-2">Tu</td>
                    <td className="border border-gray-200 p-2">{verb.imperatif_present.tu}</td>
                  </tr>
                  <tr>
                    <td className="border border-gray-200 p-2">Nous</td>
                    <td className="border border-gray-200 p-2">{verb.imperatif_present.nous}</td>
                  </tr>
                  <tr>
                    <td className="border border-gray-200 p-2">Vous</td>
                    <td className="border border-gray-200 p-2">{verb.imperatif_present.vous}</td>
                  </tr>
                </tbody>
              </table>
            </div>
            
            {/* Participle Section */}
            <div className="mb-6">
              <h3 className="text-xl font-bold mb-2">Participle</h3>
              <table className="w-full border-collapse">
                <thead>
                  <tr>
                    <th className="border border-gray-200 p-2 bg-gray-50 text-left">Form</th>
                    <th className="border border-gray-200 p-2 bg-gray-50 text-left">Participle</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td className="border border-gray-200 p-2">Present (Présent)</td>
                    <td className="border border-gray-200 p-2">{verb.participe_present}</td>
                  </tr>
                  <tr>
                    <td className="border border-gray-200 p-2">Past (Passé)</td>
                    <td className="border border-gray-200 p-2">{verb.participe_passe}</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

// Helper component for conjugation tables
interface ConjugationTableProps {
  title: string;
  conjugation: {
    je: string;
    tu: string;
    il_elle: string;
    nous: string;
    vous: string;
    ils_elles: string;
  };
}

const ConjugationTable: React.FC<ConjugationTableProps> = ({ title, conjugation }) => {
  return (
    <div className="mb-6">
      <h3 className="text-xl font-bold mb-2">{title}</h3>
      <table className="w-full border-collapse">
        <thead>
          <tr>
            <th className="border border-gray-200 p-2 bg-gray-50 text-left">Person</th>
            <th className="border border-gray-200 p-2 bg-gray-50 text-left">{title}</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td className="border border-gray-200 p-2">Je</td>
            <td className="border border-gray-200 p-2">{conjugation.je}</td>
          </tr>
          <tr>
            <td className="border border-gray-200 p-2">Tu</td>
            <td className="border border-gray-200 p-2">{conjugation.tu}</td>
          </tr>
          <tr>
            <td className="border border-gray-200 p-2">Il/Elle</td>
            <td className="border border-gray-200 p-2">{conjugation.il_elle}</td>
          </tr>
          <tr>
            <td className="border border-gray-200 p-2">Nous</td>
            <td className="border border-gray-200 p-2">{conjugation.nous}</td>
          </tr>
          <tr>
            <td className="border border-gray-200 p-2">Vous</td>
            <td className="border border-gray-200 p-2">{conjugation.vous}</td>
          </tr>
          <tr>
            <td className="border border-gray-200 p-2">Ils/Elles</td>
            <td className="border border-gray-200 p-2">{conjugation.ils_elles}</td>
          </tr>
        </tbody>
      </table>
    </div>
  );
};

export default VerbCard;