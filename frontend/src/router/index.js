import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import JobPosting from '../views/JobPosting.vue'
import AddJobPosting from '../views/AddJobPosting.vue'
import NotFound from '../views/NotFound.vue'


const routes = [
  { path: '/', component: Home },
  { path: '/jobposting', component: JobPosting },
  { path: '/jobposting/add', component: AddJobPosting },
  { path: '/jobposting/not_found', component: NotFound },
  {
  path: '/jobposting/details/:id',
  name: 'JobDetails',
  component: () => import('@/views/JobPostingDetails.vue')
},
 {
  path: '/admin',
  component: {
    template: '<div>This route is handled by Django. Go to <a href="http://localhost:8000/admin">http://localhost:8000/admin</a>.</div>'
  }
}
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
