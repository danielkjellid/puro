import Vue from 'vue'
import Router from 'vue-router'
import UserRoutes from './modules/users/routes'

Vue.use(Router)

const baseRoutes = [
  
];

const routes = baseRoutes.concat(UserRoutes);

const router = new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
});

export default router
