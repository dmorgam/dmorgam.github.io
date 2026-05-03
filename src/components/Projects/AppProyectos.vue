<template>
   <div class="container-fluid home-back left-sidebar-margin projects-page px-4 px-md-5">
      <div class="projects-header">
        <div class="alert alert-info text-center mb-0">
          <h5 class="mb-0">
            <BIconInfoCircle />
            {{ $t('projects-info-alert') }}
          </h5>
        </div>
      </div>

      <section class="projects-section" id="container">
        <h2 class="section-title">
          <span class="badge bg-pill">
            <BIconCaretRightFill />
            {{ $t('menus.projectsSidebar.container') }}
          </span>
        </h2>
        <div class="projects-grid">
          <AppFicha v-for="(item, index) in projectsData.filter(i => i.type === 'container')" :key="index" :item="item" />
        </div>
      </section>

      <section class="projects-section" id="cd">
        <h2 class="section-title">
          <span class="badge bg-pill">
            <BIconCaretRightFill />
            {{ $t('menus.projectsSidebar.cd') }}
          </span>
        </h2>
        <div class="projects-grid">
          <AppFicha v-for="(item, index) in projectsData.filter(i => i.type === 'cd')" :key="index" :item="item" />
        </div>
      </section>

      <section class="projects-section" id="systems">
        <h2 class="section-title">
          <span class="badge bg-pill">
            <BIconCaretRightFill />
            {{ $t('menus.projectsSidebar.systems') }}
          </span>
        </h2>
        <div class="projects-grid">
          <AppFicha v-for="(item, index) in projectsData.filter(i => i.type === 'systems')" :key="index" :item="item" />
        </div>
      </section>

      <section class="projects-section" id="web">
        <h2 class="section-title">
          <span class="badge bg-pill">
            <BIconCaretRightFill />
            {{ $t('menus.projectsSidebar.webp') }}
          </span>
        </h2>
        <div class="projects-grid">
          <AppFicha v-for="(item, index) in projectsData.filter(i => i.type === 'web')" :key="index" :item="item" />
        </div>
      </section>

      <section class="projects-section" id="webapps">
        <h2 class="section-title">
          <span class="badge bg-pill">
            <BIconCaretRightFill />
            {{ $t('menus.projectsSidebar.webapps') }}
          </span>
        </h2>
        <div class="projects-grid">
          <AppFicha v-for="(item, index) in projectsData.filter(i => i.type === 'webapp')" :key="index" :item="item" />
        </div>
      </section>

      <section class="projects-section" id="games">
        <h2 class="section-title">
          <span class="badge bg-pill">
            <BIconCaretRightFill />
            {{ $t('menus.projectsSidebar.games') }}
          </span>
        </h2>
        <div class="projects-grid">
          <AppFicha v-for="(item, index) in projectsData.filter(i => i.type === 'game')" :key="index" :item="item" />
        </div>
      </section>
   </div>
</template>

<script lang="ts">
import { } from 'vue'
import json from '../../projects.json'
import AppFicha from './AppFicha.vue'
import { BIconCaretRightFill, BIconInfoCircle } from 'bootstrap-icons-vue'

export default {
  components: {
    AppFicha,
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
