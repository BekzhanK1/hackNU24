import {configureStore} from '@reduxjs/toolkit'
import { createSlice } from '@reduxjs/toolkit'

const authSlice = createSlice({
    name: 'auth',
    initialState: {
        isAuth: false
    },
    reducers: {
        login(state){
            state.isAuth = true;
        },
        logout(state){
            state.isAuth = false;
        }
    }
})

const currentShopSlice = createSlice({
    name: 'shop',
    initialState: {
        city: '',
        name: '',
        type: ''
    },
    reducers: {
        setData(state, action){
            for (const key of Object.keys(action.payload)){
                state[key] = action.payload[key]
            }
        },
        reset(state){
            state = {}
        },
        resetKey(state,action){
            state[action.payload] = ""
        }
    }
})


export const authActions = authSlice.actions;
export const currentShopActions = currentShopSlice.actions

const store = configureStore({
    reducer: {
        auth: authSlice.reducer,
        currentShop: currentShopSlice.reducer
    }
})

export default store;