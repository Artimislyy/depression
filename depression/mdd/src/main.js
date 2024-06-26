/*
 * @Autor: Hongting Yuan
 * @Date: 2022-04-02 14:19:59
 * @LastEditors: Hongting Yuan
 * @LastEditTime: 2022-05-25 15:37:52
 * @Description: file content
 * @FilePath: \mdd\src\main.js
 */
// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
// 引入element-ui
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

// 引入路由配置（如果安装时有选择安装路由，这里默认已经配置好)
import router from './router'
import global_ from './utils/global'
import preventReClick from './assets/js/preventReClick.js'
// import DevicePixelRatio from './assets/js/devicePixelRatio.js'
import axios from 'axios'
import * as echarts from 'echarts'
Vue.prototype.$echarts = echarts
Vue.prototype.axios = axios
axios.defaults.baseURL = '/api'
Vue.prototype.GLOBAL = global_


Vue.config.productionTip = false
Vue.use(ElementUI)
Vue.use(preventReClick)
// Vue.use(DevicePixelRatio)
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  render: h => h(App)
  // components: { App },
  // template: '<App/>'
})
