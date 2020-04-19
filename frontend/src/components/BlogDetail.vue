<template>
    <div>
        <div class="card w-100">
            <div class="card-header">
                <h3 style="text-align: center"><strong>{{ entry.title }}</strong></h3>
            </div>
            <div class="card-body">
                <p class="card-text">
                    <pre style="white-space: pre-wrap;">{{ entry.entry }}</pre>
                </p>
            </div>
            <div class="card-footer text-muted">
                <router-link class="btn btn-dark mr-2" :to="{name: 'Blog'}">
                    <i class="fa fa-arrow-left fa-w"></i>
                </router-link>
                <a href="#" class="btn btn-dark">
                    Comment
                    <i class="fa fa-w fa-comments"></i>
                </a>
            </div>
        </div>
    </div>
</template>
<script>
import axios from 'axios';

export default {
    name: "BlogDetail",
    data: function() {
        return {
            entry: null
        }
    },
    mounted() {
        axios
            .get('http://localhost:8000/blog/' + this.$route.params.id + '/')
            .then(response => (this.entry = response.data))
    },
};
</script>