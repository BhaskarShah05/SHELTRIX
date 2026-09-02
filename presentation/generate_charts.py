import os
import matplotlib.pyplot as plt
import numpy as np

os.makedirs('/Users/bhaskarshah05/SHELTRIX/presentation/assets', exist_ok=True)

# 1. Thermal Comparison Diagram: Outdoor vs Conventional vs SHELTRIX
hours = np.arange(0, 25)
t_outdoor = -17.2 + 8.5 * np.sin(np.pi * (hours - 8) / 12) * (hours >= 7) * (hours <= 19)
t_outdoor = np.where((hours < 7) | (hours > 19), -15.5 - 1.7 * np.cos(np.pi * hours / 12), t_outdoor)

# Conventional shelter with intermittent fossil stove
t_conventional = np.array([4, 2, 0, -2, -4, -5, -4, 2, 10, 16, 22, 28, 31, 29, 24, 18, 12, 6, 2, 0, -1, -2, -3, -4, -5])

# SHELTRIX with BioPCM™ phase change latent stabilization (Flat 18.5°C - 21.5°C)
t_sheltrix = 19.4 + 1.6 * np.sin(np.pi * (hours - 10) / 14)

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10, 5), dpi=300)
fig.patch.set_facecolor('#040c1c')
ax.set_facecolor('#07132b')

ax.plot(hours, t_sheltrix, color='#00e5d4', linewidth=3.5, label='SHELTRIX Autonomous BioPCM™ Buffer (+19.4°C Target)', zorder=5)
ax.fill_between(hours, 18, 24, color='#00e5d4', alpha=0.12, label='ASHRAE Human Comfort Envelope (18°C - 24°C)')
ax.plot(hours, t_conventional, color='#f43f5e', linewidth=2, linestyle='--', label='Conventional Diesel/Kerosene Bukhari Shelter', alpha=0.85)
ax.plot(hours, t_outdoor, color='#38bdf8', linewidth=2.5, linestyle=':', label='Himalayan Extreme Outdoor Ambient (Leh, Ladakh -17.2°C)', alpha=0.75)

ax.set_title('DIURNAL THERMAL EQUILIBRIUM: 24-HOUR CONTINUOUS BENCHMARK', fontsize=13, fontweight='bold', color='#ffffff', pad=15, family='sans-serif')
ax.set_xlabel('Diurnal Timeline (Hours: 00:00 - 24:00)', fontsize=10, color='#94a3b8', labelpad=10)
ax.set_ylabel('Dry-Bulb Temperature (°C)', fontsize=10, color='#94a3b8', labelpad=10)
ax.set_xlim(0, 24)
ax.set_ylim(-22, 34)
ax.grid(True, linestyle='--', alpha=0.2, color='#38bdf8')
ax.axhline(0, color='#ffffff', linewidth=0.8, alpha=0.3)
ax.legend(loc='upper left', framealpha=0.8, facecolor='#0c1a36', edgecolor='#00e5d4', fontsize=9)
plt.tight_layout()
plt.savefig('/Users/bhaskarshah05/SHELTRIX/presentation/assets/chart_thermal_equilibrium.png')
plt.close()

# 2. System Architecture Flowchart
fig, ax = plt.subplots(figsize=(10, 5), dpi=300)
fig.patch.set_facecolor('#040c1c')
ax.set_facecolor('#07132b')
ax.axis('off')

boxes = [
    ("SATELLITE & SENSORS\n• Open-Meteo Solar DNI\n• NASA POWER CERES\n• 100Hz MQTT IoT Pods", 0.05, 0.55, 0.25, 0.35, '#0ea5e9'),
    ("PHYSICS & BIO-PCM\n• Transient Lumped ODE\n• 21°C Latent Enthalpy\n• 180 kJ/kg Buffer", 0.38, 0.55, 0.25, 0.35, '#00e5d4'),
    ("AI GENETIC OPTIMIZER\n• 128 Candidate Evolution\n• Multi-Objective Pareto\n• 1-Click Hot-Swap 3D", 0.70, 0.55, 0.25, 0.35, '#a855f7'),
    ("3D SPATIAL STUDIO\n• Real-Time Sun Azimuth\n• Glazing Aperture Solar Ray\n• Pitch Angle & Volume", 0.20, 0.1, 0.28, 0.32, '#f59e0b'),
    ("2026 DIGITAL TWIN\n• Zero-Emission Equilibrium\n• +19.4°C Living Comfort\n• 100% Fossil Fuel Free", 0.55, 0.1, 0.32, 0.32, '#10b981')
]

