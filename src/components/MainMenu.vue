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
                   { name: 'Projects', src: '/projects' },
                   { name: 'Misc', src: '/misc' }
                  ]
   
      return {
         selected,
         menus
      }
   }
}
</script>
