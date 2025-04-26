// frontend/src/components/VesselLayer.jsx

import { useContext, useEffect, useRef } from 'react';
import mapboxgl from 'mapbox-gl';
import { MapContext } from './Map';

export default function VesselLayer({ path, currentIndex }) {
  const map = useContext(MapContext);
  const markerRef = useRef();

  // Add route line once
  useEffect(() => {
    if (!map.getSource('route')) {
      map.addSource('route', {
        type: 'geojson',
        data: {
          type: 'Feature',
          geometry: { type: 'LineString', coordinates: path.map(([lat, lon]) => [lon, lat]) },
        },
      });
      map.addLayer({
        id: 'route-line',
        type: 'line',
        source: 'route',
        paint: { 'line-width': 3 },
      });
    }
  }, [map, path]);

  // Create or update marker
  useEffect(() => {
    const [lat, lon] = path[currentIndex];
    if (!markerRef.current) {
      markerRef.current = new mapboxgl.Marker()
        .setLngLat([lon, lat])
        .addTo(map);
    } else {
      markerRef.current.setLngLat([lon, lat]);
    }
  }, [map, path, currentIndex]);

  return null;
}