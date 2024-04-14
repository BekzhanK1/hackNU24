import React, {memo,useEffect} from 'react'
import { createPortal,render } from 'react-dom'

// const Map = (() => {
//   return (
//     <div className='flex-bigger h-[600px]' id='map' />
//   )
// })

const Map = (() => {
    useEffect(() => {
        // Generate a unique ID for the map container
    
        // Create the map using the generated ID
        const map = document.getElementById('map')
        if (map) handleMap()
    
        // Make sure to remove the map when the component unmounts
        return () => {
          map && map.remove();
        };
      }, []);
    
      return (
        <div id='map' className='flex-bigger h-[600px]'></div>
      )
})

export default Map


function handleMap(){
    console.log(1234)
    function init() {
        var myMap = new ymaps.Map('map', {
            center: [51.089691, 71.406599],
            zoom: 19,
            controls: []
        });
    
        // Создаем экземпляр класса ymaps.control.SearchControl
        let mySearchControl = new ymaps.control.SearchControl({
          options: {
            provider: 'yandex#search',
            noPlacemark: true
          }
        }),
        // Результаты поиска будем помещать в коллекцию.
        mySearchResults = new ymaps.GeoObjectCollection(null, {
          hintContentLayout: ymaps.templateLayoutFactory.createClass('$[properties.name]')
        });
        myMap.controls.add(mySearchControl);
        myMap.geoObjects.add(mySearchResults);
        // При клике по найденному объекту метка становится красной.
        mySearchResults.events.add('click', function (e) {
            let res = document.querySelectorAll("ymaps-2-1-79-balloon__content a")
            console.log(res)
            res.forEach(elem=>{
              console.log(elem.target.value)
            })
            e.get('target').options.set('preset', 'islands#redIcon');
        });
        // Выбранный результат помещаем в коллекцию.
        mySearchControl.events.add('resultselect', function (e) {
          let res = document.querySelectorAll("ymaps-2-1-79-balloon__content a")
            console.log(res)
          var index = e.get('index');
          mySearchControl.getResult(index).then(function (res) {
            mySearchResults.add(res);
          });
        }).add('submit', function () {
          mySearchResults.removeAll();
        })
    }
    
    ymaps.ready(init);
}