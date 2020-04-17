import Vue from "vue/dist/vue.js";
import VueRouter from "vue-router";
Vue.use(VueRouter);

import {BootstrapVue} from 'bootstrap-vue'
Vue.use(BootstrapVue)
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import Navbar from "./components/Navbar.vue";
import Home from "./components/Home.vue";
import Projects from "./components/Projects.vue";

Vue.config.productionTip = false;

const routes = [
	{ path: "/", component: Home },
	{ path: "/projects/", component: Projects }
];

const router = new VueRouter({
	linkExactActiveClass: 'active',
	routes: routes
});

new Vue({
	router,
	template: `
	<div>
	<Navbar />
    <main class="container" role="main">
		<router-view class="view"></router-view>
	</main>
	</div>
  `,
	components: {
		Navbar
	}
}).$mount("#app");
