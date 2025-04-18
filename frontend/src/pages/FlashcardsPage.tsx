import { useState, useEffect } from 'react';
import { getRandomFlashcard, Flashcard } from '../services/api';
import FlashcardComponent from '../components/FlashCard';
import FlashcardForm from '../components/FlashcardForm';
import { Container, Title, Loader, Text, Button, Center, Stack, Alert } from '@mantine/core';

const FlashcardsPage = () => {
  const [flashcard, setFlashcard] = useState<Flashcard | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const fetchRandomFlashcard = async () => {
    setLoading(true);
    setError(null);
    try {
      const data = await getRandomFlashcard();
      setFlashcard(data);
    } catch (err) {
      console.error('Error fetching flashcard:', err);
      setError('Failed to load flashcard. Please try again.');
      setFlashcard(null);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchRandomFlashcard();
  }, []);

  const handleNext = () => {
    fetchRandomFlashcard();
  };

  const handleFlashcardCreated = () => {
    // Fetch a new flashcard after creation
    fetchRandomFlashcard();
  };

  return (
    <Container size="md" py="xl">
      <Title order={1} ta="center" mb="lg">French Flashcards</Title>

      <FlashcardForm onFlashcardCreated={handleFlashcardCreated} />

      {loading ? (
        <Center py="xl">
          <Stack align="center">
            <Loader size="lg" />
            <Text mt="md">Loading flashcard...</Text>
          </Stack>
        </Center>
      ) : error ? (
        <Center py="xl">
          <Stack align="center">
            <Alert color="red" title="Error" variant="filled">
              {error}
            </Alert>
            <Button 
              onClick={fetchRandomFlashcard}
              mt="md"
            >
              Try Again
            </Button>
          </Stack>
        </Center>
      ) : flashcard ? (
        <FlashcardComponent flashcard={flashcard} onNext={handleNext} />
      ) : (
        <Center py="xl">
          <Text>No flashcards available. Please add some flashcards using the form above.</Text>
        </Center>
      )}
    </Container>
  );
};

export default FlashcardsPage;
