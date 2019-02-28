<template>
  <v-container fill-height v-if="errors == null">
    <v-layout justify-center>

      <v-flex xs12 sm10 md8 lg6>

      <v-card>
	<v-card-title>
	    <h1> New Post </h1>
	  </v-card-title>
	  <v-card-text>

            <v-text-field
              label="Post title"
              single-line
              solo
            ></v-text-field>

      <v-flex lg12>
    <v-layout align-center justify-space-between>

        <v-flex lg12>
	   <v-menu
	      ref="menu"
	      v-model="menu"
	      :close-on-content-click="false"
	      :nudge-right="40"
	      :return-value.sync="date"
	      lazy
	      transition="scale-transition"
	      offset-y
	      full-width
	      min-width="290px"
	    >
	      <v-text-field
		slot="activator"
		v-model="date"
		label="Deadline"
		append-icon="event"
		readonly
		solo
	      ></v-text-field>
	      <v-date-picker v-model="date" color="#880E4F" scrollable>
		<v-spacer></v-spacer>
		<v-btn flat color="#880E4F" @click="menu = false">Cancel</v-btn>
		<v-btn flat color="#880E4F" @click="$refs.menu.save(date)">OK</v-btn>
	      </v-date-picker>
	    </v-menu>
	</v-flex>

        <v-flex lg12>
	     <v-overflow-btn
		:items="dropdown_icon"
		label="Preferred Contact"
		target="#dropdown-example"
		solo
	      ></v-overflow-btn>
	</v-flex>

        <v-flex lg12>
	       <v-overflow-btn
		:items="dropdown_icon"
		label="Request Type"
		target="#dropdown-example"
		solo
	      ></v-overflow-btn>
       </v-flex>

    </v-layout>
        <v-flex lg12>
          <v-textarea
            solo
	    counter=500
            name="input-7-4"
            label="Type your post's details..."
          ></v-textarea>
        </v-flex>
	</v-flex>
	</v-card-text>
	</v-card>

	</v-flex>


     
    </v-layout>
  </v-container>

</template>


<style scoped>

</style>


<script>

import { HTTP } from "../APIBase";

export default {
  name: 'PostCreate',
  data: () => ({
    date: new Date().toISOString().substr(0, 10),
    menu: false,
    title: "",
    details: "",
    deadline: "",
    request_type: "",
    zipcode: "",
    category: "",
    preferred_contact: "",
  })
  
}
</script>
