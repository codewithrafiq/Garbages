import React from 'react';

import { useSubscription } from 'mqtt-react-hooks';

export default function Status() {
  /* Message structure:
   *  topic: string
   *  message: string
   */
  const { message } = useSubscription([
    'worker_count_ml_topic',
  ]);

  console.log(message);

  return (
    <>
      {/* <div style={{ display: 'flex', flexDirection: 'column' }}>
        <span>{`topic:${message.topic} - message: ${message.message}`}</span>
      </div> */}
      <h1>Hello World</h1>
    </>
  );
}