import React, { useEffect, useState } from 'react'
import {createPortal} from 'react-dom'
import {useDispatch} from 'react-redux'
import store from '../store/store'
import { useSelector } from 'react-redux'
import { currentShopActions } from '../store/store'
import Map,{} from './Map'
// const CheckShop = () => {
//   return createPortal(
//     <div>CheckShop</div>
//   ,document.getElementById("map"));
// }

const CheckShop = () =>{

  const shop = useSelector(state=>state.currentShop)

  console.log(shop)

  const [one,setOne]  =useState(0)
  const [city, setCity] = useState('')
  const [name, setName] = useState('')

  useEffect(()=>{
    setCity(shop.city)
    setName(shop.name)
  },[shop])

  function calculate(e){
    e.preventDefault()
  }
  return (
    <div className='w-full px-12 flex gap-4 justify-center'>
      <div id='map' className='flex-bigger h-[600px]'></div>
      <div className='flex-1'>
        <form className='w-3/4 flex flex-col justify-start items-center bg-white m-auto mt-[100px] px-[40px] pt-[50px] pb-[40px] gap-[25px] rounded-[20px] shadow-md' onSubmit={calculate}>
          <h4 className='text-[30px] font-[400]'>Input Data</h4>
          <input placeholder={city!=='' ? city: 'Company City'} type="text" name='city' className='w-full flex flex-col p-[20px] text-[16px] shadow-sm'/>
          <input placeholder={name!=='' ? name : 'Company City'} type="text" name='name' className='w-full flex flex-col p-[20px] text-[16px] shadow-sm'/>
          <button className='w-full flex flex-col text-[18px] text-white rounded-[16px] shadow-sm bg-blue-500 px-4 py-2'>Continue</button>
        </form>
      </div>
    </div>
  )
}

export function handleMap(){
  console.log(document.querySelector('#map'))
  if (document.querySelector('#map')){
    return null
  }
  function init() {
    var myMap = new ymaps.Map('map', {
        center: [51.089691, 71.406599],
        zoom: 19,
        controls: [],
    }, {
        // yandexMapDisablePoiInteractivity: true
    });

    // myMap.events.add('contextmenu', (e)=>{
    //     console.log(e)
    // })

    myMap.events.add('balloonopen', (e)=>{
        // console.log(e.get('currentTarget').balloon)
        let organization = e.get('currentTarget').balloon.getData().properties._data

        console.log(organization)

        console.log("Name: ", organization.name)
        console.log("Category: ", organization.categories)

        store.dispatch(currentShopActions.setData({name:organization.name, type:organization.categories, description: organization.description, city: organization.description.split(',').slice(-1)[0]}))
    })

    // // Создаем экземпляр класса ymaps.control.SearchControl
    // mySearchControl = new ymaps.control.SearchControl({
    //         options: {
    //             provider: 'yandex#search',
    //             noPlacemark: true
    //         }
    //     }),
    // // Результаты поиска будем помещать в коллекцию.
    // mySearchResults = new ymaps.GeoObjectCollection(null, {
    //     hintContentLayout: ymaps.templateLayoutFactory.createClass('$[properties.name]')
    // });
    // console.log(mySearchResults)
    // myMap.controls.add(mySearchControl);
    // myMap.geoObjects.add(mySearchResults);
    // // При клике по найденному объекту метка становится красной.
    // mySearchResults.events.add('click', function (e) {
    //     e.get('target').options.set('preset', 'islands#redIcon');
    // });
    // // Выбранный результат помещаем в коллекцию.
    // mySearchControl.events.add('resultselect', function (e) {
    //     var index = e.get('index');
    //     mySearchControl.getResult(index).then(function (res) {
    //        mySearchResults.add(res);
    //        console.log(res)
    //     });
    // }).add('submit', function () {
    //         mySearchResults.removeAll();
    //     })
    
    var searchControl = new ymaps.control.SearchControl({
      options: {
        noSelect: false,
        provider: 'yandex#search',
      }
    });

  myMap.controls.add(searchControl);

  searchControl.events.add('resultselect', function (e) {
      // Получает массив результатов.
      var results = searchControl.getResultsArray();
      // Индекс выбранного объекта.
      var selected = e.get('index');
      console.log(results[selected].properties._data)
      // Получает координаты выбранного объекта.
      var point = results[selected].geometry.getCoordinates();
  })
  }

  ymaps.ready(init);
  return null;
}

export default CheckShop