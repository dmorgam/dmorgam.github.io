<template>

   <div class="d-flex" id="wrapper">
     <SidePanel :title="menus.title" :sections="menus.items"/>
    <Proyectos />

   </div>

</template>

<script lang="ts">
// import {  } from 'vue'

import Proyectos from './components/Projects/Proyectos.vue'
import SidePanel from './components/SidePanel.vue'

export default {
  components: {
    SidePanel,
    Proyectos
  },

  setup () {
    const menus = {
      title: 'Proyectos',
      items: [
        { title: 'Proyectos Web', link: '#web' },
        { title: 'Aplicaciones Web', link: '#webapps' },
        { title: 'Juegos', link: '#games' }
      ]
    }

    return {
      menus
    }
  }
}
</script>
