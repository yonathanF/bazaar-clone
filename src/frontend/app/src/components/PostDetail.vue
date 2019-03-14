<template>
  <v-container grid-list-md fill-height v-if="errors == null">
    <v-layout row wrap>
      <v-flex lg6>
        <h1 class="title">{{ title }}</h1>
        <h1>Here: {{ post }}</h1>
        <h4 class="deadline">Deadline: {{ deadline }}</h4>

        <v-btn
          flat
          class="white--text"
          :to="{ path: `/profile/${user}` }"
          color="pink darken-2"
          right
          >User Profile</v-btn
        >

        <h3>{{ details }}</h3>
        <h3>{{ request_type }}</h3>
        <h3>{{ preferred_contact }}</h3>
        <h3>{{ zipcode }}</h3>
        <h3>{{ category }}</h3>
      </v-flex>
    </v-layout>
  </v-container>

  <h1 v-else>Something is wrong: {{ errors }}</h1>
</template>

<style scoped>
.title {
  font-size: 2.6em !important;
}
.deadline {
  font-size: 1em !important;
}
</style>

<script>
import { getPost } from "../services/PostService";

export default {
  name: "PostDetail",
  data: () => ({
    post: {},
    post_id: -1,
    errors: null
  }),
  created() {
    getPost(this.$route.params.post_id)
      .then(postData => {
        this.post = postData["post"];
        this.postId = postData["id"];
      })
      .catch(error => {
        this.errors = error;
      });
  }
};
</script>
