import { useState, useEffect } from 'react';
import { searchVerb, FrenchVerb } from '../services/api';
import { Button, TextInput, Modal, Alert, Group } from '@mantine/core';

interface VerbSearchProps {
  onVerbFound: (verb: FrenchVerb) => void;
}

const VerbSearch: React.FC<VerbSearchProps> = ({ onVerbFound }) => {
  const [searchTerm, setSearchTerm] = useState('');
  const [isSearching, setIsSearching] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [isModalOpen, setIsModalOpen] = useState(false);

  const handleSearch = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!searchTerm.trim()) {
      setError('Please enter a verb to search');
      return;
    }

    setIsSearching(true);
    setError(null);

    if (isSearching) {
      console.log('Searching for Verb...');
    }

    try {
      const verb = await searchVerb(searchTerm);
      onVerbFound(verb);
      setSearchTerm('');
      setIsModalOpen(false); // Close modal after successful search
    } catch (err: any) {
      if (err.response && err.response.status === 404) {
        setError(`Verb "${searchTerm}" not found. Please check spelling.`);
      } else {
        setError('Failed to search for verb. Please try again.');
      }
      console.error('Error searching verb:', err);
    } finally {
      setIsSearching(false);
    }
  };

  const openModal = () => {
    setIsModalOpen(true);
    setSearchTerm(''); // Clear the search term when opening the modal
    setError(null); // Clear any previous errors
  };

  const closeModal = () => {
    setIsModalOpen(false);
    setError(null);
  };

  // No need for custom backdrop click or ESC key handling
  // Mantine's Modal component handles these automatically

  return (
    <>
      {/* Compact Search Button with Text */}
      <Button
        onClick={openModal}
        leftIcon={
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
          </svg>
        }
        color="blue"
        variant="filled"
        radius="md"
        aria-label="Search for a verb"
      >
        Search
      </Button>

      {/* Search Modal using Mantine's Modal component */}
      <Modal
        opened={isModalOpen}
        onClose={closeModal}
        title="Search for a Verb"
        centered
        overlayProps={{
          color: 'blue',
          opacity: 0.55,
          blur: 3
        }}
      >
        <form onSubmit={handleSearch}>
          <TextInput
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            placeholder="Search Verb (any tense)"
            required
            autoFocus
            mb="md"
            error={error}
          />

          <Group position="right">
            <Button 
              type="submit" 
              loading={isSearching}
              disabled={isSearching}
            >
              Search
            </Button>
          </Group>
        </form>
      </Modal>
    </>
  );
};

export default VerbSearch;
