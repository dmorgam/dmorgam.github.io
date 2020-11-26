import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
import './css/simple-sidebar.css'

createApp(App).use(router).mount('#app')
