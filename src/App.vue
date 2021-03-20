<template>
<!-- Componente Main del home -->
<div>
   <MainMenu />
   <router-view />
</div>
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component'
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

}
</script>
