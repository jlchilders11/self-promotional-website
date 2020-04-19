<template>
    <div>
        <div class="card w-100">
            <div class="card-header">
                <h1><strong>{{ entry.title }}</strong></h1>
            </div>
            <div class="card-body">
                <p class="card-text">{{ entry.entry }}</p>
            </div>
            <div class="card-footer text-muted">
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