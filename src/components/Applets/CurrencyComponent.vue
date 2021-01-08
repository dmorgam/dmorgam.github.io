<template>
   <div class="alert alert-secondary w-100" style="position:absolute; bottom: 0px">
     <b><BIconCash /> Cambio de divisas</b><hr>
     <div class="row">
       <div class="col-sm-8">
         <b>€ EUR </b> {{ currency.selected }}
       </div>
       <select class="form-control col-sm-4 float-right" v-model="currency.selected">
         <option v-for="item in Object.entries(currency.rates)" :key="item[0]" :value="item[1]">
              {{ item[0] }}
         </option>
       </select>
     </div>
   </div>
</template>

<script lang="ts">
import { reactive,onMounted } from 'vue'
import { BIconCash } from 'bootstrap-icons-vue'
import axios from "axios" 

export default {

   components: {
     BIconCash,
   },
   setup(){

    const currency = reactive({
      rates: [],
      base: '',
      selected: '0.0',
      start: 'USD',
    }) 


    onMounted(() => {
        fetchCurrency()
    })
     
     function fetchCurrency(){
          
       axios.get('https://api.exchangeratesapi.io/latest?base=EUR').then((response) =>{
          currency.rates    = response.data.rates
          currency.base     = response.data.base
          currency.selected = response.data.rates[currency.start]

       })


      }


     return {
        currency,
     }


   }
}
</script>
