import os
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak, KeepTogether
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas

OUTPUT_DIR = '/Users/bhaskarshah05/SHELTRIX/presentation/output'
ASSETS_DIR = '/Users/bhaskarshah05/SHELTRIX/presentation/assets'
PUBLIC_ASSETS = '/Users/bhaskarshah05/SHELTRIX/public/assets'
os.makedirs(OUTPUT_DIR, exist_ok=True)

pdf_path = os.path.join(OUTPUT_DIR, 'SHELTRIX_Presentation.pdf')

def draw_background(canvas_obj, doc_obj):
    canvas_obj.saveState()
    # Dark Midnight Navy Background
    canvas_obj.setFillColor(colors.HexColor('#040c1c'))
    canvas_obj.rect(0, 0, 11 * inch, 8.5 * inch, fill=True, stroke=False)
    
    # Top Cyan Line
    canvas_obj.setStrokeColor(colors.HexColor('#00e5d4'))
    canvas_obj.setLineWidth(2)
    canvas_obj.line(0.6 * inch, 8.0 * inch, 10.4 * inch, 8.0 * inch)

    # Bottom Slate Line
    canvas_obj.setStrokeColor(colors.HexColor('#1e293b'))
    canvas_obj.setLineWidth(1)
    canvas_obj.line(0.6 * inch, 0.55 * inch, 10.4 * inch, 0.55 * inch)

    # Footer Branding
    canvas_obj.setFont("Helvetica-Bold", 8)
    canvas_obj.setFillColor(colors.HexColor('#00e5d4'))
    canvas_obj.drawString(0.6 * inch, 0.38 * inch, "SHELTRIX 2026 CLIMATE DIGITAL TWIN")
    
    canvas_obj.setFont("Helvetica", 8)
    canvas_obj.setFillColor(colors.HexColor('#94a3b8'))
    canvas_obj.drawString(3.6 * inch, 0.38 * inch, "Autonomous Passive Solar High-Altitude Thermal Engineering Platform")
    
    page_str = f"Page {canvas_obj._pageNumber} of 8"
    canvas_obj.drawRightString(10.4 * inch, 0.38 * inch, page_str)
    canvas_obj.restoreState()

doc = SimpleDocTemplate(
    pdf_path,
    pagesize=landscape(letter),
    leftMargin=0.6 * inch,
    rightMargin=0.6 * inch,
    topMargin=0.65 * inch,
    bottomMargin=0.65 * inch
)

styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    'DocTitle',
    parent=styles['Heading1'],
    fontName='Helvetica-Bold',
    fontSize=26,
    leading=30,
    textColor=colors.HexColor('#ffffff'),
    spaceAfter=6
)

subtitle_style = ParagraphStyle(
    'DocSubTitle',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=13,
    leading=17,
    textColor=colors.HexColor('#00e5d4'),
    spaceAfter=14
)

section_title_style = ParagraphStyle(
    'SectionTitle',
    parent=styles['Heading2'],
    fontName='Helvetica-Bold',
    fontSize=16,
    leading=20,
    textColor=colors.HexColor('#ffffff'),
    spaceAfter=4
)

category_style = ParagraphStyle(
    'CategoryBadge',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=9,
    leading=11,
    textColor=colors.HexColor('#00e5d4'),
    spaceAfter=2
)

body_style = ParagraphStyle(
    'BodyTextCustom',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=10,
    leading=14,
    textColor=colors.HexColor('#cbd5e1'),
    spaceAfter=8
)

bold_lead = ParagraphStyle(
    'BoldLead',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=10.5,
    leading=14,
    textColor=colors.HexColor('#38bdf8'),
    spaceAfter=4
)

story = []

# -------------------------------------------------------------
# PAGE 1: TITLE SLIDE
# -------------------------------------------------------------
story.append(Paragraph("AUTONOMOUS HIGH-ALTITUDE PASSIVE SOLAR PLATFORM", category_style))
story.append(Paragraph("SHELTRIX — 2026 Climate Digital Twin", title_style))
story.append(Paragraph("Zero-Emission Thermal Simulation & Generative Engineering Platform for Extreme Himalayan Altitudes", subtitle_style))

