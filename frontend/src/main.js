import Vue from "vue/dist/vue.js";
import VueRouter from "vue-router";
Vue.use(VueRouter);

import { BootstrapVue } from "bootstrap-vue";
Vue.use(BootstrapVue);
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";

import axios from 'axios'
Vue.use(axios)

import Navbar from "./components/Navbar.vue";
import Home from "./components/Home.vue";
import Projects from "./components/Projects.vue";
import Blog from "./components/Blog.vue";
import BlogDetail from "./components/BlogDetail.vue";
import BlogList from "./components/BlogList.vue";

Vue.config.productionTip = false;

const routes = [
    {
        path: '/',
        redirect: '/home',
    },
    { 
        path: "/home", 
        component: Home,
        name: 'Home'
    },
    { 
        path: "/projects/", 
        component: Projects,
        name: 'Projects'
    },
    {
        path: "/blog/",
        component: Blog,
        children: [
            {
                path: '',
                component: BlogList,
                name: 'Blog',
            },
            {
                path: ':id',
                component: BlogDetail,
                name: 'BlogDetails'
            },
        ]
    },
];

const router = new VueRouter({
    mode: 'history',
    linkActiveClass: "active",
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