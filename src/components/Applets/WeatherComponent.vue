<template>
   <div class="text-light">
     <button v-if="!weatherInfo.changeUb" v-on:click="weatherInfo.changeUb = true" title="Cambiar Ubicación" class="btn btn-sm btn-info">
         <BIconGeoAlt />
     </button>
     <div v-else class="input-group">
         <input type="text" class="form-control" v-model="weatherInfo.city">
         <div class="input-group-append">
           <button class="btn btn-sm btn-success" v-on:click="refreshWeather()">
             <BIconCheck />
           </button>
         </div>
     </div>
     <div v-if="!weatherInfo.changeUb" class="d-inline">
        <img style="width: 3em;" :src="'https://openweathermap.org/img/w/'+weatherInfo.icon+'.png'">
        {{ Math.floor(weatherInfo.degrees) }} ºC, {{ weatherInfo.info }} -
        {{ weatherInfo.city }}, {{ weatherInfo.country }}
     </div>
   </div>
</template>

<script lang="ts">
import { reactive, onMounted } from 'vue'
import { BIconCheck, BIconGeoAlt } from 'bootstrap-icons-vue'
import axios from 'axios'
import i18n from '@/i18n'

export default {

  components: {
    BIconCheck,
    BIconGeoAlt
  },
  setup () {
    const weatherInfo = reactive({
      icon: '',
      city: '',
      country: '',
      info: '',
      degrees: 0,
      changeUb: false
    })

    onMounted(() => {
      fetchLocWh()
    })

    function fetchLocWh () {
      // Location fetching
      axios.get('https://ipapi.co/json').then((response) => {
        weatherInfo.city = response.data.city
        weatherInfo.country = response.data.country_code

        fetchWeather()
      })
    }

    function fetchWeather () {
      // Forecast fetching
      axios.get('https://pcmt93kogj.execute-api.eu-central-1.amazonaws.com/weather?q=' + weatherInfo.city + ',' + weatherInfo.country + '&lang=' + i18n.global.locale)
        .then((forecast) => {
          weatherInfo.icon = forecast.data.weather[0].icon
          weatherInfo.info = forecast.data.weather[0].description
          weatherInfo.degrees = forecast.data.main.temp - 273.15
        })
    }

    function refreshWeather () {
      fetchWeather()
      weatherInfo.changeUb = false
    }

    return {
      weatherInfo,
      refreshWeather
    }
  }
}
</script>
