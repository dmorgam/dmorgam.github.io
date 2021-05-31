<template>
<!-- Componente Main del home -->
<div>
   <MainMenu />
   <router-view />
</div>
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component'
import i18n from '@/i18n'
// import {  } from 'vue'

// Components
import MainMenu from './components/MainMenu.vue'

@Options({
  components: {
    MainMenu
  }
})

// Class based TS component, extend vue, properties defined directly in the class
export default class App extends Vue {
  mounted () {
    if (navigator.language.split('-')[0] === 'es') {
      i18n.global.locale = 'es'
    } else {
      i18n.global.locale = 'en'
    }
  }
}
</script>
