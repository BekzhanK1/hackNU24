import React, { useEffect,useState } from 'react'
import { Outlet,useLocation } from 'react-router'
import Navbar from './Navbar'
const Layout = () => {
    const location = useLocation();
    const {pathname} = location;

    const [isLogin, setIsLogin] = useState();

    useEffect(()=>{
        if (pathname==isLogin){
            setIsLogin(pathname)
        }
    },[pathname])
    return (
        <>
            <Navbar/>
            <Outlet />
        </>
    )
}

export default Layout