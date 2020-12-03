<template>

   <div class="d-flex" id="wrapper">
      <SidePanel :title="menus.title" :sections="menus.items"/>
   
      <Home />
   </div>

</template>

<script lang="ts">
import {  } from 'vue'

import Home from './components/Home/Home.vue'
import SidePanel from './components/SidePanel.vue'

export default {

   components: {
        SidePanel,
        Home
   },
   setup(){
    
      let menus = { 
            title: 'Secciones', 
            items: [
               { title: 'Inicio', link: '#' },
               { title: 'Quien soy', link: '#who' },
               { title: 'Tecnologías', link: '#tech' },
            ] 
      }
      
     return {
        menus,
     }
   }
}
</script>
