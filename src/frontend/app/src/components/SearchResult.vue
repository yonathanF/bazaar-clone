<template>
  <v-layout justify-start column>
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

export default {
  name: "SearchResult",
  components: {
    Category
  },

  data: () => ({
    posts: [
      {
        date_posted: "2019-04-03T22:20:29.828Z",
        details: "I can help you improve your home",
        zip_code: 80012,
        title: "Home improvement project",
        user: 1,
        deadline: "2019-04-24",
        preferred_contact: "Email",
        category: "Labor",
        request_type: "Offering",
        id: 2
      },

      {
        date_posted: "2019-04-03T22:20:29.828Z",
        details: "I can help you improve your home",
        zip_code: 80012,
        title: "Home improvement project",
        user: 1,
        deadline: "2019-04-24",
        preferred_contact: "Email",
        category: "Labor",
        request_type: "Offering",
        id: 1
      }
    ]
  }),
  methods: {
    getKeywords() {
      console.log("test: " + this.$route.query.keywords);
      return this.$route.params.keywords;
    }
  }
};
</script>
