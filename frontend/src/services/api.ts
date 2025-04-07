import axios from 'axios';
import { EdgeTTSClient, ProsodyOptions, OUTPUT_FORMAT } from 'edge-tts-client';
import { Buffer } from 'buffer';

// // TypeScript declaration for AudioContext
// interface AudioContextWindow extends Window {
//   AudioContext: typeof AudioContext;
//   webkitAudioContext: typeof AudioContext;
// }

// Define the base API URL
const API_URL = import.meta.env.PROD ? '/api' : 'http://localhost:8000';

// Create an axios instance
const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Type definitions for our API responses
export interface Flashcard {
  id: number;
  question: string;
  answer: string;
}

export interface Conjugation {
  je: string;
  tu: string;
  il_elle: string;
  nous: string;
  vous: string;
  ils_elles: string;
}

export interface ImperativeConjugation {
  tu: string;
  nous: string;
  vous: string;
}

export interface FrenchVerb {
  id: number;
  english_text: string;
  infinitif: string;
  groupe: number;
  auxiliaire: string;
  participe_present: string;
  participe_passe: string;
  
  // Verb conjugations
  indicatif_present: Conjugation;
  indicatif_imparfait: Conjugation;
  indicatif_passe_simple: Conjugation;
  indicatif_futur_simple: Conjugation;
  conditionnel_present: Conjugation;
  subjonctif_present: Conjugation;
  subjonctif_imparfait: Conjugation;
  imperatif_present: ImperativeConjugation;
  indicatif_passe_compose: Conjugation;
  indicatif_plus_que_parfait: Conjugation;
  indicatif_passe_anterieur: Conjugation;
  indicatif_futur_anterieur: Conjugation;
  conditionnel_passe: Conjugation;
  subjonctif_passe: Conjugation;
  subjonctif_plus_que_parfait: Conjugation;
  imperatif_passe: ImperativeConjugation;
}

// ==========
// FlashCards
// ==========
export const getRandomFlashcard = async (): Promise<Flashcard> => {
  try {
    const response = await api.get('/flashcards/random');
    return response.data;
  } catch (error) {
    console.error('Error fetching random flashcard:', error);
    throw error;
  }
};

export const createFlashcard = async (flashcard: Omit<Flashcard, 'id'>): Promise<Flashcard> => {
  try {    
    const response = await api.post('/flashcards/', {
      question: flashcard.question,
      answer: flashcard.answer
    });
    return response.data;
  } catch (error) {
    console.error('Error creating flashcard:', error);
    throw error;
  }
};

// ==========
// Verbs
// ==========

export const getRandomVerb = async (): Promise<FrenchVerb> => {
  try {
    const response = await api.get('/verbs/random');
    return response.data;
  } catch (error) {
    console.error('Error fetching random verb:', error);
    throw error;
  }
};

export const getVerbById = async (id: number): Promise<FrenchVerb> => {
  try {
    const response = await api.get(`/verbs/${id}`);
    return response.data;
  } catch (error) {
    console.error(`Error fetching verb with id ${id}:`, error);
    throw error;
  }
};

export const createVerb = async (verb: string): Promise<FrenchVerb> => {
  try {
    // Null body and verb as query parameter
    const response = await api.post('/verbs/', null, {
      params: {
        verb: verb
      }
    });
    return response.data;
  } catch (error) {
    console.error('Error creating verb:', error);
    throw error;
  }
};

export const searchVerb = async (verb: string): Promise<FrenchVerb> => {
  try {
    const response = await api.get('/verbs/search', {
      params: {
        verb: verb
      }
    });
    return response.data;
  } catch (error) {
    console.error('Error searching for verb:', error);
    throw error;
  }
};

// ==========
// Miscellaneous
// ==========

export const playAudio = async (text: string, lang: string = 'fr-FR'): Promise<void> => {
  try {
    // Choose voice based on language
    let voice = 'fr-FR-VivienneMultilingualNeural'; // Default French voice
    
    if (lang === 'en-US') {
      voice = 'en-US-SteffanNeural';
    }
    
    const ttsClient = new EdgeTTSClient();

    await ttsClient.setMetadata(voice, OUTPUT_FORMAT.AUDIO_24KHZ_48KBITRATE_MONO_MP3);

    // Define SSML options
    const options = new ProsodyOptions();
    options.pitch = 'medium';
    options.rate = 1.0;
    options.volume = 90;

    // Get the audio emitter
    const emitter = ttsClient.toStream(text, options);
    
    // Initialize the audio context
    // const windowWithAudioContext = window as unknown as AudioContextWindow;
    // const audioContext = new (windowWithAudioContext.AudioContext || windowWithAudioContext.webkitAudioContext)();
    
    // Collect audio chunks
    const chunks: Buffer[] = [];
    
    return new Promise((resolve, reject) => {
      // Listen for data events
      emitter.on('data', (data: Buffer) => {
        chunks.push(data);
      });
      
      // Handle errors
      emitter.on('close', () => {
        reject(new Error('Connection closed before audio was complete'));
      });
      
      // Process and play audio when finished
      emitter.on('end', async () => {
        try {
          // Concatenate all chunks
          const totalLength = chunks.reduce((acc, chunk) => acc + chunk.length, 0);
          const audioData = new Uint8Array(totalLength);
          let offset = 0;
          
          for (const chunk of chunks) {
            audioData.set(new Uint8Array(chunk), offset);
            offset += chunk.length;
          }
          
          // Create a temporary audio element for playback
          const audioBlob = new Blob([audioData], { type: 'audio/mp3' });
          const audioUrl = URL.createObjectURL(audioBlob);
          const audio = new Audio(audioUrl);
          
          // Clean up when done
          audio.onended = () => {
            URL.revokeObjectURL(audioUrl);
            resolve();
          };
          
          // Start playback
          audio.play();
        } catch (err) {
          reject(err);
        }
      });
    });
  } catch (error) {
    console.error('Error playing audio:', error);
    throw error;
  }
};

export default api;