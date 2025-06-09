import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import JobPosting from '../views/JobPosting.vue'
import AddJobPosting from '../views/AddJobPosting.vue'


const routes = [
  { path: '/', component: Home },
  { path: '/jobposting', component: JobPosting },
  { path: '/jobposting/add', component: AddJobPosting },
  {
  path: '/jobposting/details/:id',
  name: 'JobDetails',
  component: () => import('@/views/JobPostingDetails.vue')
}
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
