<template>

   <div class="d-flex" id="wrapper">
      <SidePanel :title="menus.title" :sections="menus.items"/>

      <Home />
   </div>

</template>

<script lang="ts">
// import {  } from 'vue'

import Home from './components/Home/Home.vue'
import SidePanel from './components/SidePanel.vue'

export default {

  components: {
    SidePanel,
    Home
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
