import React from 'react'

const Results = () => {

    
      const navigate = useNavigate()
    
      function cancelHandler(){
        navigate('..');
      }
    
      function handleAuth(e){
        e.preventDefault()
      }
      return (
        <Modal title="Results" onClose={cancelHandler}>
          <div className='w-[400px]'>
            <ul className='flex flex-col justify-center items-center'>
                <li></li>
                <li></li>
                <li></li>
            </ul>
          </div>
        </Modal>
      )
}

export default Results