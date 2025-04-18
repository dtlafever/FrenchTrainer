import { useState } from 'react';
import { createAdjective, FrenchAdjective } from '../services/api';
import { TextInput, Grid, Paper, Button, Alert, Group, Stack } from '@mantine/core';

interface AdjectiveFormProps {
  onAdjectiveCreated: (adjective: FrenchAdjective) => void;
}

const AdjectiveForm: React.FC<AdjectiveFormProps> = ({ onAdjectiveCreated }) => {
  const [formData, setFormData] = useState({
    masc_french_singular: '',
    fem_french_singular: '',
    masc_french_plural: '',
    fem_french_plural: '',
    english_text: ''
  });

  const [isSubmitting, setIsSubmitting] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleChange = (name: string, value: string) => {
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    // Check if required fields are filled
    if (!formData.masc_french_singular.trim() || !formData.english_text.trim()) {
      setError('Masculine singular form and English translation are required');
      return;
    }

    setIsSubmitting(true);
    setError(null);

    try {
      const adjective = await createAdjective(formData);

      // Reset form
      setFormData({
        masc_french_singular: '',
        fem_french_singular: '',
        masc_french_plural: '',
        fem_french_plural: '',
        english_text: ''
      });

      onAdjectiveCreated(adjective);
    } catch (err: any) {
      if (err.response && err.response.data) {
        setError(err.response.data.detail || 'Failed to create adjective');
      } else {
        setError('Failed to create adjective. Please try again.');
      }
      console.error('Error creating adjective:', err);
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <Paper shadow="xs" p="md" mb="md" radius="md" withBorder>
      <form onSubmit={handleSubmit}>
        <Stack spacing="md">
          <Grid>
            <Grid.Col span={{ base: 12, md: 6 }}>
              <TextInput
                label="Masculine Singular"
                name="masc_french_singular"
                value={formData.masc_french_singular}
                onChange={(e) => handleChange('masc_french_singular', e.target.value)}
                placeholder="e.g. grand"
                required
              />
            </Grid.Col>

            <Grid.Col span={{ base: 12, md: 6 }}>
              <TextInput
                label="Feminine Singular"
                name="fem_french_singular"
                value={formData.fem_french_singular}
                onChange={(e) => handleChange('fem_french_singular', e.target.value)}
                placeholder="e.g. grande"
              />
            </Grid.Col>

            <Grid.Col span={{ base: 12, md: 6 }}>
              <TextInput
                label="Masculine Plural"
                name="masc_french_plural"
                value={formData.masc_french_plural}
                onChange={(e) => handleChange('masc_french_plural', e.target.value)}
                placeholder="e.g. grands"
              />
            </Grid.Col>

            <Grid.Col span={{ base: 12, md: 6 }}>
              <TextInput
                label="Feminine Plural"
                name="fem_french_plural"
                value={formData.fem_french_plural}
                onChange={(e) => handleChange('fem_french_plural', e.target.value)}
                placeholder="e.g. grandes"
              />
            </Grid.Col>
          </Grid>

          <TextInput
            label="English Translation"
            name="english_text"
            value={formData.english_text}
            onChange={(e) => handleChange('english_text', e.target.value)}
            placeholder="e.g. big, large, tall"
            required
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
              {isSubmitting ? 'Adding adjective...' : 'Add Adjective'}
            </Button>
          </Group>
        </Stack>
      </form>
    </Paper>
  );
};

export default AdjectiveForm;
