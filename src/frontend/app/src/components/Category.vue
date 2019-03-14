<template>
    <v-layout
      align-center 
      justify-space-between 
      row 
      >
      <v-flex> 
	<v-layout justify-end align-end>
  <v-btn class="headline" round flat dark color="pink darken-2">
    {{ categoryName}}<v-icon right>arrow_forward</v-icon>
        </v-btn>
	</v-layout>

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
	    <v-flex>
	      <div class="headline">{{ post.title }}</div>
	      </v-flex>
	      <v-layout justify-start row fill-height>
		<v-flex>

		<v-chip small flat dark color="pink lighten-1">

		    <v-icon small left>calendar_today</v-icon>
		<span class="font-weight-light">{{ post.deadline | moment("MMMM Do") }} </span>

		</v-chip>
		</v-flex>

		<v-flex>

		<v-chip dark small flat color="pink lighten-1">

		    <v-icon small left>how_to_reg</v-icon>
		<span class="font-weight-light"> {{ post.request_type}}</span>

		</v-chip>
		</v-flex>
		<v-flex>
		<v-chip small flat dark color="pink lighten-1">
		    <v-icon small left>person_pin_circle</v-icon>
		<span class="font-weight-light"> {{ post.zip_code}}</span>
		</v-chip>
		</v-flex>
	      </v-layout>

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
