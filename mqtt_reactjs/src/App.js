import React from 'react';

import { Connector } from 'mqtt-react-hooks';
import Status from './Status';

export default function App() {
  return (
    <Connector brokerUrl="wss://192.168.1.231:1833">
      <Status />
    </Connector>
  );
}