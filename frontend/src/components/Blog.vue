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
                <a href="" class="btn btn-dark mr-2">
                    Read More
                    <i class="fa fa-w fa-arrow-right"></i>
                </a>
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
    name: "Blog",
    data: function() {
        return {
            entries: null
        }
    },
    mounted() {
        axios
            .get('http://localhost:8000/blog/')
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