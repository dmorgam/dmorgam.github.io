<template>

   <div>
     <div class="d-flex" id="wrapper">
       <SidePanel :title="menus.title" :sections="menus.items"/>
      <Proyectos />

     </div>
     <div class="bg-dark left-sidebar-margin d-flex">
      <Footer />
     </div>
   </div>

</template>

<script lang="ts">
// import {  } from 'vue'

import Proyectos from './components/Projects/Proyectos.vue'
import SidePanel from './components/SidePanel.vue'
import Footer from './components/Footer/Footer.vue'

export default {
  components: {
    SidePanel,
    Proyectos,
    Footer
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