cover_data = [
    [
        Paragraph("""
        <b>Author & System Architect:</b> Bhaskar Shah<br/>
        <b>Live Production Application:</b> <font color="#00e5d4">https://sheltrix-ai.vercel.app</font><br/>
        <b>GitHub Codebase:</b> <font color="#38bdf8">https://github.com/BhaskarShah05/SHELTRIX</font><br/><br/>
        <b>Mission Summary:</b><br/>
        SHELTRIX couples satellite solar radiation intelligence (NASA POWER + Open-Meteo) with high-aperture direct solar gain and <b>BioPCM™ phase-change latent heat buffering</b> to sustain interior human comfort at <b>+19.4°C</b> during brutal <b>-17.2°C</b> Himalayan nights with <b>zero fossil auxiliary fuel consumption</b>.
        """, body_style),
        Image(os.path.join(PUBLIC_ASSETS, 'futuristic-shelter-1.jpg'), width=4.5 * inch, height=3.0 * inch)
    ]
]
t_cover = Table(cover_data, colWidths=[5.0 * inch, 4.8 * inch])
t_cover.setStyle(TableStyle([
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#0b1830')),
    ('BOX', (0,0), (-1,-1), 1.5, colors.HexColor('#00e5d4')),
    ('ROUNDEDCORNERS', [12, 12, 12, 12]),
    ('TOPPADDING', (0,0), (-1,-1), 16),
    ('BOTTOMPADDING', (0,0), (-1,-1), 16),
    ('LEFTPADDING', (0,0), (-1,-1), 18),
    ('RIGHTPADDING', (0,0), (-1,-1), 18),
]))
story.append(t_cover)
story.append(PageBreak())

# -------------------------------------------------------------
# PAGE 2: 1) PROBLEM STATEMENT & 2) SOLUTION
# -------------------------------------------------------------
story.append(Paragraph("01. EXECUTIVE BRIEFING", category_style))
story.append(Paragraph("1) Problem Statement & 2) The SHELTRIX Solution", section_title_style))
story.append(Spacer(1, 0.1 * inch))

col1_content = [
    Paragraph("🔴 PROBLEM STATEMENT", bold_lead),
    Paragraph("• <b>Sub-Zero Nighttime Extremes:</b> Winter temperatures in Leh, Ladakh and Siachen plunge to -15°C to -40°C with thin atmosphere (55 kPa), causing severe hypothermia hazards.", body_style),
    Paragraph("• <b>Extreme Diurnal Swings:</b> Clear skies cause severe radiant cooling, creating >25°C swings within 12 hours.", body_style),
    Paragraph("• <b>Logistics Vulnerability:</b> Over 60% of winter logistics budgets are spent transporting kerosene and diesel over snow-blocked mountain passes.", body_style),
    Paragraph("• <b>Carbon Monoxide Deaths:</b> Bukharis cause deadly indoor toxic fumes and respiratory illnesses in sealed high-altitude quarters.", body_style),
    Paragraph("• <b>Blind Static Design:</b> Ignored >1000 W/m² peak Himalayan sunshine (>300 sunny days/year).", body_style)
]

col2_content = [
    Paragraph("🟢 THE SHELTRIX SOLUTION", bold_lead),
    Paragraph("• <b>Direct Solar Harvesting:</b> Captures +33.3 kWh/day through high-SHGC triple krypton glazed south facades.", body_style),
    Paragraph("• <b>BioPCM™ Latent Enthalpy Buffer:</b> Absorbs daytime heat and releases 180 kJ/kg latent heat at 21°C isothermal transition, stabilizing nights.", body_style),
    Paragraph("• <b>Transient Lumped ODE Solver:</b> Continuous forward numerical integration solving C_eff * dT/dt.", body_style),
    Paragraph("• <b>Triple-Tier External APIs:</b> Live Open-Meteo Solar DNI + NASA POWER CERES validation + 100Hz MQTT IoT telemetry.", body_style),
    Paragraph("• <b>100% Zero-Emission Habitat:</b> Complete elimination of fossil fuels with zero carbon footprint.", body_style)
]

