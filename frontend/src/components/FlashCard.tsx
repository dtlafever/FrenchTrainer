import { useState } from 'react';
import { Flashcard } from '../services/api';
import { playAudio } from '../services/api';
import { Card, Text, Button, Flex, ActionIcon, Box, Stack } from '@mantine/core';
// import { useDisclosure } from '@mantine/hooks';

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
    <Flex direction="column" align="center">
      <Box
        className={`flip-card ${isFlipped ? 'flipped' : ''}`}
        onClick={handleFlip}
        style={{ position: 'relative' }}
      >
        {/* Audio Button */}
        <ActionIcon 
          variant="filled" 
          color="blue" 
          radius="md"
          onClick={handlePlayAudio}
          style={{ position: 'absolute', top: '8px', right: '8px', zIndex: 10 }}
        >
          🔊
        </ActionIcon>

        <div className="flip-card-inner">
          <Card className="flip-card-front" shadow="sm" padding="lg" radius="md" withBorder>
            <Text size="xl" ta="center">{flashcard.question}</Text>
          </Card>

          <Card className="flip-card-back" shadow="sm" padding="lg" radius="md" withBorder>
            <Stack align="center" gap="xs">
              <Text size="xl">{flashcard.question}</Text>
              <Text size="xl" fw={600}>{flashcard.answer}</Text>
            </Stack>
          </Card>
        </div>
      </Box>

      <Button 
        onClick={onNext}
        color="green"
        size="md"
        radius="md"
        mt="md"
      >
        Next Flashcard
      </Button>
    </Flex>
  );
};

export default FlashCard;
