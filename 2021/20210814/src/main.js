import Vue from 'vue'
import App from './App.vue'

import * as VueGoogleMaps from "vue2-google-maps" // Import package

Vue.config.productionTip = false

Vue.use(VueGoogleMaps, {
  load: {
    key: "api key ",
    libraries: "places",
    region: "KR" //이거 추가 안하면 동해가 일본해로 뜸 ㅡ"ㅡ
  }
});

new Vue({
  render: h => h(App),
}).$mount('#app')
