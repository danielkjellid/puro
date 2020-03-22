import Vue from 'vue'
import Router from 'vue-router'
import UserRoutes from './modules/users/routes'

import Playground from './core/backend/templates/Playground'

Vue.use(Router)

const baseRoutes = [
    {
        path: '/playground',
        name: 'playground',
        component: Playground
    },
];

const routes = baseRoutes.concat(UserRoutes);

const router = new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
});

export default router
