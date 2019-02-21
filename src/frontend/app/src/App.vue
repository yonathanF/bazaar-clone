<template>
  <v-app id="inspire">
    <v-navigation-drawer
      class="drawer"
      v-model="drawer"
      fixed
      app
    >
      <v-list>
    <v-list-group
       no-action
      value=true
      >
       <v-list-tile slot="activator">
       <v-list-tile-content>
                  <v-list-tile-title>Account</v-list-tile-title>
                </v-list-tile-content>
        </v-list-tile>

        <v-list-tile :to="info.url" 
	  v-for="info in account_info" 
 	   :key="info.title"
	  >
          <v-list-tile-action>
	    <v-icon color="pink darken-2" medium >{{ info.icon }}</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
	    <v-list-tile-title>{{ info.title }}</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>

  </v-list-group>

    <v-list-group
       no-action
      value=true
      >
        <v-list-tile slot="activator">
                <v-list-tile-content>
                  <v-list-tile-title>Categories</v-list-tile-title>
                </v-list-tile-content>
        </v-list-tile>


        <v-list-tile :to="service.category_url" 
	   v-for="service in services" 
 	   :key="service.title"
	  >
          <v-list-tile-action>
	    <v-icon color="pink darken-2" medium>{{ service.icon }}</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
	    <v-list-tile-title >{{ service.title }}</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
   </v-list-group>

      </v-list>
    </v-navigation-drawer>
    <v-toolbar class="toolbar" dark fixed app>
      <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>   
      <v-toolbar-title><router-link class="toolbar-title" to="/">Bazaar</router-link></v-toolbar-title>
    </v-toolbar>
    <v-content>
      <v-container grid-list-lg wrap fill-height>
	<!--<HomePage :service-categories=services> </HomePage>-->
      	<router-view/>
      </v-container>
    </v-content>
    <v-footer class="footer" app>
     <v-spacer></v-spacer>
      <span class="white--text">&copy; Bazaar {{ new Date().getFullYear() }}</span>
    </v-footer>
  </v-app>
</template>

<style scoped>
#app{
font:helvetica
}
.footer{
background-color: #880E4F 
}

.drawer{
background-color: #FFFFFF
}

.toolbar{
background-color: #880E4F 
}

.toolbar-title{
color: #FFFFFF;
text-decoration-color: #880E4F;
font-size: 1.4em;
}

.drawer-list{
color: #000000
}
</style>

<script>
import HomePage from './components/HomePage'
import PostDetail from './components/PostDetail'

export default {
  name: 'App',
  components: {
     HomePage,
     PostDetail
  },
  data: () => ({
      drawer: null,
      account_info: [
        {
          title: "Profile",
	  url: "/profile",
	  icon: "account_circle" 
	} ,
	{
          title: "Posts",
	  url: "/posts",
	  icon: "notes"
	},
	{
          title: "Comments",
	  url: "/comments",
	  icon: "comment"
	},
      ],
      services: [
           {
             title: "IT Consultation",
	     category_url: "/category/1",
	     icon: "desktop_mac"
	   },
	   {
             title: "Events",
	     category_url: "/category/2",
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
    props: {
      source: String
    }
}
</script>
