<template>
<v-layout
          justify-start
	  column 
        >
	<v-flex
		id = "post_id"
	   v-for="(post, category) in posts" 
	    :key="post.id"
	  >

<v-layout justify-end align-end>
  <v-btn class="headline" medium round solo dark color="pink darken-2">
    {{ category }}<v-icon right>arrow_forward</v-icon>
        </v-btn>
	</v-layout>
		<div id="category">
	  <Category :category-list="post" :category-name="category"> </Category>
	  </div>
	    </br> </br>
	</v-flex>

	</v-layout>

</template>


<script>
import Category from './Category';
import {getHomepagePosts} from '../services/PostService';

export default {
  name: 'HomePage',
  props: ['serviceCategories'],
  components: {
    Category
  },

  data: () =>({
      posts: [],
      errors: [],
  services: [
           {
             title: "IT Consultation",
	     icon: "desktop_mac"
	   },
	   {
             title: "Events",
	     icon: "event"
	   },
	   {
	     title: "Tutoring",
	     icon: "supervisor_account" 
	   },
           {
	     title: "Lifestyle",
	     icon: "linked_camera" 
	   },
           {
	     title: "Art",
	     icon: "palette" 
	   },
           {
	     title: "Household",
	     icon: "home" 
	   },

           {
	     title: "Labor",
	     icon: "directions_run" 
	   },
           {
	     title: "Pets",
	     icon: "pets" 
	   },
           {
	     title: "Automotives",
	     icon: "local_car_wash" 
	   },

      ]

  }),

  created() {
    getHomepagePosts(4)
      .then(data => {
	this.posts= data 
      })
      .catch(e => {
	this.errors.push(e)
      });
    }
}
</script>
