<template>
  <v-container grid-list-md fill-height v-if="errors == null">
    <v-layout row wrap>
      
      <v-flex lg6>
        <h1 class="title"> {{ title }}</h1>
        {{this.$route.params.post_id}}
        <h4 class ="deadline">Deadline: {{ deadline }}</h4>
        
        <v-btn flat class="white--text" :to="{path: `/profile/${user}`}" color="pink darken-2" right>User Profile</v-btn>

        <h3> {{ details }} </h3>
        <h3> {{ request_type }} </h3>
        <h3> {{ preferred_contact }} </h3>
        <h3> {{ zipcode }} </h3>
        <h3> {{ category }} </h3>

      </v-flex>

         <v-flex lg6>
      <v-card>
        <v-container grid-list-sm fluid>
          <v-layout row wrap>
            <v-flex
              v-for="n in 9"
              :key="n"
              xs4
              d-flex
            >
              <v-card flat tile class="d-flex">
                <v-img
                  :src="`https://picsum.photos/500/300?image=${n * 5 + 10}`"
                  :lazy-src="`https://picsum.photos/10/6?image=${n * 5 + 10}`"
                  aspect-ratio="1"
                  class="grey lighten-2"
                >
                  <v-layout
                    slot="placeholder"
                    fill-height
                    align-center
                    justify-center
                    ma-0
                  >
                    <v-progress-circular indeterminate color="grey lighten-5"></v-progress-circular>
                  </v-layout>
                </v-img>
              </v-card>
            </v-flex>
          </v-layout>
        </v-container>
      </v-card>
    </v-flex>


     
    </v-layout>
  </v-container>

  <h1 v-else>{{ errors }} </h1>
  
</template>


<style scoped>
 .title{
    font-size: 2.6em !important;
  }
  .deadline{
    font-size: 1em !important;
  }
</style>


<script>

import { HTTP } from "../APIBase";

export default {
  name: 'PostCreate',
  data: () => ({
    title: "",
    details: "",
    deadline: "",
    request_type: "",
    zipcode: "",
    category: "",
    images:[]
  })
  
}
</script>
