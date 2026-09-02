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

export function TemperatureProfileChart({ simResults, comfortTarget, compareSimResults = null, sensorTelemetry = null }) {
  const labels = simResults.series.map(s => s.time);
  const indoorTemps = simResults.series.map(s => s.indoorTemp);
  const ambientTemps = simResults.series.map(s => s.ambientTemp);

  const datasets = [
    {
      label: compareSimResults ? 'Design A / Current Indoor (°C)' : 'Shelter Indoor (°C)',
      data: indoorTemps,
      borderColor: '#00d2c4',
      backgroundColor: 'rgba(0, 210, 196, 0.18)',
      borderWidth: 3,
      tension: 0.4,
      fill: !compareSimResults,
      pointBackgroundColor: '#00d2c4',
      pointRadius: 3,
      pointHoverRadius: 6
    },
    {
      label: 'Ambient Outdoor (°C)',
      data: ambientTemps,
      borderColor: '#94a3b8',
      backgroundColor: 'transparent',
      borderWidth: 2,
      borderDash: [5, 5],
      tension: 0.4,
      pointRadius: 2
    },
    {
      label: 'Comfort Min (18°C)',
      data: Array(labels.length).fill(comfortTarget.min),
      borderColor: '#f59e0b',
      borderWidth: 1.5,
      borderDash: [3, 3],
      pointRadius: 0
    }
  ];

  if (compareSimResults) {
    const compareTemps = compareSimResults.series.map(s => s.indoorTemp);
    datasets.splice(1, 0, {
      label: 'Design B / Baseline Indoor (°C)',
      data: compareTemps,
      borderColor: '#ec4899',
      backgroundColor: 'transparent',
      borderWidth: 2.5,
      tension: 0.4,
      pointBackgroundColor: '#ec4899',
      pointRadius: 3
    });
  }

  if (sensorTelemetry && sensorTelemetry.historicalTemps) {
    datasets.push({
      label: 'IoT Hardware Actual (°C)',
      data: sensorTelemetry.historicalTemps,
      borderColor: '#a855f7',
      backgroundColor: 'transparent',
      borderWidth: 2,
      borderDash: [2, 2],
      pointRadius: 2
    });
  }

  const data = {
    labels,
    datasets
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

/**
 * 24-Hour Continuous Heat Flow Breakdown (W / kW over time)
 * Shows separate loss/gain paths: Solar Gain, Wall Conduction, Roof Loss, Openings & Infiltration
 */
export function HeatFlowPathChart({ simResults }) {
  const labels = simResults.series.map(s => s.time);
  const solarGains = simResults.series.map(s => s.solarGainWatts);
  const envelopeLosses = simResults.series.map(s => -s.envelopeLossWatts);
  const openingLosses = simResults.series.map(s => -s.openingLossWatts);
  const ventLosses = simResults.series.map(s => -s.ventLossWatts);
  const netFlux = simResults.series.map(s => s.qNetWatts);

  const data = {
    labels,
    datasets: [
      {
        label: 'Solar Harvest (+W)',
        data: solarGains,
        borderColor: '#00e5d4',
        backgroundColor: 'rgba(0, 229, 212, 0.15)',
        borderWidth: 2.5,
        fill: true,
        tension: 0.35,
        pointRadius: 2
      },
      {
        label: 'Net Flux Q_net (W)',
        data: netFlux,
        borderColor: '#ffffff',
        borderWidth: 2,
        borderDash: [4, 4],
        tension: 0.35,
        pointRadius: 0
      },
      {
        label: 'Envelope Conduction (-W)',
        data: envelopeLosses,
        borderColor: '#f43f5e',
        backgroundColor: 'transparent',
        borderWidth: 2,
        tension: 0.35,
        pointRadius: 1.5
      },
      {
        label: 'Openings Glazing Loss (-W)',
        data: openingLosses,
        borderColor: '#f97316',
        backgroundColor: 'transparent',
        borderWidth: 1.8,
        tension: 0.35,
        pointRadius: 1.5
      },
      {
        label: 'Infiltration / Vent (-W)',
        data: ventLosses,
        borderColor: '#38bdf8',
        backgroundColor: 'transparent',
        borderWidth: 1.8,
        tension: 0.35,
        pointRadius: 1.5
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
          font: { family: 'SF Pro Display, -apple-system, sans-serif', size: 11, weight: '700' },
          boxWidth: 12
        }
      },
      tooltip: {
        backgroundColor: 'rgba(12, 25, 48, 0.94)',
        titleColor: '#00e5d4',
        bodyColor: '#ffffff',
        titleFont: { family: 'SF Pro Display, -apple-system, sans-serif', size: 13, weight: '700' },
        bodyFont: { family: 'SF Pro Text, -apple-system, sans-serif', size: 12 },
        padding: 12,
        cornerRadius: 12,
        borderColor: 'rgba(0, 229, 212, 0.4)',
        borderWidth: 1,
        callbacks: {
          label: (ctx) => `${ctx.dataset.label}: ${ctx.raw} W`
        }
      }
    },
    scales: {
      x: {
        grid: { color: 'rgba(0,0,0,0.06)' },
        ticks: { color: '#06152d', font: { size: 10, weight: '700', family: 'SF Pro Text, -apple-system, sans-serif' } }
      },
      y: {
        grid: { color: 'rgba(0,0,0,0.06)' },
        ticks: {
          color: '#06152d',
          font: { size: 10, weight: '700', family: 'SF Pro Text, -apple-system, sans-serif' },
          callback: (v) => `${v} W`
        }
      }
    }
  };

  return (
    <div style={{ width: '100%', height: '260px', background: 'rgba(255, 255, 255, 0.25)', backdropFilter: 'blur(20px)', WebkitBackdropFilter: 'blur(20px)', borderRadius: '18px', padding: '16px', border: '1px solid rgba(255, 255, 255, 0.5)' }}>
      <Line data={data} options={options} />
    </div>
  );
}
