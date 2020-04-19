<template>
    <div>
        <div v-for="entry in entries" :key="entry.index" class="card w-100" style="margin-bottom: 2rem">
            <div class="card-header">
                <strong>{{ entry.title }}</strong>
            </div>
            <div class="card-body">
                <p class="card-text">{{ entry.entry | truncate }}</p>
            </div>
            <div class="card-footer text-muted">
                <router-link class="btn btn-dark mr-2" :to='`/blog/${entry.id}/`'>
                    Read More
                    <i class="fa fa-w fa-arrow-right"></i>
                </router-link>
                <router-link class="btn btn-dark" :to='`/blog/${entry.id}/`'>
                    Comments
                    <i class="fa fa-w fa-comments"></i>
                    {{entry.comments.length}}
                </router-link>
            </div>
        </div>
    </div>
</template>
<script>
import axios from 'axios';

export default {
    name: "BlogList",
    data: function() {
        return {
            entries: null
        }
    },
    mounted() {
        axios
            .get('http://localhost:8000/api/blog/')
            .then(response => (this.entries = response.data))
    },
    filters: {
        truncate: function(value) {
            if (!value) return ''
            value = value.substring(0, 60)
            return value
        }
    }
};
</script>