import { useState, useEffect } from 'react';
import { getRandomVerb, FrenchVerb } from '../services/api';
import VerbCard from '../components/VerbCard';
import VerbForm from '../components/VerbForm';
import VerbSearch from '../components/VerbSearch';
import { 
  Container, 
  Title, 
  Box, 
  Paper, 
  Grid, 
  Flex, 
  Text, 
  Button, 
  Center, 
  Stack, 
  Loader, 
  Alert 
} from '@mantine/core';

const VerbsPage = () => {
  const [verb, setVerb] = useState<FrenchVerb | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const fetchRandomVerb = async () => {
    setLoading(true);
    setError(null);
    try {
      const data = await getRandomVerb();
      setVerb(data);
    } catch (err) {
      console.error('Error fetching verb:', err);
      setError('Failed to load verb. Please try again.');
      setVerb(null);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchRandomVerb();
  }, []);

  const handleNext = () => {
    fetchRandomVerb();
  };

  const handleVerbCreated = () => {
    // Fetch a new verb after creation
    fetchRandomVerb();
  };

  const handleVerbFound = (foundVerb: FrenchVerb) => {
    setVerb(foundVerb);
  };

  return (
    <Container size="md" py="xl">
      <Title order={1} ta="center" mb="lg">French Verb Conjugations</Title>

      {/* Search bar for verbs */}
      <Paper bg="blue.9" p="md" mb="lg" shadow="md" radius="md">
        <Center>
          <VerbSearch onVerbFound={handleVerbFound} />
        </Center>
      </Paper>

      <Grid mb="lg">
        <Grid.Col>
          <Title order={3} mb="xs">Add a New Verb</Title>
          <VerbForm onVerbCreated={handleVerbCreated} />
        </Grid.Col>
      </Grid>

      <Box mt="xl">
        <Flex justify="space-between" align="center" mb="md">
          <Title order={2}>Verb Details</Title>
          {/* TODO: I don't think this is needed since next verb button already does this */}
          {/* <Button onClick={fetchRandomVerb}>
            Load Random Verb
          </Button> */}
        </Flex>

        {loading ? (
          <Center py="xl">
            <Stack align="center">
              <Loader size="lg" />
              <Text mt="md">Loading verb...</Text>
            </Stack>
          </Center>
        ) : error ? (
          <Center py="xl">
            <Stack align="center">
              <Alert color="red" title="Error" variant="filled">
                {error}
              </Alert>
              <Button 
                onClick={fetchRandomVerb}
                mt="md"
              >
                Try Again
              </Button>
            </Stack>
          </Center>
        ) : verb ? (
          <VerbCard verb={verb} onNext={handleNext} />
        ) : (
          <Center py="xl">
            <Text>No verbs available. Please add some verbs using the form above.</Text>
          </Center>
        )}
      </Box>
    </Container>
  );
};

export default VerbsPage;
