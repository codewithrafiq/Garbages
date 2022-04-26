import {
    Chart,
    ChartSeries,
    ChartSeriesItem,
    ChartValueAxis,
    ChartValueAxisItem,
    ChartCategoryAxis,
    ChartCategoryAxisItem,
    ChartTitle,
    ChartLegend,
    ChartAxisDefaults,
  } from "@progress/kendo-react-charts";
import { COLORS } from "../constants";
import myData from '../data/datas.json';
import React, { useState } from "react";
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";



  export const series = [
    {
      name: "Incoming",
      data: [19, 9, 20],
      color: COLORS.total,
    },
    {
      name: "Purchesed",
      data: [12, 6, 15],
      color: COLORS.pending,
    },
  ];
  
  const times = [];
  const person = [];
  const numbe = [];
  const ids = [];
  for (var i = 0; i < myData.length; i++) {
    times.push(myData[i].time);
    person.push(myData[i].person);
    numbe.push(myData[i].numbe);
    ids.push(myData[i].id);
}
  
  const Line = props => {
    const [startDate, setStartDate] = useState(new Date());
    return (<div>
      <div className="datepick">
      <DatePicker selected={startDate} onChange={(date) => setStartDate(date)} />
      </div>
      
      <Chart pannable zoomable style={{ height: 700 }}>
        {/* <ChartAxisDefaults startAngle={90} /> */}
        <ChartTitle text="Test Data" />
        <ChartLegend position="top" orientation="horizontal" />
        <ChartValueAxis>
          <ChartValueAxisItem title={{ text: "Count" }} min={0} max={30} />
        </ChartValueAxis>
        <ChartCategoryAxis>
          <ChartCategoryAxisItem title={{ text: "Timeline" }} categories={times}  />
        </ChartCategoryAxis>
        <ChartSeries>

        <ChartSeriesItem
              key={ids}
              type="line"
              tooltip={{ visible: true }}
              data={person}
            />

        <ChartSeriesItem
              key={ids}
              type="line"
              tooltip={{ visible: true }}
              data={numbe}
            />

        </ChartSeries>
      </Chart>
      </div>
    );
  };
  
  export default Line;