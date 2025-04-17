<template>

   <div>
     <div class="d-flex" id="wrapper">
       <SidePanel :title="menus.title" :sections="menus.items"/>
      <AppProyectos />

     </div>
     <div class="bg-dark left-sidebar-margin d-flex">
      <AppFooter />
     </div>
   </div>

</template>

<script lang="ts">
// import {  } from 'vue'

import AppProyectos from './components/Projects/AppProyectos.vue'
import SidePanel from './components/SidePanel.vue'
import AppFooter from './components/Footer/AppFooter.vue'

export default {
  components: {
    SidePanel,
    AppProyectos,
    AppFooter
  },

  setup () {
    const menus = {
      title: 'Proyectos',
      items: [
        { title: 'menus.projectsSidebar.container', link: '#container' },
        { title: 'menus.projectsSidebar.cd', link: '#cd' },
        { title: 'menus.projectsSidebar.systems', link: '#systems' },
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
