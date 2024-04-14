import React from 'react'
import {createBrowserRouter, RouterProvider} from 'react-router-dom'
import LoginSignup from './Components/LoginSignup'
import Layout from './Components/Layout'
import Cards from './Components/Cards'
import CheckShop from './Components/CheckShop'
import History from './Components/History'
import { handleMap } from './Components/CheckShop'
import AddCard from './Components/AddCard'
const router = createBrowserRouter([
  {
    path: '/',
    element: <Layout/>,
    children: [
      {
        path: '/login',
        element: <LoginSignup option="login"/>
      },
      {
        path: '/signup',
        element: <LoginSignup option="signup"/>
      },
      {
        path: '/cards',
        element: <Cards/>,
        children:[
          {
            path:'add-card',
            element: <AddCard/>
          }
        ]
      },
      {
        path: '/check-shop',
        element: <CheckShop/>,
        loader: () =>handleMap()
      },
      {
        path: '/history',
        element: <History/>
      }
    ]
  }
])

const App = () => {
  return (
    <RouterProvider router={router}>
      <div>App</div>
    </RouterProvider>
  )
}

export default App
