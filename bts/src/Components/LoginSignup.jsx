import React, { useEffect, useState } from 'react'
import {NavLink, useLocation} from 'react-router-dom'
// import { AuthContext } from '../Context/AuthContext';
// import { useContext } from 'react';
const LoginSignup = (props) => {

  const currentLocation = props.option;
  let content;

  //const {loginHandler} = useContext(AuthContext);

  async function handleAuth(event){
    event.preventDefault();
    const fd = new FormData(event.target);

    if (fd.has('username')){
      let username = fd.get('username');
      let email = fd.get('email');
      let password = fd.get('password');
      const requestBody = {
        username,
        email,
        password
      }
      let responseData;

      await fetch('http://localhost:4000/signup', {
        method: 'POST',
        headers:{
          'Accept': 'application/json',
          'Content-Type':'application/json'
        },
        body:JSON.stringify(requestBody)
      }).then(response=>response.json()).then(data=>{
        responseData = data;
      });

      if (responseData.success){
        loginHandler(responseData.token);
        window.location.replace('/');
      }else{
        alert(responseData.message);
      }

    }else{
      let email = fd.get('email');
      let password = fd.get('password');

      let responseData;

      const requestBody = {
        email, 
        password
      }

      await fetch('http://localhost:4000/login', {
        method: 'POST',
        headers:{
          'Accept': 'application/json',
          'Content-Type':'application/json'
        },
        body:JSON.stringify(requestBody)
      }).then(response=>response.json()).then(data=>{
        responseData = data;
      });

      if (responseData.success){
        loginHandler(responseData.token);
        window.location.replace('/');
      }else{
        alert(responseData.message);
      }
    }
  }

  if (currentLocation=='signup'){
    content = (
      <div className='w-full flex justify-center items-center h-full'>
        <form className='w-[500px] flex flex-col justify-start items-center bg-white m-auto mt-[100px] px-[100px] pt-[50px] pb-[40px] gap-[25px] rounded-[20px] shadow-md' onSubmit={handleAuth}>
          <h4 className='w-full text-[30px] font-[400]'>Sign Up</h4>
          <input type="text" placeholder='Email Address' name='email' className='w-full flex flex-col p-[20px] text-[16px] shadow-sm'/>
          <input type="text" placeholder='Password' name='password' className='w-full flex flex-col p-[20px] text-[16px] shadow-sm'/>
          <button className='w-full flex flex-col text-[18px] text-white rounded-[16px] shadow-sm bg-blue-500 px-4 py-2'>Continue</button>
          <p className='w-full text-[#ff4141]-600 font-[500] cursor-pointer'>Already have an account? <span><NavLink to='/login' style={{textDecoration:'none'}}>Click here</NavLink></span></p>
          <div className='flex gap-[20px]'>
            <input type="checkbox" className='w-[20px]'/>
            <p className='w-full'>By continuing, I agree to the terms of use & privacy policy.</p>
          </div>
        </form>
      </div>
    )
  }else{
    content = (
      <div className='w-full flex justify-center items-center h-full'>
        <form className='w-[500px] flex flex-col justify-start items-center bg-white m-auto mt-[100px] px-[100px] pt-[50px] pb-[40px] gap-[25px] rounded-[20px] shadow-md' onSubmit={handleAuth}>
          <h4 className='w-full text-[30px] font-[400]'>Login</h4>
          <input type="text" placeholder='Email Address' name='email' className='w-full flex flex-col p-[20px] text-[16px] shadow-sm'/>
          <input type="text" placeholder='Password' name='password' className='w-full flex flex-col p-[20px] text-[16px] shadow-sm'/>
          <button className='w-full flex flex-col text-[18px] text-white rounded-[16px] shadow-sm bg-blue-500 px-4 py-2'>Continue</button>
          <p className='w-full text-[#ff4141]-600 font-[500] cursor-pointer'>Create a new account? <span><NavLink to='/signup' style={{textDecoration:'none'}}>Click here</NavLink></span></p>
          <div className='flex gap-[20px]'>
            <input type="checkbox" className='w-[20px]'/>
            <p className='w-full'>By continuing, I agree to the terms of use & privacy policy.</p>
          </div>
        </form>
      </div>
    )
  }
  return (
    content
  )
}

export default LoginSignup