import { useState, useEffect } from 'react';
import { getRandomAdjective, FrenchAdjective } from '../services/api';
import AdjectiveForm from '../components/AdjectiveForm';
import AdjectiveSearch from '../components/AdjectiveSearch';
import AdjectiveCard from '../components/AdjectiveCard';
import { 
  Container, 
  Title, 
  Box, 
  Group, 
  Grid, 
  Flex, 
  Text, 
  Button, 
  Center, 
  Stack, 
  Loader, 
  Alert 
} from '@mantine/core';

const AdjectivesPage = () => {
  const [adjective, setAdjective] = useState<FrenchAdjective | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const fetchRandomAdjective = async () => {
    setLoading(true);
    setError(null);
    try {
      const data = await getRandomAdjective();
      setAdjective(data);
    } catch (err) {
      console.error('Error fetching adjective:', err);
      setError('Failed to load adjective. Please try again.');
      setAdjective(null);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchRandomAdjective();
  }, []);

  const handleNext = () => {
    fetchRandomAdjective();
  };

  const handleAdjectiveCreated = (newAdjective: FrenchAdjective) => {
    setAdjective(newAdjective);
  };

  const handleAdjectiveFound = (foundAdjective: FrenchAdjective) => {
    setAdjective(foundAdjective);
  };

  return (
    <Container size="md" py="xl">
      <Title order={1} ta="center" mb="lg">French Adjectives</Title>

      {/* Search and Random section */}
      <Group justify="center" mb="lg">
        <AdjectiveSearch onAdjectiveFound={handleAdjectiveFound} />
        <Button 
          onClick={fetchRandomAdjective}
          color="grape"
          radius="md"
        >
          Random Adjective
        </Button>
      </Group>

      <Grid mb="lg">
        <Grid.Col>
          <Title order={3} mb="xs">Add a New Adjective</Title>
          <AdjectiveForm onAdjectiveCreated={handleAdjectiveCreated} />
        </Grid.Col>
      </Grid>

      <Box mt="xl">
        <Flex justify="space-between" align="center" mb="md">
          <Title order={2}>Adjective Details</Title>
        </Flex>

        {loading ? (
          <Center py="xl">
            <Stack align="center">
              <Loader size="lg" />
              <Text mt="md">Loading adjective...</Text>
            </Stack>
          </Center>
        ) : error ? (
          <Center py="xl">
            <Stack align="center">
              <Alert color="red" title="Error" variant="filled">
                {error}
              </Alert>
              <Button 
                onClick={fetchRandomAdjective}
                mt="md"
              >
                Try Again
              </Button>
            </Stack>
          </Center>
        ) : adjective ? (
          <AdjectiveCard adjective={adjective} onNext={handleNext} />
        ) : (
          <Center py="xl">
            <Text>No adjectives available. Please add some adjectives using the form above.</Text>
          </Center>
        )}
      </Box>
    </Container>
  );
};

export default AdjectivesPage;
