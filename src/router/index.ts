import { createWebHistory, createRouter } from 'vue-router'
import Index from '../AppIndex.vue'
import AppProjects from '../AppProjects.vue'
import QrCode from '../QrCode.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Index
  },
  {
    path: '/projects',
    name: 'AppProjects',
    component: AppProjects
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
