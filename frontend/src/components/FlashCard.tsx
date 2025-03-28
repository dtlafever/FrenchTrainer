import { useState } from 'react';
import { Flashcard } from '../services/api';
import { playAudio } from '../services/api';

interface FlashCardProps {
  flashcard: Flashcard;
  onNext: () => void;
}

const FlashCard: React.FC<FlashCardProps> = ({ flashcard, onNext }) => {
  const [isFlipped, setIsFlipped] = useState(false);

  const handleFlip = () => {
    setIsFlipped(!isFlipped);
  };

  const handlePlayAudio = (e: React.MouseEvent) => {
    e.stopPropagation();
    playAudio(flashcard.question);
  };

  return (
    <div className="flex flex-col items-center">
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
            <p className="text-xl">{flashcard.question}</p>
          </div>
          <div className="flip-card-back bg-white">
            <div className="text-center">
              <p className="text-xl mb-1">{flashcard.question}</p>
              <p className="text-xl font-semibold">{flashcard.answer}</p>
            </div>
          </div>
        </div>
      </div>
      
      <button 
        onClick={onNext}
        className="mt-4 bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600"
      >
        Next Flashcard
      </button>
    </div>
  );
};

export default FlashCard;