import React from 'react'
import CardItem from './CardItem'
import { useState, useEffect } from 'react'
import { createPortal } from 'react-dom'
import Modal from './Modal'
import { Link, useNavigate } from 'react-router-dom'
import { Outlet } from 'react-router-dom'
const Cards = () => {
  const [showModal, setShowModal] = useState(false);
  const [modalMessage, setModalMessage] = useState('Rendered your data well!');
  const [modalTitle, setModalTitle] = useState('Successfully rendered');

  const navigate = useNavigate();

  function showAddCard(){
    //const {error, message, title} = addToCart(id);
    //error ? setModalTitle(error) : setModalTitle(title);
    //setModalMessage(message);
    //setShowModal(true);
    navigate('./add-card')
  }

  return (
    <>
      {showModal && <Modal title={modalTitle} onClose={()=>setShowModal(false)}>
        <p>{modalMessage}</p>
        <button className='text-[16px] text-white p-[10px] w-fit rounded-[20px] cursor-pointer bg-blue-500' onClick={()=>setShowModal(false)}>Accept</button>
      </Modal>}
      <div className='w-full text-center mt-8 flex justify-center'>
        <div className='shadow-md p-8 rounded-md w-[500px] flex justify-center flex-col'>
          <div className='w-full flex justify-between'>
            <h1 className='text-4xl'>My cards</h1>
            <Link className='bg-white shadow-ssm w-12 h-12 rounded-[30px] hover:bg-gray-100' to="add-card">+</Link>
          </div>
          <ul className='p-4 pl-0 flex flex-col gap-4 justify-center'>
            <CardItem/>
            <CardItem/>
            <CardItem/>
            <CardItem/>
          </ul>
        </div>
      </div>
      <Outlet/>
    </>
  )
}

export default Cards