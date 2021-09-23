import Vue from 'vue';
import Router from 'vue-router';
import Home from '../components/Home.vue';
import Ping from '../components/Ping.vue';
import Books from '../components/Books.vue';
import Map from '../components/AddGoogleMap.vue';
import Chart from '../components/Chart.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home,
    },
    {
      path: '/books',
      name: 'Books',
      component: Books,
    },
    {
      path: '/ping',
      name: 'Ping',
      component: Ping,
    },
    {
      path: '/map',
      name: 'Map',
      component: Map,
    },
    {
      path: '/chart',
      name: 'Chart',
      component: Chart,
    },
  ],
});