p2_table = Table([[col1_content, col2_content]], colWidths=[4.85 * inch, 4.85 * inch])
p2_table.setStyle(TableStyle([
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('BACKGROUND', (0,0), (0,0), colors.HexColor('#0f1b33')),
    ('BACKGROUND', (1,0), (1,0), colors.HexColor('#0c2238')),
    ('BOX', (0,0), (0,0), 1.2, colors.HexColor('#f43f5e')),
    ('BOX', (1,0), (1,0), 1.2, colors.HexColor('#00e5d4')),
    ('ROUNDEDCORNERS', [10, 10, 10, 10]),
    ('TOPPADDING', (0,0), (-1,-1), 12),
    ('BOTTOMPADDING', (0,0), (-1,-1), 12),
    ('LEFTPADDING', (0,0), (-1,-1), 14),
    ('RIGHTPADDING', (0,0), (-1,-1), 14),
]))
story.append(p2_table)
story.append(PageBreak())

# -------------------------------------------------------------
# PAGE 3: 3) FLOW OF SOLUTION & SYSTEM ARCHITECTURE
# -------------------------------------------------------------
story.append(Paragraph("02. ENGINEERING FLOW & ARCHITECTURE", category_style))
story.append(Paragraph("3) Flow of Solution: 5-Step Pipeline & Closed-Loop Architecture", section_title_style))
story.append(Spacer(1, 0.08 * inch))

if os.path.exists(os.path.join(ASSETS_DIR, 'diagram_system_architecture.png')):
    story.append(Image(os.path.join(ASSETS_DIR, 'diagram_system_architecture.png'), width=9.8 * inch, height=4.2 * inch))

story.append(PageBreak())

# -------------------------------------------------------------
# PAGE 4: 4) DETAILED TECH STACK
# -------------------------------------------------------------
story.append(Paragraph("03. IMPLEMENTATION ARCHITECTURE", category_style))
story.append(Paragraph("4) Detailed Tech Stack & Modular Microservice Separation", section_title_style))
story.append(Spacer(1, 0.1 * inch))

tech_data = [
    [
        Paragraph("<b>LAYER</b>", bold_lead),
        Paragraph("<b>CORE TECHNOLOGIES</b>", bold_lead),
        Paragraph("<b>TECHNICAL SPECIFICATIONS & ROLE</b>", bold_lead)
    ],
    [
        Paragraph("<b>Frontend Client</b>", body_style),
        Paragraph("React 18.3, Vite 8, Vanilla CSS, Apple SF Pro", body_style),
        Paragraph("Component lifecycle, responsive state, ultra-transparent crystal glassmorphism, <300ms HMR builds.", body_style)
    ],
    [
        Paragraph("<b>3D Graphics</b>", body_style),
        Paragraph("Three.js (WebGL), OrbitControls, Shaders", body_style),
        Paragraph("Procedural 3D shelter geometry, south glazing specular refraction, 24-hour sun altitude & azimuth dial.", body_style)
    ],
    [
        Paragraph("<b>Analytics & Data</b>", body_style),
        Paragraph("Chart.js, React-ChartJS-2", body_style),
        Paragraph("24-hour dual-curve temperature profile, 5-component heat balance bar charts with frosted backplates.", body_style)
    ],
    [
        Paragraph("<b>Backend Solver</b>", body_style),
        Paragraph("Node.js, Express 4.21, CORS", body_style),
        Paragraph("Transient lumped-capacitance ODE solver (C_eff * dT/dt), BioPCM™ latent enthalpy piecewise modeling.", body_style)
    ],
    [
        Paragraph("<b>Optimization AI</b>", body_style),
        Paragraph("Multi-Objective Genetic Algorithm", body_style),
        Paragraph("Evaluates 128 architectural variations with multi-parameter chromosome crossover, mutation & Pareto ranking.", body_style)
    ],
    [
        Paragraph("<b>External APIs</b>", body_style),
        Paragraph("Open-Meteo, NASA POWER, MQTT TLSv1.3", body_style),
        Paragraph("Real-time DNI irradiance, geocoding, CERES satellite validation benchmark, 100Hz IoT telemetry stream.", body_style)
    ],
    [
        Paragraph("<b>Infrastructure</b>", body_style),
        Paragraph("Vercel Serverless Edge, GitHub Monorepo", body_style),
        Paragraph("Zero-install web application, global CDN edge caching, continuous production deployment.", body_style)
    ]
]

