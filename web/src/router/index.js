import Vue from 'vue'
import Router from 'vue-router'
import login from '@/components/login'
import dashboard from '@/components/dashboard/main'
import project from '@/components/project/main'
import logout from '@/components/logout'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: '/mockserver/',
  routes: [
    {
      path: '/',
      name: 'login',
      component: login
    },
    {
      path: '/login',
      name: 'login',
      component: login
    },
    {
      path: '/logout',
      name: 'logout',
      component: logout
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: dashboard
    },
    {
      path: '/project',
      name: 'project',
      component: project
    }
  ]
})
