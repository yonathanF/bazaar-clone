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
  
<!-- 
  
  
  <div class="img"><v-img class="imgs" src="https://picsum.photos/510/300?random" height=300 width=300></v-img></div>
  

   -->

  
</template>
<style scoped>
 .title{
    font-size: 2.6em !important;
  }
  .deadline{
    font-size: 1em !important;
  }
  /* .overall{
    position: absolute;
    width: 100%;
    top: 30px;
  }
  
  .v-carousel{
    width: 500px;
    display: inline-block;
  }

  .v-btn{
    position:absolute;
    width: 400px;
    left: 50%;
  }
  .img{
    position: absolute;
    display: inline-block;
    right: 28%;
  } */
</style>


<script>


import { HTTP } from "../APIBase";

var Categories = {
        "LI": "Lifestyle",
        "IT": "IT Consultation",
        "EV": "Events",
        "TU": "Tutoring",
        "AR": "Art",
        "HO": "Household",
        "LB": "Labor",
        "OT": "Other",
}

var Type = {
  "OF": "Offering",
  "AS": "Asking",
}  

export default {
  name: 'PostDetail',
  data: () => ({
    info: [], // To hold the data from our API call
    errors: null,
    title: "",
    details: "",
    deadline: "",
    user: "",
    request_type: "",
    date_posted: "",
    zipcode: "",
    category: "",
    images:[]
  }),
  created(){
    HTTP.get(`postdetails/${this.$route.params.post_id}`)
    .then(response => {
      this.info = response
    })
    .then(response => {
      this.details = this.info['data'][1]['post']['details']
      this.title = this.info['data'][1]['post']['title']
      this.deadline = this.info['data'][1]['post']['deadline']
      this.user = String(this.info['data'][1]['post']['user'])
      this.request_type = this.info['data'][1]['post']['request_type']
      this.date_posted = this.info['data'][1]['post']['date_posted']
      this.zipcode = this.info['data'][1]['post']['zip_code']
      this.category = this.info['data'][1]['post']['category']
    })
    .then(response => {
      this.request_type = Type[this.request_type]
      this.category = Categories[this.category]
    })
    .catch(e =>{
      this.errors = "That post does not exist"
    })
  }
}
</script>