t_tech = Table(tech_data, colWidths=[1.8 * inch, 3.2 * inch, 4.8 * inch])
t_tech.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0c2545')),
    ('TEXTCOLOR', (0,0), (-1,0), colors.HexColor('#00e5d4')),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#1e3a5f')),
    ('BACKGROUND', (0,1), (-1,-1), colors.HexColor('#08152c')),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('TOPPADDING', (0,0), (-1,-1), 5),
    ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ('LEFTPADDING', (0,0), (-1,-1), 8),
    ('RIGHTPADDING', (0,0), (-1,-1), 8),
]))
story.append(t_tech)
story.append(PageBreak())

# -------------------------------------------------------------
# PAGE 5: 5) UNIQUE SELLING PROPOSITIONS (USPs)
# -------------------------------------------------------------
story.append(Paragraph("04. COMPETITIVE ADVANTAGES", category_style))
story.append(Paragraph("5) Unique Selling Propositions (USPs)", section_title_style))
story.append(Spacer(1, 0.1 * inch))

usp_data = [
    [
        Paragraph("<b>☀️ 1. Autonomous Zero-Energy Thermal Equilibrium</b><br/><font color='#cbd5e1'>Sustains +19.4°C indoor comfort during -17.2°C ambient nights with 0 auxiliary fossil heating, eliminating fuel transport.</font>", body_style),
        Paragraph("<b>🧬 2. BioPCM™ Phase-Change Latent Storage</b><br/><font color='#cbd5e1'>180 kJ/kg latent heat capacity at 21°C isothermal transition absorbs peak solar energy and releases heat during night freeze.</font>", body_style)
    ],
    [
        Paragraph("<b>🌐 3. Triple-Tier External API Ecosystem</b><br/><font color='#cbd5e1'>Live Open-Meteo Solar DNI & Geocoding + NASA POWER satellite validation benchmark + 100Hz MQTT TLSv1.3 IoT telemetry.</font>", body_style),
        Paragraph("<b>🎮 4. Real-Time 3D Spatial Solar Dial Studio</b><br/><font color='#cbd5e1'>Interactive Three.js 3D studio projecting continuous solar altitude, azimuth angles, and sun rays relative to True South.</font>", body_style)
    ],
    [
        Paragraph("<b>⚡ 5. AI Genetic Multi-Objective Optimizer</b><br/><font color='#cbd5e1'>Evaluates 128 architectural candidates balancing comfort, solar harvest, and zero deficit with 1-click hot-swap to 3D geometry.</font>", body_style),
        Paragraph("<b>💎 6. 2026 Crystal Glassmorphism Experience</b><br/><font color='#cbd5e1'>High-definition 2K landscape backdrop, true edge-to-edge 4K video launch intro, SF Pro typography, and dual light/dark modes.</font>", body_style)
    ]
]

t_usp = Table(usp_data, colWidths=[4.85 * inch, 4.85 * inch])
t_usp.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#091a38')),
    ('GRID', (0,0), (-1,-1), 1.0, colors.HexColor('#00e5d4')),
    ('ROUNDEDCORNERS', [8, 8, 8, 8]),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('TOPPADDING', (0,0), (-1,-1), 10),
    ('BOTTOMPADDING', (0,0), (-1,-1), 10),
    ('LEFTPADDING', (0,0), (-1,-1), 12),
    ('RIGHTPADDING', (0,0), (-1,-1), 12),
]))
story.append(t_usp)
story.append(PageBreak())

