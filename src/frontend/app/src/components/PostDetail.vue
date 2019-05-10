<template>
  <v-container grid-list-md fill-height v-if="errors == null">
    <v-layout align-start justify-center column fill-height>
      <v-flex sm8 lg11>
        <v-card>
          <v-card-title class="display-2">
            {{ post.title }}
          </v-card-title>

          <v-card-text>
            <v-flex lg9>
              <v-layout justify-start row>
                <v-tooltip top>
                  <template v-slot:activator="{ on }">
                    <v-chip color="pink lighten-1" v-on="on" text-color="white">
                      <v-avatar>
                        <v-icon small>calendar_today</v-icon>
                      </v-avatar>

                      {{ post.deadline | moment("dddd, MMMM Do") }}
                    </v-chip>
                  </template>
                  <span>Deadline</span>
                </v-tooltip>

                <v-tooltip top>
                  <template v-slot:activator="{ on }">
                    <v-chip color="pink lighten-1" v-on="on" text-color="white">
                      <v-avatar>
                        <v-icon small>how_to_reg</v-icon>
                      </v-avatar>
                      {{ post.request_type }}
                    </v-chip>
                  </template>
                  <span>Request Type</span>
                </v-tooltip>

                <v-tooltip top>
                  <template v-slot:activator="{ on }">
                    <v-chip color="pink lighten-1" v-on="on" text-color="white">
                      <v-avatar>
                        <v-icon small>contacts</v-icon>
                      </v-avatar>
                      {{ post.preferred_contact }}
                    </v-chip>
                  </template>
                  <span>Preferred Contact</span>
                </v-tooltip>

                <v-tooltip top>
                  <template v-slot:activator="{ on }">
                    <v-chip color="pink lighten-1" v-on="on" text-color="white">
                      <v-avatar>
                        <v-icon small>pets</v-icon>
                      </v-avatar>
                      {{ post.category }}
                    </v-chip>
                  </template>
                  <span>Category</span>
                </v-tooltip>

                <v-tooltip top>
                  <template v-slot:activator="{ on }">
                    <v-chip color="pink lighten-1" v-on="on" text-color="white">
                      <v-avatar>
                        <v-icon small>person_pin_circle</v-icon>
                      </v-avatar>
                      {{ post.zip_code }}
                    </v-chip>
                  </template>
                  <span>Zip code</span>
                </v-tooltip>
              </v-layout>

              <v-layout>
                <div class="post-detail">
                  <p>
                    {{ post.details }}
                  </p>
                </div>
              </v-layout>
            </v-flex>
          </v-card-text>
        </v-card>
      </v-flex>

      <h2>Recommended Posts</h2>
      <v-flex>
        <Category :category-list="post.recommendations"> </Category>
      </v-flex>
    </v-layout>
  </v-container>

  <h1 v-else>Something is wrong: {{ errors }}</h1>
</template>

<style scoped>
.post-detail {
  border-style: solid none none none;
  border-width: 1px;
  margin: 10px;
  padding: 15px 0px 0px 0px;
}
</style>

<script>
import { getPost } from "../services/PostService";
import Category from "./Category";

export default {
  name: "PostDetail",
  components: {
    Category
  },

  data: () => ({
    post: {},
    post_id: -1,
    errors: null
  }),
  watch: {
    $route(to, from) {
      next();
    }
  },

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
