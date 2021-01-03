<template>
   <div class="text-light">
     <img style="width: 3em;" :src="'https://openweathermap.org/img/w/'+weatherInfo.icon+'.png'">
     {{ weatherInfo.info }} -  
     {{ weatherInfo.city }}, {{ weatherInfo.country }}
   </div>
</template>

<script lang="ts">
import { reactive,onMounted } from 'vue'
import axios from "axios" 

export default {

   setup(){

    const weatherInfo = reactive({
        icon: '',
        city: '',
        country: '',
        info: '',
        apiKey: '9d5cedadfe0c37af9903057243965e06',
    }) 


    onMounted(() => {
        fetchWeather()
    })
     
     function fetchWeather(){
          
       // Location fetching
       axios.get('https://ipapi.co/json').then((response) => {
            weatherInfo.city    = response.data.city
            weatherInfo.country = response.data.country_code


            // Forecast fetching
            axios.get('https://api.openweathermap.org/data/2.5/weather?q='+weatherInfo.city+','+weatherInfo.country+'&lang=es&appid='+weatherInfo.apiKey)
            .then((forecast) => {
                
                weatherInfo.icon = forecast.data.weather[0].icon
                weatherInfo.info = forecast.data.weather[0].description

            })

       })

     }


     return {
        weatherInfo,
     }


   }
}
</script>
