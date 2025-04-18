import { useState } from 'react';
import { createVerb } from '../services/api';
import { TextInput, Paper, Button, Alert, Text, Stack, Group } from '@mantine/core';

interface VerbFormProps {
  onVerbCreated: () => void;
}

const VerbForm: React.FC<VerbFormProps> = ({ onVerbCreated }) => {
  const [verb, setVerb] = useState('');
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!verb.trim()) {
      setError('Verb is required');
      return;
    }

    setIsSubmitting(true);
    setError(null);

    try {
      await createVerb(verb);
      setVerb('');
      onVerbCreated();
    } catch (err: any) {
      if (err.response && err.response.status === 404) {
        setError('Verb not found in the dictionary. Please check spelling.');
      } else {
        setError('Failed to create verb. Please try again.');
      }
      console.error('Error creating verb:', err);
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <Paper shadow="xs" p="md" mb="md" radius="md" withBorder>
      <form onSubmit={handleSubmit}>
        <Stack spacing="md">
          <TextInput
            label="French Verb (infinitive form)"
            value={verb}
            onChange={(e) => setVerb(e.target.value)}
            placeholder="e.g. parler"
            required
            description="Enter the infinitive form of a French verb (e.g. parler, manger, finir)"
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
              {isSubmitting ? 'Looking up verb...' : 'Add Verb'}
            </Button>
          </Group>
        </Stack>
      </form>
    </Paper>
  );
};

export default VerbForm;
