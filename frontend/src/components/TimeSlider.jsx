// frontend/src/components/TimeSlider.jsx

import React from 'react';
import styles from '../styles/TimeSlider.module.css';

export default function TimeSlider({ length, currentIndex, onChange }) {
  return (
    <div className={styles.sliderContainer}>
      <input
        type="range"
        min={0}
        max={length - 1}
        value={currentIndex}
        onChange={e => onChange(Number(e.target.value))}
      />
      <div>Step: {currentIndex + 1} / {length}</div>
    </div>
  );
}
