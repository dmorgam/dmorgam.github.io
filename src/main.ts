import { createApp } from 'vue'
import App from './App.vue'
import router from './router/index'
import i18n from './i18n'
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
import './css/simple-sidebar.css'
import './css/main.css'

createApp(App).use(router).use(i18n).mount('#app')