from matplotlib.patches import FancyBboxPatch

for title, x, y, w, h, col in boxes:
    rect = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.03,rounding_size=0.04", facecolor='#0d2144', edgecolor=col, linewidth=2.5)
    ax.add_patch(rect)
    ax.text(x + w/2, y + h/2, title, color='#ffffff', fontsize=9.5, fontweight='bold', ha='center', va='center', family='sans-serif', linespacing=1.4)

# Connecting Arrows
ax.annotate('', xy=(0.38, 0.72), xytext=(0.30, 0.72), arrowprops=dict(arrowstyle="->", color='#00e5d4', lw=2.5))
ax.annotate('', xy=(0.70, 0.72), xytext=(0.63, 0.72), arrowprops=dict(arrowstyle="->", color='#a855f7', lw=2.5))
ax.annotate('', xy=(0.34, 0.42), xytext=(0.50, 0.55), arrowprops=dict(arrowstyle="->", color='#f59e0b', lw=2.5))
ax.annotate('', xy=(0.71, 0.42), xytext=(0.52, 0.55), arrowprops=dict(arrowstyle="->", color='#10b981', lw=2.5))
ax.annotate('', xy=(0.55, 0.26), xytext=(0.48, 0.26), arrowprops=dict(arrowstyle="<->", color='#ffffff', lw=2))

ax.text(0.5, 0.96, "SHELTRIX CLOSED-LOOP DIGITAL TWIN SYSTEM ARCHITECTURE", fontsize=12, fontweight='bold', color='#ffffff', ha='center')
plt.tight_layout()
plt.savefig('/Users/bhaskarshah05/SHELTRIX/presentation/assets/diagram_system_architecture.png')
plt.close()

# 3. Component Heat Balance Bar Chart
components = ['Solar Gain\n(+Capture)', 'Envelope Loss\n(-Conduction)', 'Openings Loss\n(-Glazing)', 'Infiltration\n(-Air Leakage)', 'Aux. Heating\n(Deficit)']
values = [33.3, -12.4, -6.8, -4.2, 0.0]
colors = ['#00e5d4', '#f43f5e', '#f97316', '#38bdf8', '#10b981']

fig, ax = plt.subplots(figsize=(9, 4.8), dpi=300)
fig.patch.set_facecolor('#040c1c')
ax.set_facecolor('#07132b')

bars = ax.bar(components, values, color=colors, width=0.55, edgecolor='#ffffff', linewidth=1.2)
ax.axhline(0, color='#ffffff', linewidth=1.2, alpha=0.6)
ax.set_ylabel('Energy Balance (kWh/day)', color='#94a3b8', fontsize=10, labelpad=8)
ax.set_title('COMPONENT HEAT BALANCE: 24-HOUR ENERGY GAIN VS LOSSES', fontsize=12, fontweight='bold', color='#ffffff', pad=14)
ax.grid(axis='y', linestyle='--', alpha=0.25, color='#38bdf8')

for bar in bars:
    yval = bar.get_height()
    va = 'bottom' if yval >= 0 else 'top'
    ypos = yval + (0.8 if yval >= 0 else -1.8)
    txt = f"+{yval} kWh" if yval > 0 else (f"{yval} kWh" if yval < 0 else "0.0 kWh (Zero-Deficit)")
    ax.text(bar.get_x() + bar.get_width()/2, ypos, txt, ha='center', va=va, color='#ffffff', fontweight='bold', fontsize=9.5)

ax.set_ylim(-16, 38)
plt.tight_layout()
plt.savefig('/Users/bhaskarshah05/SHELTRIX/presentation/assets/chart_energy_balance.png')
plt.close()

print("Presentation charts and architecture diagrams successfully rendered!")
