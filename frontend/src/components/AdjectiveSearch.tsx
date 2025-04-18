import { useState } from 'react';
import { searchAdjectives, FrenchAdjective } from '../services/api';
import { TextInput, Button, Group, Alert, Flex, Box, Loader } from '@mantine/core';

interface AdjectiveSearchProps {
  onAdjectiveFound: (adjective: FrenchAdjective) => void;
}

const AdjectiveSearch: React.FC<AdjectiveSearchProps> = ({ onAdjectiveFound }) => {
  const [searchTerm, setSearchTerm] = useState('');
  const [isSearching, setIsSearching] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleSearch = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!searchTerm.trim()) {
      setError('Please enter an adjective to search');
      return;
    }

    setIsSearching(true);
    setError(null);

    try {
      const results = await searchAdjectives(searchTerm);
      if (results) {
        onAdjectiveFound(results);
        setSearchTerm('');
      } else {
        setError(`Adjective "${searchTerm}" not found. Please check spelling.`);
      }
    } catch (err: any) {
      if (err.response && err.response.status === 404) {
        setError(`Adjective "${searchTerm}" not found. Please check spelling.`);
      } else {
        setError('Failed to search for adjective. Please try again.');
      }
      console.error('Error searching adjective:', err);
    } finally {
      setIsSearching(false);
    }
  };

  return (
    <Box pos="relative">
      <form onSubmit={handleSearch}>
        <Flex>
          <TextInput
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            placeholder="Search for an adjective"
            style={{ flexGrow: 1 }}
            radius="md"
            styles={{ input: { borderTopRightRadius: 0, borderBottomRightRadius: 0 } }}
            error={error}
          />
          <Button
            type="submit"
            loading={isSearching}
            disabled={isSearching}
            radius="md"
            styles={{ root: { borderTopLeftRadius: 0, borderBottomLeftRadius: 0 } }}
          >
            {isSearching ? 'Searching...' : 'Search'}
          </Button>
        </Flex>
      </form>
    </Box>
  );
};

export default AdjectiveSearch;
