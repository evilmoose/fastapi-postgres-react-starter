import { useAuth } from '../contexts/AuthContext';
import NormalScrollLayout from '../components/NormalScrollLayout';

const Home = () => {
  const { currentUser } = useAuth();
  
  return (
    <NormalScrollLayout>
      <h1>Home</h1>
    </NormalScrollLayout>
  );
};

export default Home;