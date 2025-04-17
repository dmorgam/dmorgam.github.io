<template>

   <div>
     <div class="d-flex" id="wrapper">
        <SidePanel :title="menus.title" :sections="menus.items"/>

        <AppHome />
     </div>
     <div class="bg-dark left-sidebar-margin d-flex">
      <AppFooter />
     </div>
   </div>

</template>

<script lang="ts">
// import {  } from 'vue'

import AppHome from './components/Home/AppHome.vue'
import SidePanel from './components/SidePanel.vue'
import AppFooter from './components/Footer/AppFooter.vue'

export default {

  components: {
    SidePanel,
    AppHome,
    AppFooter
  },

  setup () {
    const menus = {
      title: 'Secciones',
      items: [
        { title: 'menus.indexSidebar.start', link: '#' },
        { title: 'menus.indexSidebar.who', link: '#who' },
        { title: 'menus.indexSidebar.tech', link: '#tech' },
        { title: 'menus.indexSidebar.credly', link: '#credly' }
      ]
    }

    return {
      menus
    }
  }
}
</script>
