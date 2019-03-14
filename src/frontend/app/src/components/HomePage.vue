<template>
<v-layout
          justify-start
	  column 
        >
	<v-flex
	   v-for="(post, category) in posts" 
	    :key="post.id"
	  >


	  <Category :category-list="post" :category-name="category"> </Category>
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
