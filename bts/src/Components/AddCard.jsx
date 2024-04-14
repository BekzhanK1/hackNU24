import React,{useState} from 'react'
import Modal from './Modal'
import { useNavigate } from 'react-router'
import CreditCardForm from './CreditCardComponent'

const AddCard = () => {

  const [state, setState] = useState({
    number: '',
    expiry: '',
    cvc: '',
    name: '',
    focus: '',
  });

  console.log(1234)

  const handleInputChange = (evt) => {
    const { name, value } = evt.target;
    
    setState((prev) => ({ ...prev, [name]: value }));
  }

  const handleInputFocus = (evt) => {
    setState((prev) => ({ ...prev, focus: evt.target.name }));
  }

  const navigate = useNavigate()

  function cancelHandler(){
    navigate('..');
  }

  function handleAuth(e){
    e.preventDefault()
  }
  return (
    <Modal title="Adding card" onClose={cancelHandler}>
      <CreditCardForm/>
    </Modal>
  )
}

export default AddCard