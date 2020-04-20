<template>
    <div>
        <div class="card w-100" v-if="entry">
            <div class="card-header">
                <h3 style="text-align: center"><strong>{{ entry.title }}</strong></h3>
            </div>
            <div class="card-body">
                <p class="card-text" style="white-space: pre-wrap;">
                    {{ entry.entry }}
                </p>
            </div>
            <div class="card-footer text-muted">
                <router-link class="btn btn-dark mr-2" :to="{name: 'Blog'}">
                    <i class="fa fa-arrow-left fa-w"></i>
                </router-link>
                <button v-on:click="new_comment = !new_comment" class="btn btn-dark">
                    Comment
                    <i class="fa fa-w fa-comments"></i>
                </button>
            </div>
        </div>
        <div v-if="new_comment" class="mt-3 form-group card p-4">
            <h5>New Comment: </h5>
            <form>
                <label for="email_input">Email address</label>
                <input type="email" class="form-control" id="email_input" placeholder="Enter email" v-model="email">
                <label for="name">User Name</label>
                <input type="" class="form-control" id="name" placeholder="Enter Display Name" v-model="name">
                <label for="comment">Comment</label>
                <textarea class="form-control" id="comment" rows="3" v-model="comment"></textarea>
                <button v-on:click.prevent="submit_comment" class="btn btn-primary mt-3">Submit</button>
            </form>
        </div>
        <div v-for="comment in entry.comments" :key="comment.id" class="card w-100 mt-3">
            <div class="card-header">
                {{comment.user_name}}:
            </div>
            <div class="card-body">
                {{comment.comment}}
            </div>
            <div class="card-footer">
                {{comment.publish_date | moment}}
            </div>
        </div>
    </div>
</template>
<script>
import axios from 'axios';
import moment from 'moment';

export default {
    name: "BlogDetail",
    data: function() {
        return {
            entry: '',
            new_comment: false, 
            name: '',
            comment: '',
            email: '',
        }
    },
    mounted() {
        this.getComments()
    },
    filters: {
        moment: function(value) {
            return moment(value).format('MM/D/YYYY');
        }
    },
    methods: {
        getComments: function() {
            axios
                .get('http://localhost:8000/api/blog/' + this.$route.params.id + '/')
                .then(response => (this.entry = response.data))
        },
        submit_comment: function() {
            var data = {
                'user_name': this.name,
                'comment': this.comment,
                'email': this.email,
                'parent': this.entry.id,
                'publish_data': '',
            }

            axios
                .post("http://localhost:8000/api/comment/", data)
                .then(() => {
                    this.new_comment = false;
                    this.getComments();
                })
        }
    }
};
</script>