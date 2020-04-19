<template>
    <b-navbar toggleable="lg" type="dark" variant="dark" fixed=top>
        <b-navbar-brand>
            Jeremy Childers
        </b-navbar-brand>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <b-navbar-nav>
                <li class="nav-item">
                    <router-link class="nav-link" :to="{name: 'Home'}">
                        <i class="fa fa-fw fa-home"></i>
                        Home
                    </router-link>
                </li>
                <li class="nav-item">
                    <router-link class="nav-link" :to="{name: 'Projects'}">
                        <i class="fa fa-fw fa-flask"></i>
                        Projects
                    </router-link>
                </li>
                <li class="nav-item">
                    <router-link class="nav-link" :to="{name: 'Blog'}">
                        <i class="fa fa-fw fa-feed"></i>
                        Blog
                    </router-link>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="https://github.com/jlchilders11" target="_blank">
                        <i class="fa fa-fw fa-github"></i>
                        Github
                    </a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="https://www.linkedin.com/in/jeremy-childers-2270681a3/">
                        <i class="fa fa-fw fa-linkedin"></i>
                        LinkedIn
                    </a>
                </li>
            </b-navbar-nav>
        </div>
    </b-navbar>
</template>
<script>
export default {
    name: "Navbar",
};
</script>