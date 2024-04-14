import React from 'react'
import { createPortal } from 'react-dom';
import {motion} from 'framer-motion'
const Modal = ({children, onClose, title}) => {
    return createPortal(
      <>
        <div className="fixed top-0 left-0 w-full z-5 bg-backdrop h-full" onClick={onClose} />
        <motion.dialog 
          variants={{
            hidden: {opacity:0, y:-30},
            show: {opacity:1, y:0}
          }}
          initial="hidden"
          animate="show"
          exit="hidden"
          open 
          className="flex flex-col top-[250px] gap-[10px] rounded-[6px] m-auto p-8 z-10">
          <h2 className='text-[20px]'>{title}</h2>
          {children}
        </motion.dialog>
      </>,
      document.getElementById('modal')
    );
}

export default Modal