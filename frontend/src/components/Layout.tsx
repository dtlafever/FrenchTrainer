import { Outlet } from 'react-router-dom';
import Navigation from './Navigation';

const Layout = () => {
  return (
    <div className="min-h-screen flex flex-col bg-gray-100">
      <Navigation />
      <main className="flex-grow py-6">
        <Outlet />
      </main>
      <footer className="bg-gray-800 text-white p-4 text-center">
        <p>French Trainer &copy; {new Date().getFullYear()}</p>
      </footer>
    </div>
  );
};

export default Layout;