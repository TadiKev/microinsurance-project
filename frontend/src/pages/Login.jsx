import { useState } from 'react';
import api from '../services/api';

export default function Login({ onLogin }) {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState(null);

  const submit = async (e) => {
    e.preventDefault();
    try {
      const resp = await api.post('/token/', { username, password });
      localStorage.setItem('access_token', resp.data.access);
      localStorage.setItem('refresh_token', resp.data.refresh);
      if (onLogin) onLogin();
    } catch (err) {
      setError('Invalid credentials');
    }
  };

  return (
    <form onSubmit={submit} className="max-w-md mx-auto p-4">
      <h2 className="text-xl font-semibold mb-4">Login</h2>
      {error && <div className="text-red-500 mb-2">{error}</div>}
      <input value={username} onChange={e=>setUsername(e.target.value)} placeholder="Username" className="mb-2 p-2 border w-full"/>
      <input type="password" value={password} onChange={e=>setPassword(e.target.value)} placeholder="Password" className="mb-2 p-2 border w-full"/>
      <button type="submit" className="bg-green-600 text-white px-4 py-2 rounded">Login</button>
    </form>
  );
}
