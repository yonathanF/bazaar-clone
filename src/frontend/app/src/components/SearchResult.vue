<template>
  <v-layout justify-start column>
    <v-flex>
      <Category></Category>
    </v-flex>
  </v-layout>
</template>

<script>
import Category from "./Category";

export default {
  name: "SearchResult",
  components: {
    Category
  }
};
</script>
