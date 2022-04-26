import React from "react";
import "@progress/kendo-theme-material/dist/all.css";
import "hammerjs";
import "./App.css";
import {Tabs, Tab, AppBar} from '@material-ui/core'

import Bar from "./components/Bar";
import Line from "./components/Line";




function App() {
  const [value, setValue] = React.useState(0)
  const handleTabs=(e,val)=>{
    console.warn(val)
    setValue(val)
  }
  return (
      <div className="container">
        <h1>Data Visualization</h1>
          <div className="section">
            <>
          <AppBar position="static">
          <Tabs value={value} onChange={handleTabs}>
            <Tab label="Hourly"></Tab>
            <Tab label="Day">
            </Tab>
          </Tabs>
        </AppBar>
        {value === 0 && <Line/>}
        {value === 1 && <Bar/>}
        </>
          </div>
      </div>
  );
}

export default App;