// frontend/src/utils/api.js

const API_BASE = process.env.NEXT_PUBLIC_API_BASE_URL || '';

export async function simulate({ scenario, source, target, algorithm }) {
  const res = await fetch(`${API_BASE}/simulate`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ scenario, source, target, algorithm }),
  });
  if (!res.ok) {
    const err = await res.json();
    throw new Error(err.detail || 'Simulation failed');
  }
  return res.json();
}

export async function downloadReport(region) {
  const res = await fetch(`${API_BASE}/report/${region}`, {
    method: 'GET',
    headers: { Accept: 'application/pdf' },
  });
  if (!res.ok) {
    const err = await res.json();
    throw new Error(err.detail || 'Report generation failed');
  }
  const blob = await res.blob();
  const url = window.URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = `${region}_climate_report.pdf`;
  document.body.appendChild(a);
  a.click();
  a.remove();
  window.URL.revokeObjectURL(url);
}
