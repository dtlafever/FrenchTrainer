import { useState } from 'react';
import { FrenchVerb, playAudio } from '../services/api';
import {
  Button, 
  Card, 
  Text, 
  Box, 
  Stack, 
  Title, 
  Group, 
  ActionIcon, 
  Table, 
  Paper,
  Grid
} from '@mantine/core';

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
    <Stack align="center" gap="md">
      {/* Display options with flag icons */}
      <Group mb="md" justify="center">
        <Button 
          onClick={toggleLanguage}
          leftSection={showEnglishFirst ? (
            <svg width="24" height="16" viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg">
              {/* UK Flag */}
              <rect width="512" height="512" fill="#012169"/>
              <path d="M0 0 L512 512 M512 0 L0 512" stroke="#fff" strokeWidth="36"/>
              <path d="M256 0 V512 M0 256 H512" stroke="#fff" strokeWidth="60"/>
              <path d="M0 0 L512 512 M512 0 L0 512" stroke="#C8102E" strokeWidth="24"/>
              <path d="M256 0 V512 M0 256 H512" stroke="#C8102E" strokeWidth="36"/>
            </svg>
          ) : (
            <svg width="24" height="16" viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg">
              {/* French Flag */}
              <rect width="170.667" height="512" fill="#002654"/>
              <rect x="170.667" width="170.667" height="512" fill="#FFFFFF"/>
              <rect x="341.333" width="170.667" height="512" fill="#CE1126"/>
            </svg>
          )}
          title={showEnglishFirst ? "Switch to French first" : "Switch to English first"}
          radius="md"
        >
          {showEnglishFirst ? "English First" : "French First"}
        </Button>
      </Group>

      {/* Verb Flashcard */}
      <Box 
        className={`flip-card ${isFlipped ? 'flipped' : ''}`} 
        onClick={handleFlip}
        style={{ position: 'relative', cursor: 'pointer' }}
      >
        {/* Audio Button */}
        <ActionIcon 
          onClick={handlePlayAudio}
          color="blue"
          variant="filled"
          radius="md"
          size="lg"
          style={{ position: 'absolute', top: '8px', right: '8px', zIndex: 10 }}
        >
          🔊
        </ActionIcon>

        <div className="flip-card-inner">
          <Card className="flip-card-front" shadow="sm" p="lg" radius="md" withBorder>
            <Text size="xl" ta="center">{frontText}</Text>
          </Card>

          <Card className="flip-card-back" shadow="sm" p="lg" radius="md" withBorder>
            <Stack align="center" gap={0}>
              <Text size="xl" mb={4}>{backTitle}</Text>
              <Text size="xl" fw={600}>{backTranslation}</Text>
            </Stack>
          </Card>
        </div>
      </Box>

      {/* Action Buttons */}
      <Group justify="center">
        <Button 
          onClick={onNext}
          color="green"
          radius="md"
        >
          Next Verb
        </Button>

        <Button 
          onClick={toggleConjugations}
          color="grape"
          radius="md"
        >
          {showConjugations ? 'Hide Conjugations' : 'Show Conjugations'}
        </Button>
      </Group>

      {/* Conjugation Details */}
      {showConjugations && (
        <Paper shadow="sm" p="lg" radius="md" withBorder w="100%" maw={800} mt="lg">
          <Title order={2} mb="sm">
            {verb.infinitif} ({verb.english_text})
          </Title>
          <Text mb="md">Group: {verb.groupe} | Auxiliary: {verb.auxiliaire}</Text>

          <Grid>
            {/* Present Tenses */}
            <Grid.Col span={{ base: 12, md: 6 }}>
              <ConjugationTable
                title="Present (Présent)"
                conjugation={verb.indicatif_present}
              />
            </Grid.Col>

            {/* Imperfect Tense */}
            <Grid.Col span={{ base: 12, md: 6 }}>
              <ConjugationTable
                title="Imperfect (Imparfait)"
                conjugation={verb.indicatif_imparfait}
              />
            </Grid.Col>

            {/* Future Simple */}
            <Grid.Col span={{ base: 12, md: 6 }}>
              <ConjugationTable
                title="Future (Futur Simple)"
                conjugation={verb.indicatif_futur_simple}
              />
            </Grid.Col>

            {/* Passé Composé */}
            <Grid.Col span={{ base: 12, md: 6 }}>
              <ConjugationTable
                title="Past Perfect (Passé Composé)"
                conjugation={verb.indicatif_passe_compose}
              />
            </Grid.Col>

            {/* Conditional Present */}
            <Grid.Col span={{ base: 12, md: 6 }}>
              <ConjugationTable
                title="Conditional (Conditionnel Présent)"
                conjugation={verb.conditionnel_present}
              />
            </Grid.Col>

            {/* Subjunctive Present */}
            <Grid.Col span={{ base: 12, md: 6 }}>
              <ConjugationTable
                title="Subjunctive (Subjonctif Présent)"
                conjugation={verb.subjonctif_present}
              />
            </Grid.Col>

            {/* Imperative Present */}
            <Grid.Col span={{ base: 12, md: 6 }}>
              <Box mb="md">
                <Title order={3} mb="xs">Imperative (Impératif)</Title>
                <Table withColumnBorders withTableBorder>
                  <Table.Thead>
                    <Table.Tr>
                      <Table.Th>Person</Table.Th>
                      <Table.Th>Imperative</Table.Th>
                    </Table.Tr>
                  </Table.Thead>
                  <Table.Tbody>
                    <Table.Tr>
                      <Table.Td>Tu</Table.Td>
                      <Table.Td>{verb.imperatif_present.tu}</Table.Td>
                    </Table.Tr>
                    <Table.Tr>
                      <Table.Td>Nous</Table.Td>
                      <Table.Td>{verb.imperatif_present.nous}</Table.Td>
                    </Table.Tr>
                    <Table.Tr>
                      <Table.Td>Vous</Table.Td>
                      <Table.Td>{verb.imperatif_present.vous}</Table.Td>
                    </Table.Tr>
                  </Table.Tbody>
                </Table>
              </Box>
            </Grid.Col>

            {/* Participle Section */}
            <Grid.Col span={{ base: 12, md: 6 }}>
              <Box mb="md">
                <Title order={3} mb="xs">Participle</Title>
                <Table withColumnBorders withTableBorder>
                  <Table.Thead>
                    <Table.Tr>
                      <Table.Th>Form</Table.Th>
                      <Table.Th>Participle</Table.Th>
                    </Table.Tr>
                  </Table.Thead>
                  <Table.Tbody>
                    <Table.Tr>
                      <Table.Td>Present (Présent)</Table.Td>
                      <Table.Td>{verb.participe_present}</Table.Td>
                    </Table.Tr>
                    <Table.Tr>
                      <Table.Td>Past (Passé)</Table.Td>
                      <Table.Td>{verb.participe_passe}</Table.Td>
                    </Table.Tr>
                  </Table.Tbody>
                </Table>
              </Box>
            </Grid.Col>
          </Grid>
        </Paper>
      )}
    </Stack>
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
  // Define color scheme based on tense title - currently not used
  // Commented out to avoid unused function warning
  /*
  const getTenseColor = (title: string) => {
    const colorMap: { [key: string]: string } = {
      "Present (Présent)": "blue",
      "Imperfect (Imparfait)": "green",
      "Future (Futur Simple)": "violet",
      "Past Perfect (Passé Composé)": "yellow",
      "Conditional (Conditionnel Présent)": "pink",
      "Subjunctive (Subjonctif Présent)": "teal",
    };

    return colorMap[title] || "gray";
  };
  */

  // Note: We previously had color-coding for different tenses, but it's not currently used
  // const color = getTenseColor(title);

  return (
    <Box mb="md">
      <Title order={3} mb="xs">{title}</Title>
      <Table withColumnBorders withTableBorder>
        <Table.Thead>
          <Table.Tr>
            <Table.Th>Person</Table.Th>
            <Table.Th>{title}</Table.Th>
          </Table.Tr>
        </Table.Thead>
        <Table.Tbody>
          <Table.Tr>
            <Table.Td>Je</Table.Td>
            <Table.Td>{conjugation.je}</Table.Td>
          </Table.Tr>
          <Table.Tr>
            <Table.Td>Tu</Table.Td>
            <Table.Td>{conjugation.tu}</Table.Td>
          </Table.Tr>
          <Table.Tr>
            <Table.Td>Il/Elle</Table.Td>
            <Table.Td>{conjugation.il_elle}</Table.Td>
          </Table.Tr>
          <Table.Tr>
            <Table.Td>Nous</Table.Td>
            <Table.Td>{conjugation.nous}</Table.Td>
          </Table.Tr>
          <Table.Tr>
            <Table.Td>Vous</Table.Td>
            <Table.Td>{conjugation.vous}</Table.Td>
          </Table.Tr>
          <Table.Tr>
            <Table.Td>Ils/Elles</Table.Td>
            <Table.Td>{conjugation.ils_elles}</Table.Td>
          </Table.Tr>
        </Table.Tbody>
      </Table>
    </Box>
  );
};

export default VerbCard;
