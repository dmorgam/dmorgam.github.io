<template>

  <nav class="navbar fixed-top navbar-expand-lg navbar-dark bg-dark">
      <a class="navbar-brand" href="javascript: void(0)">Dmorgam</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" 
              aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
         <span class="navbar-toggler-icon"></span>
      </button>
      <div class="navbar-collapse collapse w-100 order-1 order-md-0 dual-collapse2" id="navbarNavAltMarkup">
          <div class="navbar-nav">
             <router-link v-for="item in menus" :key="item.name" class="nav-link" :to="item.src"
                          :class="{'active': $route.name == item.route }">
                
                <!-- Icono del Home -->
                <BIconHouseFill v-if="item.name == 'Home'" />

                 {{ item.name }} 
             </router-link>
          </div>
        <div class="navbar-nav ml-auto">
            <div class="nav-item">
              <weatherApplet />
            </div>
        </div>
      </div>
  </nav>

</template>

<script lang="ts">

interface MenuItem {
  route: string,
  name: string,
  src: string
}

import {  } from 'vue'
import weatherApplet from './Applets/WeatherComponent.vue'
import { BIconHouseFill } from 'bootstrap-icons-vue'


export default {
   components: {
        weatherApplet,
        BIconHouseFill,
   },
   setup(){
      
     let menus: MenuItem[] = [
                    { route: 'Home',name: 'Home', src: '/' },
                    { route: 'Projects',name: 'Proyectos', src: '/projects' },
                  ]
   
      return {
         menus
      }
   }
}
</script>
