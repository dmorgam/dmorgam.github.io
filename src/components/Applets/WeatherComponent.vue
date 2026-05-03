<template>
  <div class="weather-applet">
    <div v-if="!weatherInfo.changeUb" class="weather-display"
         :title="`${weatherInfo.info} · ${weatherInfo.city}, ${weatherInfo.country}`">
      <img v-if="weatherInfo.icon" class="weather-icon"
           :src="'https://openweathermap.org/img/w/'+weatherInfo.icon+'.png'" alt="">
      <span class="weather-temp" v-if="weatherInfo.degrees">
        {{ Math.floor(weatherInfo.degrees) }}<small>°C</small>
      </span>
      <span class="weather-city" v-if="weatherInfo.city">{{ weatherInfo.city }}</span>
      <button v-on:click="weatherInfo.changeUb = true" class="weather-edit"
              :title="$t('weatherApplet.changeLocation') || 'Change location'" aria-label="Change location">
        <BIconGeoAlt />
      </button>
    </div>

    <div v-else class="weather-edit-form">
      <input type="text" class="weather-input" v-model="weatherInfo.city"
             @keyup.enter="refreshWeather()" placeholder="City">
      <button class="weather-confirm" v-on:click="refreshWeather()" aria-label="Confirm">
        <BIconCheck />
      </button>
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
      axios.get('https://ipapi.co/json').then((response) => {
        weatherInfo.city = response.data.city
        weatherInfo.country = response.data.country_code
        fetchWeather()
      })
    }

    function fetchWeather () {
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
