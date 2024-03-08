import React, { useState } from "react";
import snt from "./snt.png";
const Demandcreating = () => {
  const [formValues, setFormValues] = useState({
    number: "",
    date: "",
    unit: "NOS",
    quantity: "",
    consignee: "",
    consigneeOfficer: "",
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormValues({ ...formValues, [name]: value });
  };

  const handleSubmit = () => {
    console.log("Form Values:", formValues);
  };

  return (
    <div className="flex items-center m-10 justify-evenly">
      <div>
        <h1 className="font-bold text-2xl text-white mb-10">
          Request the <span className="text-yellow-300">Demands </span>here{" "}
          <span className="text-blue-500">.</span>
        </h1>
        <input
          type="name"
          name="name"
          id="name"
          placeholder="Name"
          value={formValues.number}
          onChange={handleChange}
          className="kaza outline-none focus:p-7 transition-all  text-white ml-16 border-black p-4"
          style={{ backgroundColor: "#1a202c" }}
        />
        <div>
          <div className=" m-5">
            <input
              type="number"
              name="number"
              id="number"
              placeholder="Number"
              value={formValues.number}
              onChange={handleChange}
              className="kaza outline-none focus:p-7 transition-all  text-white ml-10 border-black p-4"
              style={{ backgroundColor: "#1a202c" }}
            />
            <input
              type="date"
              name="date"
              id="date"
              placeholder="Date"
              value={formValues.date}
              onChange={handleChange}
              className="kaza outline-none text-white ml-10 border-black p-4"
              style={{ backgroundColor: "#1a202c" }}
            />
          </div>

          <div className="m-5">
            <input
              type="number"
              name="quantity"
              id="quantity"
              placeholder="QUANTITY"  
              value={formValues.quantity}
              onChange={handleChange}
              className="kaza focus:p-7 outline-none text-white ml-10 border-black p-4"
              style={{ backgroundColor: "#1a202c" }}
            />
            <select
              name="unit"
              id="unit"
              value={formValues.unit}
              onChange={handleChange}
              className="kaza outline-none focus:p-7 transition-all  text-white ml-10 border-black p-4"
              style={{ backgroundColor: "#1a202c" }}
            >
              <option value="NOS">NOS</option>
            </select>
          </div>

          <div className="m-5">
            <input
              type="text"
              name="consignee"
              id="consignee"
              placeholder="CONSIGNEE"
              value={formValues.consignee}
              onChange={handleChange}
              className="kaza outline-none focus:p-7 transition-all  text-white ml-10 border-black p-4"
              style={{ backgroundColor: "#1a202c" }}
            />{" "}
            <input
              type="text"
              name="consigneeOfficer"
              id="consigneeOfficer"
              placeholder="CON.OFFICER"
              value={formValues.consigneeOfficer}
              onChange={handleChange}
              className="kaza focus:p-7 outline-none transition-all text-white ml-10 border-black p-4"
              style={{ backgroundColor: "#1a202c" }}
            />
          </div>
          <div className="ml-5">
            <input
              type="text"
              name="consignee"
              id="consignee"
              placeholder="CONSIGNEE Code"
              value={formValues.consignee}
              onChange={handleChange}
              className="kaza outline-none focus:p-7 transition-all  text-white ml-10 border-black p-4"
              style={{ backgroundColor: "#1a202c" }}
            />{" "}
            <input
              type="text"
              name="consignee"
              id="consignee"
              placeholder="INDENT Code"
              value={formValues.consignee}
              onChange={handleChange}
              className="kaza outline-none focus:p-7 transition-all  text-white ml-10 border-black p-4"
              style={{ backgroundColor: "#1a202c" }}
            />
          </div>
          <div className="m-5">
            <input
              type="text"
              name="consignee"
              id="consignee"
              placeholder="Allocation NUMBER"
              value={formValues.consignee}
              onChange={handleChange}
              className="kaza outline-none focus:p-7 transition-all  text-white ml-10 border-black p-4"
              style={{ backgroundColor: "#1a202c" }}
            />
            <input
              type="text"
              name="consignee"
              id="consignee"
              placeholder="ACCOUNTS UNIT"
              value={formValues.consignee}
              onChange={handleChange}
              className="kaza outline-none focus:p-7 transition-all  text-white ml-10 border-black p-4"
              style={{ backgroundColor: "#1a202c" }}
            />
          </div>
          <div className="m-5">
            <button
              onClick={handleSubmit}
              className="kaza ml-10 p-4 transition-all px-10 bg-yellow-400 font-bold rounded-md hover:shadow-lg hover:bg-yellow-500"
            >
              Submit
            </button>
          </div>
        </div>
      </div>
      <div className="w-48 ">
        <img src={snt} alt="snsst" />
      </div>
    </div>
  );
};

export default Demandcreating;
