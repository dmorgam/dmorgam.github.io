<template>

  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <a class="navbar-brand" href="javascript: void(0)">Dmorgam</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" 
              aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
         <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
          <div class="navbar-nav">
             <router-link v-for="item in menus" :key="item.name" class="nav-link" :to="item.src"
                :class="{'active': item.name == selected}">
                
                <!-- Icono del Home -->
                <svg v-if="item.src == '/'" width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-house-fill" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                     <path fill-rule="evenodd" d="M8 3.293l6 6V13.5a1.5 1.5 0 0 1-1.5 1.5h-9A1.5 1.5 0 0 1 2 13.5V9.293l6-6zm5-.793V6l-2-2V2.5a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5z"/>
                     <path fill-rule="evenodd" d="M7.293 1.5a1 1 0 0 1 1.414 0l6.647 6.646a.5.5 0 0 1-.708.708L8 2.207 1.354 8.854a.5.5 0 1 1-.708-.708L7.293 1.5z"/>
                </svg>

                 {{ item.name }} 
             </router-link>
          </div>
      </div>
  </nav>

</template>

<script lang="ts">
import { ref } from 'vue'

export default {
   setup(){
      const selected = ref('Home')
      
      let menus = [
                   { name: 'Home', src: '/' },
                   { name: 'Proyectos', src: '/projects' },
                  ]
   
      return {
         selected,
         menus
      }
   }
}
</script>
