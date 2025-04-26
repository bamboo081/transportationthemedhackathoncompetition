// frontend/src/hooks/useSimulation.js

import { useState, useCallback } from 'react';
import { simulate } from '../utils/api';

export default function useSimulation() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const runSimulation = useCallback(async (params) => {
    setLoading(true);
    setError(null);
    try {
      const result = await simulate(params);
      setData(result);
    } catch (err) {
      setError(err);
    } finally {
      setLoading(false);
    }
  }, []);

  return { data, loading, error, runSimulation };
}
