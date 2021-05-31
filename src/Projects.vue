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
        { title: 'menus.projectsSidebar.webp', link: '#web' },
        { title: 'menus.projectsSidebar.webapps', link: '#webapps' },
        { title: 'menus.projectsSidebar.games', link: '#games' }
      ]
    }

    return {
      menus
    }
  }
}
</script>
