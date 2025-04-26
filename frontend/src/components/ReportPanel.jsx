// frontend/src/components/ReportPanel.jsx

import React, { useState } from 'react';
import { downloadReport } from '../utils/api';
import styles from '../styles/ReportPanel.module.css';

export default function ReportPanel({ region }) {
  const [loading, setLoading] = useState(false);

  const handleClick = async () => {
    setLoading(true);
    try {
      await downloadReport(region);
    } finally {
      setLoading(false);
    }
  };

  return (
    <button
      className={styles.reportButton}
      onClick={handleClick}
      disabled={loading}
    >
      {loading ? 'Generating PDF…' : 'Generate Report'}
    </button>
  );
}
