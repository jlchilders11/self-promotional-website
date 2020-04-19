import Vue from "vue/dist/vue.js";
import VueRouter from "vue-router";
Vue.use(VueRouter);

import { BootstrapVue } from "bootstrap-vue";
Vue.use(BootstrapVue);
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";

import VueSimpleMarkdown from 'vue-simple-markdown'
// You need a specific loader for CSS files like https://github.com/webpack/css-loader
import 'vue-simple-markdown/dist/vue-simple-markdown.css'
 
Vue.use(VueSimpleMarkdown)

import axios from 'axios'
Vue.use(axios)

import Navbar from "./components/Navbar.vue";
import Home from "./components/Home.vue";
import Projects from "./components/Projects.vue";
import Blog from "./components/Blog.vue";
import BlogDetail from "./components/BlogDetail.vue"

Vue.config.productionTip = false;

const routes = [
    { path: "/", component: Home },
    { path: "/projects/", component: Projects },
    { path: "/blog/", component: Blog },
    { path: "/blog/:id", component: BlogDetail }
];

const router = new VueRouter({
	mode: 'history',
    linkExactActiveClass: "active",
    routes: routes,
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
        Navbar,
    },
}).$mount("#app");