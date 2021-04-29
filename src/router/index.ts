import { createWebHistory, createRouter } from 'vue-router'
import Index from '../Index.vue'
import Projects from '../Projects.vue'
import QrCode from '../QrCode.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Index
  },
  {
    path: '/projects',
    name: 'Projects',
    component: Projects
  },
  {
    path: '/qrcode',
    name: 'QrCode',
    component: QrCode
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
