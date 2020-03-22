// for optimization all routes in the backend is loaded lazily
export default [
  {
    path: '/users',
    name: 'users',
    component: () => import(/* webpackChunkName: "users" */ '../views/UsersOverview.vue'),
    title: 'Backend: Users',
  },
  {
    path: '/users/:id',
    name: 'users-detail',
    component: () => import(/* webpackChunkName: "users-detail" */ '../views/UserDetail')
  },
]