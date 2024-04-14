import React, { useContext, useState,useRef } from 'react'
import { Link } from 'react-router-dom';
const Navbar = function Navbar(){
  const [picked, setPicked] = useState(null);

  let menuRef = useRef();

  function categoryHandler(category){
    setPicked(category);
  }
  return (
    <div className='w-full flex justify-between items-center text-[24px] py-4 shadow shadow-black-md px-20'>
      <div className='flex w-[400px] justify-between'>
        <Link to="/cards">Cards</Link>
        <Link to="/check-shop">Check Shop</Link>
        <Link to="/history">History</Link>
      </div>
      <div className=''>
        <Link to="/login">Login</Link>
      </div>
    </div>

  )
}

export default Navbar