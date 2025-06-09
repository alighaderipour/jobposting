import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import JobPosting from '../views/JobPosting.vue'
import AddJobPosting from '../views/AddJobPosting.vue'

const routes = [
  { path: '/', component: Home },
  { path: '/jobposting', component: JobPosting },
  { path: '/add_employee', component: AddJobPosting },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
