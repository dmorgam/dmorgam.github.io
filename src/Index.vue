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
import i18n from '@/i18n'

export default {

  components: {
    SidePanel,
    Home
  },

  setup () {
    const menus = {
      title: 'Secciones',
      items: [
        { title: i18n.global.t('menus.indexSidebar.start'), link: '#' },
        { title: i18n.global.t('menus.indexSidebar.who'), link: '#who' },
        { title: i18n.global.t('menus.indexSidebar.tech'), link: '#tech' }
      ]
    }

    return {
      menus
    }
  }
}
</script>
