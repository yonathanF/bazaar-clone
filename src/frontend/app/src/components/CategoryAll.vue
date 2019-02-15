<template>
  <v-layout
      justify-start
      column 
   >
     <v-flex >
	<Category category-name="service.title"></Category>
     </v-flex>


  </v-layout>

</template>

<script>
import Category from './Category'

export default {
  name: 'CategoryAll',
  components: {
    Category
  },
}

</script>
