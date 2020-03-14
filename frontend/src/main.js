import Vue from 'vue/dist/vue.js'
import VueRouter from 'vue-router'
Vue.use(VueRouter)

import Navbar from './components/Navbar.vue'
import Home from './components/Home.vue'

Vue.config.productionTip = false



const routes = [
	{ path: '/', component: Home }
]

const router = new VueRouter({
	routes:routes
})

new Vue({
  router,
  template: `
	<div>
	<Navbar />
	<router-view class="view"></router-view>
	</div>
  `,
  components: {
    Navbar
  }
}).$mount('#app');
