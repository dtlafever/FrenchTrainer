import { Outlet } from 'react-router-dom';
import { AppShell, Text } from '@mantine/core';
import Navigation from './Navigation';

const Layout = () => {
  return (
    <AppShell
      header={{ height: 60 }}
      footer={{ height: 60 }}
      bg="gray.0"
    >
      <AppShell.Header>
        <Navigation />
      </AppShell.Header>

      <AppShell.Main py="md">
        <Outlet />
      </AppShell.Main>

      <AppShell.Footer>
          <Text ta="center" c="white">
            French Trainer &copy; {new Date().getFullYear()}
          </Text>
      </AppShell.Footer>
    </AppShell>
  );
};

export default Layout;
