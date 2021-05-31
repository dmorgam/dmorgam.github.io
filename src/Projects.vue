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
import i18n from '@/i18n'

export default {
  components: {
    SidePanel,
    Proyectos
  },

  setup () {
    const menus = {
      title: 'Proyectos',
      items: [
        { title: i18n.global.t('menus.projectsSidebar.webp'), link: '#web' },
        { title: i18n.global.t('menus.projectsSidebar.webapps'), link: '#webapps' },
        { title: i18n.global.t('menus.projectsSidebar.games'), link: '#games' }
      ]
    }

    return {
      menus
    }
  }
}
</script>
