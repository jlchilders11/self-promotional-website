<template>
    <div class="row">
        <div v-for="project in projects" :key="project.index" class="col-sm-12 col-md-6 col-lg-3 mb-4">
            <div class="card h-100">
                <div class="card-header">
                    <strong>{{project.name | dashtospace }}</strong>
                </div>
                <div class="card-body">
                    <p class="card-text">{{project.description}}</p>
                </div>
                <div class="card-footer text-muted">
                    <a :href="project.html_url" target="_" class="btn btn-dark mr-2">
                        <i class="fa fa-w fa-github"></i>
                        GitHub
                    </a>
                    {{project.updated_at | moment }}
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import axios from 'axios';
import moment from 'moment';

export default {
    name: "Projects",
    data: function() {
        return {
            projects: null
        }
    },
    mounted() {
        axios
            .get('https://api.github.com/users/jlchilders11/repos')
            .then(response => (this.projects = response.data.reverse()))

    },
    filters: {
        dashtospace: function(value) {
            if (!value) return ''
            value = value.replace(/-/g, ' ');
            return value
        },
        moment: function(value) {
            return moment(value).format('MM/D/YYYY');
        }
    }
};
</script>