<template>
   <div class="container-fluid home-back left-sidebar-margin">
      <br><br><br><br>

      <div class="alert alert-info">
        <h5>
          <BIconInfoCircle />
          {{ $t('projects-info-alert') }}
        </h5>
      </div>

      <br>
      <h1 class="text-light" id="cd">
        <span class="badge badge-pill ">
          <BIconCaretRightFill />
          {{ $t('menus.projectsSidebar.cd') }}
        </span>
        <hr style="opacity: 0%;">
      </h1><br><br>

      <Ficha v-for="(item, index) in projectsData.filter(i => i.type === 'cd')" :key="index" :item="item" />

      <br><br>
      <h1 class="text-light" id="web">
        <span class="badge badge-pill">
          <BIconCaretRightFill />
          {{ $t('menus.projectsSidebar.webp') }}
        </span>
        <hr style="opacity: 0%;">
      </h1><br><br>

      <Ficha v-for="(item, index) in projectsData.filter(i => i.type === 'web')" :key="index" :item="item" />

      <br><br>
      <h1 class="text-light" id="webapps">
        <span class="badge badge-pill">
          <BIconCaretRightFill />
          {{ $t('menus.projectsSidebar.webapps') }}
        </span>
        <hr style="opacity: 0%;">
      </h1><br><br>

      <Ficha v-for="(item, index) in projectsData.filter(i => i.type === 'webapp')" :key="index" :item="item" />

      <br><br>
      <h1 class="text-light" id="games">
        <span class="badge badge-pill">
          <BIconCaretRightFill />
          {{ $t('menus.projectsSidebar.games') }}
        </span>
        <hr style="opacity: 0%;">
      </h1><br><br>

      <Ficha v-for="(item, index) in projectsData.filter(i => i.type === 'game')" :key="index" :item="item" />

      <br>
   </div>
</template>

<script lang="ts">
import { } from 'vue'
import json from '../../projects.json'
import Ficha from './Ficha.vue'
import { BIconCaretRightFill, BIconInfoCircle } from 'bootstrap-icons-vue'

export default {
  components: {
    Ficha,
    BIconCaretRightFill,
    BIconInfoCircle
  },

  setup () {
    const projectsData = json

    return {
      projectsData
    }
  }
}
</script>
