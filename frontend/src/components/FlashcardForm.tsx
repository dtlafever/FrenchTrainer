import { useState } from 'react';
import { createFlashcard } from '../services/api';
import { TextInput, Button, Paper, Alert, Stack, Group } from '@mantine/core';
import { useForm } from '@mantine/form';

interface FlashcardFormProps {
  onFlashcardCreated: () => void;
}

const FlashcardForm: React.FC<FlashcardFormProps> = ({ onFlashcardCreated }) => {
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const form = useForm({
    initialValues: {
      question: '',
      answer: '',
    },
    validate: {
      question: (value) => (!value.trim() ? 'Question is required' : null),
      answer: (value) => (!value.trim() ? 'Answer is required' : null),
    },
  });

  const handleSubmit = async (values: { question: string; answer: string }) => {
    setIsSubmitting(true);
    setError(null);

    try {
      await createFlashcard(values);
      form.reset();
      onFlashcardCreated();
    } catch (err) {
      setError('Failed to create flashcard. Please try again.');
      console.error('Error creating flashcard:', err);
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <Paper shadow="xs" p="md" mb="md" radius="md">
      <form onSubmit={form.onSubmit(handleSubmit)}>
        {/*<Stack spacing="md">*/}
        <Stack>
          <TextInput
            label="Question (French)"
            placeholder="e.g. Bonjour"
            required
            {...form.getInputProps('question')}
          />

          <TextInput
            label="Answer (English)"
            placeholder="e.g. Hello"
            required
            {...form.getInputProps('answer')}
          />

          {error && (
            <Alert color="red" title="Error" variant="filled">
              {error}
            </Alert>
          )}

          <Group justify="flex-end">
            <Button
              type="submit"
              loading={isSubmitting}
              disabled={isSubmitting}
            >
              {isSubmitting ? 'Adding...' : 'Add Flashcard'}
            </Button>
          </Group>
        </Stack>
      </form>
    </Paper>
  );
};

export default FlashcardForm;
