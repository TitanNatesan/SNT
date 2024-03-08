import React, { useState } from "react";
import snt from "./snt.png";
import axios from "axios";
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

const Demandcreating = () => {
  const [formValues, setFormValues] = useState({
    product: "",
    number: null,
    quantity: null,
    nos: "NOS",
    consignee_name: "",
    consignee_officer: "",
    consignee_code: "",
    demand_code: "",
    allocation_number: "",
    accounts_unit: "",
  });
  const [error, setError] = useState(null);

  const handleChange = (e) => {
    const { id, value } = e.target;
    setFormValues({ ...formValues, [id]: value });
  };

  const handleSubmit = async () => {
    try {
      const response = await axios.post(
        "http://192.168.96.132:8000/DemandRegister/",
        formValues,
        {
          headers: {
            "Content-Type": "application/json",
          },
        }
      );
      console.log("API Response:", response.data);
      toast.success("hi");
    } catch (error) {
      console.error("Error making POST request:", error.response.data);
      setError(error.response.data);
      toast.error("Demand Request doesn't send ");
    }
  };

  return (
    <div className="100vh">
      <div className="flex items-center m-10 justify-evenly overflow-y-hidden">
        <div>
          <h1 className="font-bold text-2xl text-white mb-10">
            Request the <span className="text-yellow-300">Demands </span>here
            <span className="text-blue-500"> .</span>
          </h1>
          <input
            type="name"
            name="product"
            id="product"
            placeholder="Name"
            onChange={handleChange}
            className="kaza outline-none  transition-all  text-white ml-16 border-black p-4"
            style={{ backgroundColor: "#1a202c" }}
          />
        <di >
          <div className=" m-5">
            <input
              type="number"
              name="number"
              id="number"
              placeholder="Number"
              onChange={handleChange}
              className="kaza outline-none  transition-all  text-white ml-10 border-black p-4"
              style={{ backgroundColor: "#1a202c" }}
            />
            <input
              type="date"
              name="date"
              id="date"
              placeholder="Date"
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
              onChange={handleChange}
              className="kaza  outline-none text-white ml-10 border-black p-4"
              style={{ backgroundColor: "#1a202c" }}
            />
            <select
              name="unit"
              id="unit"
              onChange={handleChange}
              className="kaza outline-none  transition-all  text-white ml-10 border-black p-4"
              style={{ backgroundColor: "#1a202c" }}
            >
              <option value="NOS">NOS</option>
            </select>
          </div>

          <div className="m-5">
            <input
              type="text"
              name="consignee_name"
              id="consignee_name"
              placeholder="CONSIGNEE"
              onChange={handleChange}
              className="kaza outline-none  transition-all  text-white ml-10 border-black p-4"
              style={{ backgroundColor: "#1a202c" }}
            />{" "}
            <input
              type="text"
              name="consignee_officer"
              id="consignee_officer"
              placeholder="CON.OFFICER"
              onChange={handleChange}
              className="kaza  outline-none transition-all text-white ml-10 border-black p-4"
              style={{ backgroundColor: "#1a202c" }}
            />
          </div>
          <div className="ml-5">
            <input
              type="text"
              name="consignee"
              id="consignee_code"
              placeholder="CONSIGNEE Code"
              onChange={handleChange}
              className="kaza outline-none  transition-all  text-white ml-10 border-black p-4"
              style={{ backgroundColor: "#1a202c" }}
            />
            <input
              type="text"
              name="consignee"
              id="demand_code"
              placeholder="INDENT Code"
              onChange={handleChange}
              className="kaza outline-none  transition-all  text-white ml-10 border-black p-4"
              style={{ backgroundColor: "#1a202c" }}
            />
          </div>
          <div className="m-5">
            <input
              type="text"
              name="consignee"
              id="allocation_number"
              placeholder="Allocation NUMBER"
              onChange={handleChange}
              className="kaza outline-none  transition-all  text-white ml-10 border-black p-4"
              style={{ backgroundColor: "#1a202c" }}
            />
            <input
              type="text"
              name="consignee"
              id="accounts_unit"
              placeholder="ACCOUNTS UNIT"
              onChange={handleChange}
              className="kaza outline-none  transition-all  text-white ml-10 border-black p-4"
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
        </di>
        
      </div>
      <div className=" h-screen">
        <ToastContainer />
      </div>
    </div>
  </div>
  )
}

export default Demandcreating;