import { Link, useLocation } from 'react-router-dom';
import { Group, Title, Container, Flex, Button } from '@mantine/core';

const Navigation = () => {
  const location = useLocation();

  const isActive = (path: string) => {
    return location.pathname === path;
  };

  return (
    <Container fluid h={60} bg="blue.7" c="white">
      <Flex
        justify="space-between"
        align="center"
        h="100%"
        direction={{ base: 'column', md: 'row' }}
      >
        <Link to="/" style={{ color: 'white', textDecoration: 'none' }}>
          <Title order={2}>
            French Trainer
          </Title>
        </Link>

        <Group>
          <Button
            component={Link}
            to="/"
            variant={isActive('/') ? 'filled' : 'subtle'}
            color={isActive('/') ? 'blue.9' : 'blue.0'}
            radius="md"
          >
            Flashcards
          </Button>

          <Button
            component={Link}
            to="/verbs"
            variant={isActive('/verbs') ? 'filled' : 'subtle'}
            color={isActive('/verbs') ? 'blue.9' : 'blue.0'}
            radius="md"
          >
            Verb Conjugations
          </Button>

          <Button
            component={Link}
            to="/adjectives"
            variant={isActive('/adjectives') ? 'filled' : 'subtle'}
            color={isActive('/adjectives') ? 'blue.9' : 'blue.0'}
            radius="md"
          >
            Adjectives
          </Button>

          <Button
            component="a"
            href="http://localhost:8000/chat"
            target="_blank"
            rel="noopener noreferrer"
            variant="subtle"
            color="blue.0"
            radius="md"
          >
            Chat with LLM
          </Button>
        </Group>
      </Flex>
    </Container>
  );
};

export default Navigation;
