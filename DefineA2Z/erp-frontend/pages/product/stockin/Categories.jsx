import React, { useEffect, useState } from "react";
import axios from "axios";

const Categories = () => {
  const [data, setData] = useState();
  const [id, setId] = useState();
  const [reload, setReload] = useState();
  useEffect(() => {
    console.log("Categories.jsx is loaded");
    axios({
      method: "GET",
      url: "http://localhost:8000/api/products/categories/",
    }).then((response) => {
      console.log(response.data);
      setData(response?.data);
    });
  }, [reload]);
  const name = {};
  const setCatName = (id, namec) => {
    name[id] = namec;
    console.log(name);
  };
  const editCat = (id) => {
    if (name[id] == undefined) {
      alert("Please enter the name of the category");
    } else {
      axios({
        method: "POST",
        url: `http://localhost:8000/api/products/categories/${id}/`,
        data: {
          name: name[id],
        },
        headers: {
          "Content-Type": "application/json",
          Authorization: "Token 2d95e08ff18907b1ad310a7b8727a82e212c50a2",
        },
      }).then((response) => {
        console.log("editCat", response);
        setReload(!reload);
      });
    }
  };
  const deleteCat = (id) => {
    axios({
      method: "DELETE",
      url: `http://localhost:8000/api/products/categories/${id}/`,
      headers: {
        "Content-Type": "application/json",
        Authorization: "Token 2d95e08ff18907b1ad310a7b8727a82e212c50a2",
      },
    }).then((response) => {
      console.log("deleteCat", response);
      setReload(!reload);
    });
  };
  const addCat = (id) => {
    if (name[id] == undefined) {
      alert("Please enter the name of the category");
    } else {
      axios({
        method: "PUT",
        url: "http://localhost:8000/api/products/categories/",
        data: {
          hcat_id: id,
          name: name[id],
        },
        headers: {
          "Content-Type": "application/json",
          Authorization: "Token 2d95e08ff18907b1ad310a7b8727a82e212c50a2",
        },
      }).then((response) => {
        console.log("addCat", response);
        setReload(!reload);
      });
    }
  };
  const MyComponent = ({ data }) => {
    return (
      <ul>
        {data?.map((m, index) => {
          return (
            <li key={index}>
              <div>
                <h3>{m.name}</h3>
                <input
                  onChange={(e) => {
                    setCatName(m.id, e.target.value);
                  }}
                  type="text"
                  value={name[m.id]}
                />
                {console.log("fdddddddddddddddddddddd")}
                {console.log(name[m.id])}
                <input
                  type="button"
                  onClick={(e) => {
                    editCat(m.id);
                  }}
                  value="edit"
                />
                <input type="button" value="delete" />
                <input
                  type="button"
                  onClick={(e) => {
                    addCat(m.id);
                  }}
                  value="add"
                />
                {/* {m.id} */}
              </div>
              {m.sub_categories && <MyComponent data={m.sub_categories} />}
            </li>
          );
        })}
      </ul>
    );
  };

  return (
    <div>
      <h1>Hello This is Categorys Pages</h1>
      <MyComponent data={data} />
    </div>
  );
};

export default Categories;
