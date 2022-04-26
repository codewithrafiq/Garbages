import React, { useEffect, useState } from "react";
import { baseUrl } from "../env";
import "leaflet/dist/leaflet.css";
import { MapContainer, GeoJSON, TileLayer, LayersControl } from "react-leaflet";

const MYMap = () => {
  const [geoData, setGeoData] = useState(null);
  useEffect(() => {
    fetch(`${baseUrl}/country_data/`, {
      method: "GET",
    })
      .then((res) => res.json())
      .then((data) => {
        console.log(data);
        setGeoData(data);
      });
  }, []);
  return (
    <div>
      <h1 style={{ textAlign: "center" }}>Map</h1>
      <MapContainer style={{ height: "80vh" }} zoom={2} center={[20, 100]}>
        <TileLayer
          attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />
        <GeoJSON key={geoData} data={geoData} />
      </MapContainer>
    </div>

  );
};

export default MYMap;
