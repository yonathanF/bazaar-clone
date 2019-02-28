<template>
  <v-container grid-list-md fill-height v-if="errors == null">
    <v-layout row wrap>
      <v-form>

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
            label="Picker in menu"
            prepend-icon="event"
            readonly
          ></v-text-field>
          <v-date-picker v-model="date" color="#880E4F" scrollable>
            <v-spacer></v-spacer>
            <v-btn flat color="#880E4F" @click="menu = false">Cancel</v-btn>
            <v-btn flat color="#880E4F" @click="$refs.menu.save(date)">OK</v-btn>
          </v-date-picker>
        </v-menu>
	</v-form>


     
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
    images:[]
  })
  
}
</script>