# -------------------------------------------------------------
# PAGE 6: THERMAL EVIDENCE & ENERGY BALANCE
# -------------------------------------------------------------
story.append(Paragraph("05. PHYSICS ENGINE VALIDATION", category_style))
story.append(Paragraph("Engineering Evidence: 24-Hour Diurnal Equilibrium & Energy Balance", section_title_style))
story.append(Spacer(1, 0.08 * inch))

chart_data = [
    [
        Image(os.path.join(ASSETS_DIR, 'chart_thermal_equilibrium.png'), width=4.8 * inch, height=3.9 * inch),
        Image(os.path.join(ASSETS_DIR, 'chart_energy_balance.png'), width=4.8 * inch, height=3.9 * inch)
    ]
]
t_charts = Table(chart_data, colWidths=[4.9 * inch, 4.9 * inch])
t_charts.setStyle(TableStyle([
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#07132b')),
    ('BOX', (0,0), (-1,-1), 1.2, colors.HexColor('#00e5d4')),
    ('ROUNDEDCORNERS', [10, 10, 10, 10]),
    ('TOPPADDING', (0,0), (-1,-1), 8),
    ('BOTTOMPADDING', (0,0), (-1,-1), 8),
    ('LEFTPADDING', (0,0), (-1,-1), 8),
    ('RIGHTPADDING', (0,0), (-1,-1), 8),
]))
story.append(t_charts)
story.append(PageBreak())

# -------------------------------------------------------------
# PAGE 7: 6) FEASIBILITY & COMPETITOR BENCHMARK
# -------------------------------------------------------------
story.append(Paragraph("06. MARKET & FEASIBILITY", category_style))
story.append(Paragraph("6) Feasibility Analysis & Competitor Benchmark Matrix", section_title_style))
story.append(Spacer(1, 0.08 * inch))

comp_data = [
    [
        Paragraph("<b>METRIC / FEATURE</b>", bold_lead),
        Paragraph("<b>ARCTIC PREFAB BUNKERS</b>", bold_lead),
        Paragraph("<b>TRADITIONAL MUD PASSIVE</b>", bold_lead),
        Paragraph("<b>SHELTRIX 2026 (WINNER)</b>", bold_lead)
    ],
    [
        Paragraph("<b>Heating Source</b>", body_style),
        Paragraph("Diesel Generator / Bukhari", body_style),
        Paragraph("Passive Sensible Mud Mass", body_style),
        Paragraph("<font color='#00e5d4'><b>Autonomous Solar + BioPCM™</b></font>", body_style)
    ],
    [
        Paragraph("<b>Fuel Consumption</b>", body_style),
        Paragraph("20–40 Liters/day ($30–$60/day)", body_style),
        Paragraph("Zero fuel", body_style),
        Paragraph("<font color='#00e5d4'><b>0 Liters/day (Zero Fossil Fuel)</b></font>", body_style)
    ],
    [
        Paragraph("<b>Diurnal Stability</b>", body_style),
        Paragraph("Erratic (Overheats / Freezes)", body_style),
        Paragraph("Large Day/Night Swings (~12°C)", body_style),
        Paragraph("<font color='#00e5d4'><b>Flat 18°C–24°C Comfort Envelope</b></font>", body_style)
    ],
    [
        Paragraph("<b>Real-Time 3D Studio</b>", body_style),
        Paragraph("None", body_style),
        Paragraph("None", body_style),
        Paragraph("<font color='#00e5d4'><b>Interactive Three.js Sun Dial</b></font>", body_style)
    ],
    [
        Paragraph("<b>Live Satellite APIs</b>", body_style),
        Paragraph("None", body_style),
        Paragraph("None", body_style),
        Paragraph("<font color='#00e5d4'><b>Open-Meteo + NASA POWER</b></font>", body_style)
    ],
    [
        Paragraph("<b>IoT Digital Twin</b>", body_style),
        Paragraph("Manual logs", body_style),
        Paragraph("None", body_style),
        Paragraph("<font color='#00e5d4'><b>100Hz MQTT TLSv1.3 Sensor Stream</b></font>", body_style)
    ],
    [
        Paragraph("<b>AI Optimization</b>", body_style),
        Paragraph("None", body_style),
        Paragraph("Trial and error", body_style),
        Paragraph("<font color='#00e5d4'><b>Genetic Pareto Optimizer (128 variants)</b></font>", body_style)
    ]
]

