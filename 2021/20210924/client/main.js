import BootstrapVue from 'bootstrap-vue';
import * as VueGoogleMaps from 'vue2-google-maps';
import Vue from 'vue';
import App from './App.vue';
import router from './router';
import 'bootstrap/dist/css/bootstrap.css';

Vue.use(BootstrapVue);

Vue.use(VueGoogleMaps, {
  load: {
    key: '구글 클라우드에서 받은 키 넣어야 됩니다.',
    libraries: 'places',
    region: 'KR',
  },
});

Vue.config.productionTip = false;

new Vue({
  router,
  render: (h) => h(App),
}).$mount('#app');
