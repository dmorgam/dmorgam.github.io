<template>
<!-- Componente Main del home -->
<div>
   <MainMenu />
   
   <div class="d-flex" id="wrapper">
      <SidePanel :data="SidePanel" />
   
      <Home/>
   </div>
   
</div>
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component'
import {  reactive } from 'vue'

// Components
import MainMenu from './components/MainMenu.vue'
import Home from './components/Home/Home.vue'
import SidePanel from './components/SidePanel.vue'

@Options({
  components: {
     MainMenu, 
     Home, 
     SidePanel,
  },
})
export default class App extends Vue {
   options(){

      const SidePanel = reactive({ title: '', items: [] })
      
      return {
         SidePanel,
      }
   }

}
</script>