t_comp = Table(comp_data, colWidths=[2.2 * inch, 2.4 * inch, 2.4 * inch, 2.8 * inch])
t_comp.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0c2545')),
    ('TEXTCOLOR', (0,0), (-1,0), colors.HexColor('#00e5d4')),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#1e3a5f')),
    ('BACKGROUND', (0,1), (-1,-1), colors.HexColor('#08152c')),
    ('BACKGROUND', (3,1), (3,-1), colors.HexColor('#0b2a4a')),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('TOPPADDING', (0,0), (-1,-1), 5),
    ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ('LEFTPADDING', (0,0), (-1,-1), 8),
    ('RIGHTPADDING', (0,0), (-1,-1), 8),
]))
story.append(t_comp)
story.append(PageBreak())

# -------------------------------------------------------------
# PAGE 8: 7) RESEARCH & PEER-REVIEWED REFERENCES
# -------------------------------------------------------------
story.append(Paragraph("07. SCIENTIFIC FOUNDATIONS", category_style))
story.append(Paragraph("7) Research, Literature & Peer-Reviewed References", section_title_style))
story.append(Spacer(1, 0.08 * inch))

ref_data = [
    [
        Paragraph("<b>[1] Duffie, J. A., & Beckman, W. A. (2020).</b> <i>Solar Engineering of Thermal Processes, Photovoltaics and Wind</i> (5th ed.). Wiley.<br/>"
                  "<b>Application in SHELTRIX:</b> Governs the solar declination, equation of time, solar azimuth, and altitude algorithms powering the 3D Sun Ray Tracker.", body_style)
    ],
    [
        Paragraph("<b>[2] NASA Langley Research Center — POWER Project (2026).</b> <i>Prediction of Worldwide Energy Resources.</i><br/>"
                  "<b>Application in SHELTRIX:</b> Ingests ALLSKY_SFC_SW_DWN satellite solar radiation benchmarks for NASA validation of real-time Open-Meteo DNI data.", body_style)
    ],
    [
        Paragraph("<b>[3] Phase Change Solutions (2024).</b> <i>BioPCM™ Technical Specifications and Enthalpy Profiles.</i><br/>"
                  "<b>Application in SHELTRIX:</b> Formulation of the isothermal latent heat storage model at 21°C transition with 180 kJ/kg latent heat capacity.", body_style)
    ],
    [
        Paragraph("<b>[4] Wangchuk, S. (Himalayan Institute of Alternatives, Ladakh — HIAL).</b> <i>Passive Solar Heated Buildings in Cold Deserts.</i><br/>"
                  "<b>Application in SHELTRIX:</b> Benchmarks high-altitude thermal envelopes, Trombe wall composite matrices, and south glazing orientation.", body_style)
    ],
    [
        Paragraph("<b>[5] ASHRAE Standard 55-2023.</b> <i>Thermal Environmental Conditions for Human Occupancy.</i><br/>"
                  "<b>Application in SHELTRIX:</b> Governs human comfort bounds (18.0°C - 24.0°C) used in the Genetic Optimizer's multi-objective fitness function.", body_style)
    ]
]

t_ref = Table(ref_data, colWidths=[9.8 * inch])
t_ref.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#08162e')),
    ('GRID', (0,0), (-1,-1), 1.0, colors.HexColor('#00e5d4')),
    ('ROUNDEDCORNERS', [8, 8, 8, 8]),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('TOPPADDING', (0,0), (-1,-1), 6),
    ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ('LEFTPADDING', (0,0), (-1,-1), 10),
    ('RIGHTPADDING', (0,0), (-1,-1), 10),
]))
story.append(t_ref)

doc.build(story, onFirstPage=draw_background, onLaterPages=draw_background)
print(f"Presentation PDF successfully built at: {pdf_path}")
