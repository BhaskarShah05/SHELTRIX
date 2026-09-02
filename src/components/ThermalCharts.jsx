import React from 'react';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  BarElement,
  Title,
  Tooltip,
  Legend,
  Filler
} from 'chart.js';
import { Line, Bar } from 'react-chartjs-2';

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  BarElement,
  Title,
  Tooltip,
  Legend,
  Filler
);

export function TemperatureProfileChart({ simResults, comfortTarget }) {
  const labels = simResults.series.map(s => s.time);
  const indoorTemps = simResults.series.map(s => s.indoorTemp);
  const ambientTemps = simResults.series.map(s => s.ambientTemp);

  const data = {
    labels,
    datasets: [
      {
        label: 'Shelter Indoor (°C)',
        data: indoorTemps,
        borderColor: '#00d2c4',
        backgroundColor: 'rgba(0, 210, 196, 0.18)',
        borderWidth: 3,
        tension: 0.4,
        fill: true,
        pointBackgroundColor: '#00d2c4',
        pointRadius: 3,
        pointHoverRadius: 6
      },
      {
        label: 'Ladakh Ambient Outdoor (°C)',
        data: ambientTemps,
        borderColor: '#94a3b8',
        backgroundColor: 'transparent',
        borderWidth: 2,
        borderDash: [5, 5],
        tension: 0.4,
        pointRadius: 2
      },
      {
        label: 'Target Comfort Threshold (18°C)',
        data: Array(labels.length).fill(comfortTarget.min),
        borderColor: '#f59e0b',
        borderWidth: 1.5,
        borderDash: [3, 3],
        pointRadius: 0
      }
    ]
  };

  const options = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        position: 'top',
        labels: {
          color: '#06152d',
          font: { family: 'SF Pro Display, -apple-system, sans-serif', size: 12, weight: '700' }
        }
      },
      tooltip: {
        backgroundColor: 'rgba(12, 25, 48, 0.92)',
        titleColor: '#00e5d4',
        bodyColor: '#ffffff',
        titleFont: { family: 'SF Pro Display, -apple-system, sans-serif', size: 13, weight: '700' },
        bodyFont: { family: 'SF Pro Text, -apple-system, sans-serif', size: 12 },
        padding: 12,
        cornerRadius: 12,
        borderColor: 'rgba(0, 229, 212, 0.4)',
        borderWidth: 1
      }
    },
    scales: {
      x: {
        grid: { color: 'rgba(0,0,0,0.06)' },
        ticks: { color: '#06152d', font: { size: 11, weight: '700', family: 'SF Pro Text, -apple-system, sans-serif' } }
      },
      y: {
        grid: { color: 'rgba(0,0,0,0.06)' },
        ticks: { color: '#06152d', font: { size: 11, weight: '700', family: 'SF Pro Text, -apple-system, sans-serif' }, callback: (v) => `${v}°C` }
      }
    }
  };

  return (
    <div style={{ width: '100%', height: '240px', background: 'rgba(255, 255, 255, 0.25)', backdropFilter: 'blur(20px)', WebkitBackdropFilter: 'blur(20px)', borderRadius: '18px', padding: '16px', border: '1px solid rgba(255, 255, 255, 0.5)' }}>
      <Line data={data} options={options} />
    </div>
  );
}

export function EnergyBreakdownChart({ simResults }) {
  const data = {
    labels: ['Solar Gain', 'Envelope Loss', 'Openings Loss', 'Ventilation Infil.', 'Aux. Heating Deficit'],
    datasets: [
      {
        label: 'Energy (kWh/day)',
        data: [
          simResults.solarGainKwh,
          simResults.envelopeLossKwh,
          simResults.openingLossKwh,
          simResults.ventLossKwh,
          simResults.supplementalHeatingKwh
        ],
        backgroundColor: [
          'rgba(0, 229, 212, 0.9)',
          'rgba(244, 63, 94, 0.85)',
          'rgba(249, 115, 22, 0.85)',
          'rgba(56, 189, 248, 0.85)',
          'rgba(239, 68, 68, 0.9)'
        ],
        borderRadius: 14,
        borderWidth: 1.5,
        borderColor: [
          '#00e5d4',
          '#f43f5e',
          '#f97316',
          '#38bdf8',
          '#ef4444'
        ]
      }
    ]
  };

  const options = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: { display: false },
      tooltip: {
        backgroundColor: 'rgba(12, 25, 48, 0.92)',
        titleColor: '#00e5d4',
        bodyColor: '#ffffff',
        titleFont: { family: 'SF Pro Display, -apple-system, sans-serif', size: 13, weight: '700' },
        bodyFont: { family: 'SF Pro Text, -apple-system, sans-serif', size: 12, weight: '600' },
        padding: 12,
        cornerRadius: 12,
        borderColor: 'rgba(0, 229, 212, 0.4)',
        borderWidth: 1
      }
    },
    scales: {
      x: {
        grid: { display: false },
        ticks: {
          color: '#06152d',
          font: { size: 11, weight: '800', family: 'SF Pro Display, -apple-system, sans-serif' }
        }
      },
      y: {
        grid: { color: 'rgba(255, 255, 255, 0.25)' },
        ticks: {
          color: '#06152d',
          font: { size: 11, weight: '700', family: 'SF Pro Display, -apple-system, sans-serif' },
          callback: (v) => `${v} kWh`
        }
      }
    }
  };

  return (
    <div style={{ width: '100%', height: '220px', background: 'rgba(255, 255, 255, 0.25)', backdropFilter: 'blur(20px)', WebkitBackdropFilter: 'blur(20px)', borderRadius: '18px', padding: '16px', border: '1px solid rgba(255, 255, 255, 0.5)' }}>
      <Bar data={data} options={options} />
    </div>
  );
}
