<template>
    <v-layout
      align-center 
      justify-space-between 
      row 
      >
      <v-flex> 
	<h1 class="category"> {{categoryName}}</h1> 
    <v-layout
      align-center 
      justify-space-between 
      row 
      >

    <v-flex
      v-for="post in categoryList"
      :key="post.id"
    >

    <v-card>
          <v-img
            src="https://cdn.vuetifyjs.com/images/cards/sunshine.jpg"
            height="200px"
          >
          </v-img>
  
          <v-card-title primary-title>
            <div>
	      <div class="headline">{{ post.title }}</div>
	      <span> {{ post.deadline }}</span>
	      <span> {{ post.zip_code}}</span>
	      <span> {{ post.request_type}}</span>
            </div>
          </v-card-title>
  
          <v-card-actions>
            <v-btn icon>
	      <v-icon>bookmark_border</v-icon>
	    </v-btn>
	    <v-btn  :to="{name:'postDetail', params: {post_id: post.id }}" flat color="pink darken-2">Details</v-btn>
            <v-spacer></v-spacer>
	  </v-btn>
          </v-card-actions>
  
        </v-card>           
	</v-flex>
	</v-layout>
	</v-flex>
    </v-layout>
</template>

<style scoped>
.category{
font:helvetica;
font-size: 1.7em;
color: #AD1457
}
</style>

<script>

  export default {
    name: 'Category',
    props: ['categoryName', 'categoryList'],
   }

  </script>
