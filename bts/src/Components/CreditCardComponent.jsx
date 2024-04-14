import React, { useState } from "react";
import Cards from "react-credit-cards-2";
import "react-credit-cards-2/dist/es/styles-compiled.css";
const CreditCardForm = () => {
  const [state, setState] = useState({
    number: "",
    name: "",
    expiry: "",
    cvc: "",
    name: "",
    focus: "",
    bank_name: ""
  });
  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setState((prev) => ({ ...prev, [name]: value }));
  };
  const handleInputFocus = (e) => {
    setState((prev) => ({ ...prev, focus: e.target.name }));
  };

  const handleSubmit = async (e) =>{
    e.preventDefault()
    await fetch('')
  }
  return (
    <>
    <div className="flex justify-center items-center gap-[28px]">
        
        <div className="flex flex-col">
        <Cards
            number={state.number}
            expiry={state.expiry}
            cvc={state.cvc}
            name={state.name}
            focused={state.focus}
        />
        <input
              type="text"
              name="bank_name"
              className="border-stone-400 border-[1.5px] p-2 rounded-md mt-4"
              placeholder="Bank Name"
              onChange={handleInputChange}
              onFocus={handleInputFocus}
              required
        />
        </div>
      
      <div className="">
        <form>
          <div className="mb-3">
            <input
              type="number"
              name="number"
              className="border-stone-400 border-[1.5px] p-2 rounded-md"
              placeholder="Card Number"
              value={state.number}
              onChange={handleInputChange}
              onFocus={handleInputFocus}
              required
            />
          </div>
          <div className="mb-3">
            <input
              type="text"
              name="name"
              className="border-stone-400 border-[1.5px] p-2 rounded-md"
              placeholder="Name"
              onChange={handleInputChange}
              onFocus={handleInputFocus}
              required
            />
          </div>
            <div className="w-full mb-3 flex justify-between">
              <input
                type="number"
                name="expiry"
                className="border-stone-400 border-[1.5px] p-2 rounded-md w-[80px]"
                placeholder="Valid Thru"
                pattern="\d\d/\d\d"
                value={state.expiry}
                onChange={handleInputChange}
                onFocus={handleInputFocus}
                required
              />
              <input
                type="number"
                name="cvc"
                className=" border-stone-400 border-[1.5px] p-2 rounded-md w-[100px]"
                placeholder="CVC"
                pattern="\d{3,4}"
                value={state.cvc}
                onChange={handleInputChange}
                onFocus={handleInputFocus}
                required
              />
            </div>
            <div className="grid justify-center">
                <button className="w-[200px] bg-blue-500 text-white p-2" onClick={()=>handleSubmit()}>Confirm</button>
            </div>
        </form>
      </div>
    </div>
    </>
  );
};
export default CreditCardForm;