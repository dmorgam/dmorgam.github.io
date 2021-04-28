<template>
   <div class="container-fluid home-back left-sidebar-margin">
      <br><br><br><br>
      <h1 class="text-light" id="web">
        <span class="badge badge-pill badge-secondary">
          <BIconCaretRightFill />
          Proyectos Web
        </span>
      </h1><br><br>

      <Ficha v-for="(item, index) in projectsData.filter(i => i.type === 'web')" :key="index" :item="item" />

      <br><br>
      <h1 class="text-light" id="webapps">
        <span class="badge badge-pill badge-info">
          <BIconCaretRightFill />
          Webapps
        </span>
      </h1><br><br>

      <Ficha v-for="(item, index) in projectsData.filter(i => i.type === 'webapp')" :key="index" :item="item" />

      <br><br>
      <h1 class="text-light" id="games">
        <span class="badge badge-pill badge-light">
          <BIconCaretRightFill />
          Juegos
        </span>
      </h1><br><br>

      <Ficha v-for="(item, index) in projectsData.filter(i => i.type === 'game')" :key="index" :item="item" />

      <br>
   </div>
</template>

<script lang="ts">
import { } from 'vue'
import json from '../../projects.json'
import Ficha from './Ficha.vue'
import { BIconCaretRightFill } from 'bootstrap-icons-vue'

export default {
  components: {
    Ficha,
    BIconCaretRightFill
  },

  setup () {
    const projectsData = json

    return {
      projectsData
    }
  }
}
</script>
