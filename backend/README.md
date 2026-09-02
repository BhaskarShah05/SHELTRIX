# 🏔️ SHELTRIX Backend Services

Dedicated Node.js / Express microservice architecture for the **SHELTRIX 2026 Climate Digital Twin & High-Altitude Thermal Engineering Platform**.

## 🔌 API Microservices Provided
- `GET  /api/health` — Microservice health status & operational engine capability matrix
- `GET  /api/climate/locations` — High-altitude benchmark stations (Leh, Siachen, Spiti, Nyoma)
- `GET  /api/climate/query?lat=34.15&lon=77.58` — Real-time Open-Meteo DNI, solar, and weather profiles
- `GET  /api/climate/nasa-benchmark?lat=34.15&lon=77.58` — NASA POWER CERES/MERRA-2 analytical validation
- `POST /api/simulate` — Transient lumped-capacitance ODE solver ($C_{\text{eff}} \frac{dT}{dt}$) with BioPCM™ latent enthalpy model
- `POST /api/optimizer/run` — AI Genetic evolutionary optimizer evaluating 128 candidates for Pareto optimality
- `GET  /api/iot/telemetry` — Live 100Hz MQTT TLSv1.3 sensor telemetry stream

## 🚀 Running Backend Locally

```bash
cd backend
npm install
npm run dev
```

The server will listen at `http://localhost:5001`.
