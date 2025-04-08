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
              {/* <span>English First</span> */}
            </>
          ) : (
            <>
              <svg className="w-6 h-4" viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg">
                {/* French Flag */}
                <rect width="170.667" height="512" fill="#002654"/>
                <rect x="170.667" width="170.667" height="512" fill="#FFFFFF"/>
                <rect x="341.333" width="170.667" height="512" fill="#CE1126"/>
              </svg>
              {/* <span>French First</span> */}
            </>
          )}
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
      
      {/* Next Verb Button */}
      <button 
        onClick={onNext}
        className="mt-4 bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600"
      >
        Next Verb
      </button>

      {/* Conjugation Toggle Button */}
      <button 
        onClick={toggleConjugations}
        className="mt-4 bg-purple-500 text-white px-4 py-2 rounded hover:bg-purple-600"
      >
        {showConjugations ? 'Hide Conjugations' : 'Show Conjugations'}
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
              <table className="w-full border-collapse bg-indigo-50">
                <thead>
                  <tr>
                    <th className="border border-indigo-200 p-2 bg-indigo-100 text-left">Person</th>
                    <th className="border border-indigo-200 p-2 bg-indigo-100 text-left">Imperative</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td className="border border-indigo-200 p-2">Tu</td>
                    <td className="border border-indigo-200 p-2">{verb.imperatif_present.tu}</td>
                  </tr>
                  <tr>
                    <td className="border border-indigo-200 p-2">Nous</td>
                    <td className="border border-indigo-200 p-2">{verb.imperatif_present.nous}</td>
                  </tr>
                  <tr>
                    <td className="border border-indigo-200 p-2">Vous</td>
                    <td className="border border-indigo-200 p-2">{verb.imperatif_present.vous}</td>
                  </tr>
                </tbody>
              </table>
            </div>
            
            {/* Participle Section */}
            <div className="mb-6">
              <h3 className="text-xl font-bold mb-2">Participle</h3>
              <table className="w-full border-collapse bg-cyan-50">
                <thead>
                  <tr>
                    <th className="border border-cyan-200 p-2 bg-cyan-100 text-left">Form</th>
                    <th className="border border-cyan-200 p-2 bg-cyan-100 text-left">Participle</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td className="border border-cyan-200 p-2">Present (Présent)</td>
                    <td className="border border-cyan-200 p-2">{verb.participe_present}</td>
                  </tr>
                  <tr>
                    <td className="border border-cyan-200 p-2">Past (Passé)</td>
                    <td className="border border-cyan-200 p-2">{verb.participe_passe}</td>
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
  // Define color scheme based on tense title
  const getTenseColor = (title: string) => {
    const colorMap: { [key: string]: string } = {
      "Present (Présent)": "bg-blue-50 border-blue-200",
      "Imperfect (Imparfait)": "bg-green-50 border-green-200",
      "Future (Futur Simple)": "bg-purple-50 border-purple-200",
      "Past Perfect (Passé Composé)": "bg-amber-50 border-amber-200",
      "Conditional (Conditionnel Présent)": "bg-rose-50 border-rose-200",
      "Subjunctive (Subjonctif Présent)": "bg-teal-50 border-teal-200",
    };
    
    return colorMap[title] || "bg-gray-50 border-gray-200";
  };
  
  const baseColor = getTenseColor(title);
  const headerColor = baseColor.replace("-50", "-100");
  
  return (
    <div className="mb-6">
      <h3 className="text-xl font-bold mb-2">{title}</h3>
      <table className={`w-full border-collapse ${baseColor}`}>
        <thead>
          <tr>
            <th className={`border ${headerColor} p-2 text-left font-semibold`}>Person</th>
            <th className={`border ${headerColor} p-2 text-left font-semibold`}>{title}</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td className={`border ${baseColor} p-2`}>Je</td>
            <td className={`border ${baseColor} p-2`}>{conjugation.je}</td>
          </tr>
          <tr>
            <td className={`border ${baseColor} p-2`}>Tu</td>
            <td className={`border ${baseColor} p-2`}>{conjugation.tu}</td>
          </tr>
          <tr>
            <td className={`border ${baseColor} p-2`}>Il/Elle</td>
            <td className={`border ${baseColor} p-2`}>{conjugation.il_elle}</td>
          </tr>
          <tr>
            <td className={`border ${baseColor} p-2`}>Nous</td>
            <td className={`border ${baseColor} p-2`}>{conjugation.nous}</td>
          </tr>
          <tr>
            <td className={`border ${baseColor} p-2`}>Vous</td>
            <td className={`border ${baseColor} p-2`}>{conjugation.vous}</td>
          </tr>
          <tr>
            <td className={`border ${baseColor} p-2`}>Ils/Elles</td>
            <td className={`border ${baseColor} p-2`}>{conjugation.ils_elles}</td>
          </tr>
        </tbody>
      </table>
    </div>
  );
};

export default VerbCard;