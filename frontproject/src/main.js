import Vue from 'vue'
import store from  './store'
import router from './router'
import App from './App.vue'
import axios from 'axios'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
axios.defaults.baseURL='http://127.0.0.1:8000'

Vue.config.productionTip = false
Vue.use(ElementUI)
Vue.prototype.$ajax=axios
new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')
