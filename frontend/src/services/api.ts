import axios from 'axios';

// Define the base API URL
const API_URL = 'http://localhost:8000';

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

// API functions
export const getRandomFlashcard = async (): Promise<Flashcard> => {
  try {
    const response = await api.get('/flashcards/random');
    console.log(response.data)
    return response.data.flashcard;
  } catch (error) {
    console.error('Error fetching random flashcard:', error);
    throw error;
  }
};

export const createFlashcard = async (flashcard: Omit<Flashcard, 'id'>): Promise<Flashcard> => {
  try {
    const formData = new FormData();
    formData.append('question', flashcard.question);
    formData.append('answer', flashcard.answer);
    
    const response = await api.post('/create_flashcard', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });
    return response.data;
  } catch (error) {
    console.error('Error creating flashcard:', error);
    throw error;
  }
};

export const getRandomVerb = async (): Promise<FrenchVerb> => {
  try {
    const response = await api.get('/verbs/flashcards');
    console.log(response.data.verb);
    return response.data.verb;
  } catch (error) {
    console.error('Error fetching random verb:', error);
    throw error;
  }
};

export const getVerbById = async (id: number): Promise<FrenchVerb> => {
  try {
    const response = await api.get(`/verbs/flashcards/${id}`);
    return response.data.verb;
  } catch (error) {
    console.error(`Error fetching verb with id ${id}:`, error);
    throw error;
  }
};

export const createVerb = async (verb: string): Promise<FrenchVerb> => {
  try {
    const response = await api.post('/verbs/', null, {
      params: { verb },
    });
    return response.data;
  } catch (error) {
    console.error('Error creating verb:', error);
    throw error;
  }
};

export const playAudio = async (text: string, lang: string = 'fr-FR'): Promise<void> => {
  try {
    await api.get('/api/speak', {
      params: {
        text,
        lang,
      },
    });
  } catch (error) {
    console.error('Error playing audio:', error);
    throw error;
  }
};

export default api;