// frontend/src/components/Dashboard.jsx

import React, { useState, useRef, useEffect } from 'react';
import Map from './Map';
import VesselLayer from './VesselLayer';
import TimeSlider from './TimeSlider';
import ReportPanel from './ReportPanel';
import useSimulation from '../hooks/useSimulation';
import styles from '../styles/Dashboard.module.css';

export default function Dashboard() {
  // User inputs
  const [scenario, setScenario] = useState('panama_drought');
  const [source, setSource] = useState([24.0, -90.0]);
  const [target, setTarget] = useState([29.0, -85.0]);
  const [algorithm, setAlgorithm] = useState('dijkstra');

  // Run simulation & hold result
  const { data: simData, loading, error, runSimulation } = useSimulation();

  // Time slider index
  const [currentIndex, setCurrentIndex] = useState(0);

  // When new data arrives, reset slider
  useEffect(() => {
    if (simData?.path) {
      setCurrentIndex(0);
    }
  }, [simData]);

  const handleRun = () => {
    runSimulation({ scenario, source, target, algorithm });
  };

  return (
    <div className={styles.container}>
      <aside className={styles.sidebar}>
        <h2>Simulation Controls</h2>
        <label>
          Scenario
          <select value={scenario} onChange={e => setScenario(e.target.value)}>
            <option value="panama_drought">Panama Drought</option>
            <option value="hurricane_gulf">Gulf Hurricane</option>
          </select>
        </label>
        <label>
          Source (lat, lon)
          <input
            type="text"
            value={source.join(', ')}
            onChange={e => setSource(e.target.value.split(',').map(Number))}
          />
        </label>
        <label>
          Target (lat, lon)
          <input
            type="text"
            value={target.join(', ')}
            onChange={e => setTarget(e.target.value.split(',').map(Number))}
          />
        </label>
        <label>
          Algorithm
          <select value={algorithm} onChange={e => setAlgorithm(e.target.value)}>
            <option value="dijkstra">Dijkstra</option>
            <option value="astar">A*</option>
          </select>
        </label>
        <button onClick={handleRun} disabled={loading}>
          {loading ? 'Running…' : 'Run Simulation'}
        </button>
        {error && <p className={styles.error}>Error: {error.message}</p>}
        {simData && (
          <div className={styles.results}>
            <p>Total Distance: {simData.total_distance.toFixed(1)} km</p>
            <TimeSlider
              length={simData.path.length}
              currentIndex={currentIndex}
              onChange={setCurrentIndex}
            />
            <ReportPanel region={scenario} />
          </div>
        )}
      </aside>
      <main className={styles.mapContainer}>
        <Map center={source}>
          {simData?.path && (
            <VesselLayer path={simData.path} currentIndex={currentIndex} />
          )}
        </Map>
      </main>
    </div>
);
}
