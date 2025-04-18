import { FrenchAdjective, playAudio } from '../services/api';
import { Card, Title, Text, Button, Grid, Group, Box, ActionIcon, Flex, Paper } from '@mantine/core';

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

  // Audio icon component for reuse
  const AudioIcon = () => (
    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 20 20" fill="currentColor">
      <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM9.555 7.168A1 1 0 008 8v4a1 1 0 001.555.832l3-2a1 1 0 000-1.664l-3-2z" clipRule="evenodd" />
    </svg>
  );

  return (
    <Card shadow="md" radius="md" withBorder p="lg">
      <Card.Section p="md">
        <Group mb="md">
          <Title order={3}>{adjective.masc_french_singular}</Title>
          <ActionIcon 
            variant="subtle" 
            color="blue" 
            onClick={() => handlePlayAudio(adjective.masc_french_singular)}
            aria-label="Play pronunciation"
          >
            <AudioIcon />
          </ActionIcon>
        </Group>
        <Text c="dimmed" fs="italic" mb="lg">{adjective.english_text}</Text>
      </Card.Section>

      <Grid mb="md">
        <Grid.Col span={6}>
          <Paper p="md" radius="md" bg="blue.0">
            <Text fw={600} c="blue.8" mb="sm">Masculine</Text>

            <Box mb="sm">
              <Text size="sm" c="dimmed">Singular:</Text>
              <Flex align="center" gap="xs">
                <Text fw={500}>{adjective.masc_french_singular}</Text>
                <ActionIcon 
                  size="sm" 
                  variant="subtle" 
                  color="blue" 
                  onClick={() => handlePlayAudio(adjective.masc_french_singular)}
                  aria-label="Play pronunciation"
                >
                  <AudioIcon />
                </ActionIcon>
              </Flex>
            </Box>

            <Box>
              <Text size="sm" c="dimmed">Plural:</Text>
              <Flex align="center" gap="xs">
                <Text fw={500}>{adjective.masc_french_plural}</Text>
                <ActionIcon 
                  size="sm" 
                  variant="subtle" 
                  color="blue" 
                  onClick={() => handlePlayAudio(adjective.masc_french_plural)}
                  aria-label="Play pronunciation"
                >
                  <AudioIcon />
                </ActionIcon>
              </Flex>
            </Box>
          </Paper>
        </Grid.Col>

        <Grid.Col span={6}>
          <Paper p="md" radius="md" bg="pink.0">
            <Text fw={600} c="pink.8" mb="sm">Feminine</Text>

            <Box mb="sm">
              <Text size="sm" c="dimmed">Singular:</Text>
              <Flex align="center" gap="xs">
                <Text fw={500}>{adjective.fem_french_singular}</Text>
                <ActionIcon 
                  size="sm" 
                  variant="subtle" 
                  color="blue" 
                  onClick={() => handlePlayAudio(adjective.fem_french_singular)}
                  aria-label="Play pronunciation"
                >
                  <AudioIcon />
                </ActionIcon>
              </Flex>
            </Box>

            <Box>
              <Text size="sm" c="dimmed">Plural:</Text>
              <Flex align="center" gap="xs">
                <Text fw={500}>{adjective.fem_french_plural}</Text>
                <ActionIcon 
                  size="sm" 
                  variant="subtle" 
                  color="blue" 
                  onClick={() => handlePlayAudio(adjective.fem_french_plural)}
                  aria-label="Play pronunciation"
                >
                  <AudioIcon />
                </ActionIcon>
              </Flex>
            </Box>
          </Paper>
        </Grid.Col>
      </Grid>

      <Group justify="flex-end">
        <Button
          onClick={onNext}
          color="blue"
          radius="md"
        >
          Next Adjective
        </Button>
      </Group>
    </Card>
  );
};

export default AdjectiveCard;
