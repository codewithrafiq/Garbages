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
  } from "@progress/kendo-react-charts";
import { COLORS } from "../constants";
import React, { useState } from "react";
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";



  export const series = [
    {
      name: "Incoming",
      data: [19],
      color: COLORS.total,
    },
    {
      name: "Purchased",
      data: [12],
      color: COLORS.pending,
    }
  ];
  
  const categories = ["May 12, 2021"];
  
  const Bar = props => {
    const [startDate, setStartDate] = useState(new Date());
    return (
      <div>
        <div className="datepick">
      <DatePicker selected={startDate} onChange={(date) => setStartDate(date)} />
      </div>
      
      <Chart pannable zoomable style={{ height: 500 }}>
        <ChartTitle text="Test Data" />
        <ChartLegend position="top" orientation="horizontal" />
        <ChartValueAxis>
          <ChartValueAxisItem title={{ text: "Footfall" }} min={0} max={30} />
        </ChartValueAxis>
        <ChartCategoryAxis>
          <ChartCategoryAxisItem categories={categories} />
        </ChartCategoryAxis>
        <ChartSeries>
          {series.map((item, idx) => (
            <ChartSeriesItem
              key={idx}
              type="column"
              tooltip={{ visible: true }}
              data={item.data}
              name={item.name}
            />
          ))}
        </ChartSeries>
      </Chart>
      </div>
    );
  };
  
  export default Bar;