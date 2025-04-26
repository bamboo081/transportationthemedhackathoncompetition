// frontend/src/components/Map.jsx

import React, { useRef, useEffect, createContext } from 'react';
import mapboxgl from 'mapbox-gl';
import 'mapbox-gl/dist/mapbox-gl.css';

mapboxgl.accessToken = process.env.NEXT_PUBLIC_MAPBOX_TOKEN;

export const MapContext = createContext(null);

export default function Map({ center, children }) {
  const mapContainer = useRef();
  const mapRef = useRef();

  useEffect(() => {
    if (mapRef.current) return; // initialize once
    mapRef.current = new mapboxgl.Map({
      container: mapContainer.current,
      style: 'mapbox://styles/mapbox/light-v10',
      center: [center[1], center[0]],
      zoom: 5,
    });
  }, [center]);

  return (
    <MapContext.Provider value={mapRef.current}>
      <div style={{ width: '100%', height: '100%' }} ref={mapContainer} />
      {mapRef.current && children}
    </MapContext.Provider>
  );
}
