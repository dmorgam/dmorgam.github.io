<template>

  <nav class="navbar fixed-top navbar-expand-lg navbar-dark bg-dark">
      <a class="navbar-brand" href="javascript: void(0)">Dmorgam</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup"
              aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
         <span class="navbar-toggler-icon"></span>
      </button>
      <div class="navbar-collapse collapse w-100 order-1 order-md-0 dual-collapse2" id="navbarNavAltMarkup">
          <div class="navbar-nav">
            <router-link v-for="item in menus.filter(i => i.submenu.length === 0)" :key="item.name"
                class="nav-link" :to="item.src" :class="{'active': $route.name == item.route }">

                <!-- Icono del Home -->
                <BIconHouseFill v-if="item.name == 'Home'" />
                 {{ $t(item.name) }}
             </router-link>
             <li class="nav-item dropdown" v-for="(item, idx) in menus.filter(i => i.submenu.length > 0)" :key="idx">
               <a class="nav-link dropdown-toggle" href="javascript:void(0)" :id="item.name" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                 {{ $t(item.name) }}
               </a>
               <div class="dropdown-menu" v-for="(itm, index) in item.submenu" :key="index">
                 <router-link class="dropdown-item" :to="itm.src">{{ $t(itm.name) }}</router-link>
                </div>
             </li>
          </div>
        <div class="navbar-nav ml-auto">
            <div class="nav-item">
              <weatherApplet />
            </div>
            <div class="nav-item d-flex align-items-center">
              <select class="form-control form-control-sm ml-2" v-model="$root.$i18n.locale">
                <option value="en">🇬🇧 English</option>
                <option value="es">🇪🇸 Español</option>
              </select>
            </div>
        </div>
      </div>
  </nav>

</template>

<script lang="ts">
// import {  } from 'vue'
import weatherApplet from './Applets/WeatherComponent.vue'
import { BIconHouseFill } from 'bootstrap-icons-vue'

interface MenuItem {
  route: string,
  name: string,
  src: string,
  submenu: MenuItem[]
}

export default {
  components: {
    weatherApplet,
    BIconHouseFill
  },
  setup () {
    const menus: MenuItem[] = [
      { route: 'Home', name: 'menus.navbar.home', src: '/', submenu: [] as MenuItem[] },
      { route: 'Projects', name: 'menus.navbar.projects', src: '/projects', submenu: [] as MenuItem[] },
      {
        route: 'Tools',
        name: 'menus.navbar.tools',
        src: '',
        submenu: [{ route: 'Qrcode', name: 'menus.navbar.toolsMenu.qrcode', src: '/qrcode', submenu: [] as MenuItem[] }]
      }
    ]

    return {
      menus
    }
  }
}
</script>
