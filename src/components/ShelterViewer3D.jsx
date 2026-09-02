import React, { useEffect, useRef } from 'react';
import * as THREE from 'three';

export default function ShelterViewer3D({ shelter, currentHour = 12 }) {
  const mountRef = useRef(null);

  useEffect(() => {
    const container = mountRef.current;
    if (!container) return;

    const width = container.clientWidth || 400;
    const height = container.clientHeight || 280;

    // Scene setup
    const scene = new THREE.Scene();
    
    // Camera
    const camera = new THREE.PerspectiveCamera(45, width / height, 0.1, 1000);
    camera.position.set(12, 10, 14);
    camera.lookAt(0, 1.5, 0);

    // Renderer with antialiasing and alpha
    const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
    renderer.setSize(width, height);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    renderer.shadowMap.enabled = true;
    renderer.shadowMap.type = THREE.PCFSoftShadowMap;

    while (container.firstChild) {
      container.removeChild(container.firstChild);
    }
    container.appendChild(renderer.domElement);

    // Ambient light
    const ambientLight = new THREE.AmbientLight(0xffffff, 0.75);
    scene.add(ambientLight);

    // Dynamic Sun light based on currentHour & shelter orientation
    const sunLight = new THREE.DirectionalLight(0xfff3d1, 1.8);
    // Sun position calculation
    const sunAngle = ((currentHour - 6) / 12) * Math.PI; // Sunrise at 6, peak at 12, sunset at 18
    const sunY = Math.max(1, Math.sin(sunAngle) * 15);
    const sunX = Math.cos(sunAngle) * 18;
    const sunZ = 12;
    sunLight.position.set(sunX, sunY, sunZ);
    sunLight.castShadow = true;
    sunLight.shadow.mapSize.width = 1024;
    sunLight.shadow.mapSize.height = 1024;
    scene.add(sunLight);

    // Sun Marker Sphere
    const sunGeo = new THREE.SphereGeometry(0.6, 16, 16);
    const sunMat = new THREE.MeshBasicMaterial({ color: 0xffcc00 });
    const sunMesh = new THREE.Mesh(sunGeo, sunMat);
    sunMesh.position.copy(sunLight.position);
    scene.add(sunMesh);

    // Mountainous Ground / Ladakh Terrain
    const groundGeo = new THREE.PlaneGeometry(35, 35, 32, 32);
    const groundMat = new THREE.MeshStandardMaterial({
      color: 0x223048,
      roughness: 0.8,
      metalness: 0.1,
      wireframe: false
    });
    const ground = new THREE.Mesh(groundGeo, groundMat);
    ground.rotation.x = -Math.PI / 2;
    ground.receiveShadow = true;
    scene.add(ground);

    // Ground Grid
    const grid = new THREE.GridHelper(30, 30, 0x00d2c4, 0x1e3a5f);
    grid.position.y = 0.02;
    scene.add(grid);

    // Shelter Group
    const shelterGroup = new THREE.Group();
    scene.add(shelterGroup);

    const L = shelter.length || 6;
    const W = shelter.width || 4;
    const H = shelter.height || 3;

    // Main Shelter Walls
    const wallGeo = new THREE.BoxGeometry(L, H, W);
    const wallMat = new THREE.MeshPhysicalMaterial({
      color: 0xf1f5f9,
      roughness: 0.35,
      metalness: 0.1,
      transmission: 0.25, // Glassmorphism wall aesthetic
      transparent: true,
      opacity: 0.92,
      reflectivity: 0.6
    });
    const wallMesh = new THREE.Mesh(wallGeo, wallMat);
    wallMesh.position.y = H / 2;
    wallMesh.castShadow = true;
    wallMesh.receiveShadow = true;
    shelterGroup.add(wallMesh);

    // Interior Floor
    const floorGeo = new THREE.BoxGeometry(L * 0.96, 0.2, W * 0.96);
    const floorMat = new THREE.MeshStandardMaterial({ color: 0x8b5a2b, roughness: 0.5 });
    const floorMesh = new THREE.Mesh(floorGeo, floorMat);
    floorMesh.position.y = 0.1;
    shelterGroup.add(floorMesh);

    // South Glazing (Solar Window Aperture)
    const windowW = Math.min(L * 0.8, Math.sqrt(shelter.windowArea) * 1.5);
    const windowH = Math.min(H * 0.8, shelter.windowArea / windowW);
    const windowGeo = new THREE.BoxGeometry(windowW, windowH, 0.15);
    const windowMat = new THREE.MeshPhysicalMaterial({
      color: 0x38bdf8,
      transmission: 0.88,
      opacity: 0.75,
      transparent: true,
      roughness: 0.05,
      ior: 1.5
    });
    const windowMesh = new THREE.Mesh(windowGeo, windowMat);
    windowMesh.position.set(0, H / 2, W / 2 + 0.08); // Placed on south face
    shelterGroup.add(windowMesh);

    // Roof (Flat or Pitched)
    if (shelter.roofType === 'pitched') {
      const roofPitchH = 1.2;
      const prismGeo = new THREE.ConeGeometry(Math.max(L, W) * 0.7, roofPitchH, 4);
      const roofMat = new THREE.MeshStandardMaterial({ color: 0x0f172a, roughness: 0.4 });
      const roofMesh = new THREE.Mesh(prismGeo, roofMat);
      roofMesh.position.y = H + roofPitchH / 2;
      roofMesh.rotation.y = Math.PI / 4;
      roofMesh.castShadow = true;
      shelterGroup.add(roofMesh);
    } else {
      const roofGeo = new THREE.BoxGeometry(L + 0.6, 0.3, W + 0.6);
      const roofMat = new THREE.MeshStandardMaterial({ color: 0x1e293b, roughness: 0.3 });
      const roofMesh = new THREE.Mesh(roofGeo, roofMat);
      roofMesh.position.y = H + 0.15;
      roofMesh.castShadow = true;
      shelterGroup.add(roofMesh);
    }

    // Apply Orientation (Azimuth rotation)
    const radAzimuth = ((shelter.orientation - 180) * Math.PI) / 180;
    shelterGroup.rotation.y = radAzimuth;

    // Azimuth Compass Ring
    const compassGeo = new THREE.RingGeometry(L * 0.9, L * 0.95, 32);
    const compassMat = new THREE.MeshBasicMaterial({ color: 0x00d2c4, side: THREE.DoubleSide });
    const compassMesh = new THREE.Mesh(compassGeo, compassMat);
    compassMesh.rotation.x = -Math.PI / 2;
    compassMesh.position.y = 0.05;
    scene.add(compassMesh);

    // Animation Loop (Slow graceful rotation)
    let reqId;
    let clock = new THREE.Clock();

    const animate = () => {
      reqId = requestAnimationFrame(animate);
      const elapsedTime = clock.getElapsedTime();
      // Gentle orbit sway
      camera.position.x = 12 * Math.cos(elapsedTime * 0.08);
      camera.position.z = 12 * Math.sin(elapsedTime * 0.08);
      camera.lookAt(0, 1.5, 0);

      renderer.render(scene, camera);
    };
    animate();

    const handleResize = () => {
      if (!container) return;
      const w = container.clientWidth;
      const h = container.clientHeight;
      camera.aspect = w / h;
      camera.updateProjectionMatrix();
      renderer.setSize(w, h);
    };
    window.addEventListener('resize', handleResize);

    return () => {
      cancelAnimationFrame(reqId);
      window.removeEventListener('resize', handleResize);
      if (container && renderer.domElement) {
        container.removeChild(renderer.domElement);
      }
      renderer.dispose();
    };
  }, [shelter, currentHour]);

  return (
    <div style={{ position: 'relative', width: '100%', height: '100%', minHeight: '320px' }}>
      <div ref={mountRef} style={{ width: '100%', height: '100%', borderRadius: '24px', overflow: 'hidden' }} />
      <div style={{
        position: 'absolute',
        bottom: '12px',
        left: '16px',
        background: 'rgba(15, 23, 42, 0.75)',
        backdropFilter: 'blur(12px)',
        padding: '6px 14px',
        borderRadius: '99px',
        fontSize: '0.72rem',
        color: '#a5f3fc',
        display: 'flex',
        alignItems: 'center',
        gap: '8px',
        border: '1px solid rgba(255, 255, 255, 0.15)'
      }}>
        <span style={{ width: '8px', height: '8px', borderRadius: '50%', background: '#00d2c4', display: 'inline-block' }}></span>
        <span>Three.js Spatial Engine • Azimuth: {shelter.orientation}° • Sun Hour: {currentHour}:00</span>
      </div>
    </div>
  );
}
