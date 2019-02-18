<template>
<v-layout
          justify-start
	  column 
        >
	<v-flex
	   v-for="service in services" 
	    :key="service.title"
	  >
	  <Category :category-name="service.title"></Category>
	    </br> </br>
	</v-flex>

	<h1> {{ posts }} </h1>
	</v-layout>

</template>


<script>
import Category from './Category'
import {HTTP} from '../ApiServices';

export default {
  name: 'HomePage',
  props: ['serviceCategories'],
  components: {
    Category
  },

  data: () =>({
    posts: null,
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
    HTTP.get(`posts`)
    .then(response => {
      this.posts = response.data
    })
    .catch(e => {
      this.errors.push(e)
    })
  },
  methods: {
    goBack () {
      window.history.length > 1
        ? this.$router.go(-1)
        : this.$router.push('/')
    }
  }
}
</script>
