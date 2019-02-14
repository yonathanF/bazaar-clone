<template>
    <v-layout
      align-center 
      justify-space-between 
      row 
      >
      <v-flex> 

	<h1> {{ categoryName }}</h1>
     <v-layout
      align-center 
      justify-space-between 
      row 
      >

    <v-flex
      v-for="post in posts"
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
              <div class="headline">Top western road trips</div>
              <span class="grey--text">1,000 miles of wonder</span>
            </div>
          </v-card-title>
  
          <v-card-actions>
            <v-btn icon>
	      <v-icon>bookmark_border</v-icon>
	    </v-btn>
            <v-btn flat color="pink darken-4">Details</v-btn>
            <v-spacer></v-spacer>
	  </v-btn>
          </v-card-actions>
  
        </v-card>           
	</v-flex>
	</v-layout>
	</v-flex>
    </v-layout>
</template>

  <script>
  export default {
    props: ['categoryName'],
    data: () => ({
        posts: [
            {
	      id: 1,
	      title: "title"
	    },
            {
	      id: 2,
	      title: "title"
	    },
	    {
	      id: 3,
	      title: "title"
	    },
            {
	      id: 4,
	      title: "title"
	    },
            
	]
    })

   }

  </script>
