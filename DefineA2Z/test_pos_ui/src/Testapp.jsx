
import React from 'react';

const data =[{
    "title": "Food",
    "path": "/root",
    "children": [{
        "title": "Veg",
        "path": "/root/Food",
        "children": [{
            "title": "Carrot",
            "path": "/root/Food/Veg",
            "children": [{
                "title": "Ooty carrot",
                "path": "/root/Food/Veg/Brinjal",
                "children": [
                    {
                        "title": "title 1",
                        "path": "/root/Food/Veg/Brinjal",
                        "children": []
                    },{
                        "title": "title 2",
                        "path": "/root/Food/Veg/Brinjal",
                        "children": []
                    }
                ]
            }]
        }]
    }]
}, {
    "title": "Cloths",
    "path": "/root",
    "children": [{
        "title": "T shirt",
        "path": "/root/Cloths",
        "children": []
    }, {
        "title": "Shirt",
        "path": "/root/Cloths",
        "children": []
    }]
}]


const MyComponent = ({data}) => {
   return (
    <ul>
      {data.map((m, index) => {
        return (<li key={index}>
          {m.title}
          {m.children && <MyComponent data={m.children} />}
        </li>);
      })}
    </ul>
  );
}



const Testapp = () => {
  return <div>
    <MyComponent data={data} />
  </div>;
};

export default Testapp;
