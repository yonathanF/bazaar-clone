<template>
  <v-layout row wrap>
    <v-flex>
      <v-layout justify-right row>
        <h4 class="searchTitle display-1" style="padding:15px">
          Search result for: {{ getKeywords() }}
        </h4>
      </v-layout>
      <Category :category-list="posts"></Category>
    </v-flex>
  </v-layout>
</template>

<style scoped>
.searchTitle {
  color: #ad1457;
}
</style>

<script>
import Category from "./Category";
import { searchPost } from "../services/PostService";
import { router } from "../routers/MainRouter";

export default {
  name: "SearchResult",
  components: {
    Category
  },

  data: () => ({
    posts: []
  }),
  watch: {
    $route(to, from) {
      if (to.name === "search") {
        var x = to.params.keywords;
        searchPost(x)
          .then(searchResults => {
            this.$data.posts = searchResults["posts"];
          })
          .catch(e => {
            console.log(e);
          });
      }
    }
  },
  created: function() {
    searchPost(this.$route.params.keywords)
      .then(searchResults => {
        this.$data.posts = searchResults["posts"];
      })
      .catch(e => {
        console.log(e);
      });
  },
  methods: {
    getKeywords() {
      return this.$route.params.keywords;
    }
  }
};
</script>
