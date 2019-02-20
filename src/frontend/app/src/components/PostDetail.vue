<template>
  <v-container grid-list-md fill-height>
    <v-layout row wrap>
      
      <v-flex lg6>
        <h1 class="title"> {{ title }}</h1>
        <h4 class ="deadline">Deadline: {{ deadline }}</h4>
        
        <v-btn flat class="white--text" to='profile' color="pink darken-2" right>User Profile</v-btn>


        
        <p>A bunch of description things that make it look cool what else can you put in here </p>
        <p>A bunch of description things that make it look cool what else can you put in here </p>
        <p>A bunch of description things that make it look cool what else can you put in here </p>
        <p>A bunch of description things that make it look cool what else can you put in here </p>
        <p>A bunch of description things that make it look cool what else can you put in here </p>
        <p>A bunch of description things that make it look cool what else can you put in here </p>
        <p>A bunch of description things that make it look cool what else can you put in here </p>
        <p>{{ info }}</p>
        <p> {{errors}}</p>
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

export default {
  name: 'PostDetail',
  data: () => ({
    info: null, // To hold the data from our API call
    errors: null,
    title: "Some Title",
    details: "Details",
    deadline: "2/29/19",
    images:[ 
      {
        src: 'https://cdn.vuetifyjs.com/images/carousel/squirrel.jpg'
      },
      {
        src: 'https://cdn.vuetifyjs.com/images/carousel/sky.jpg'
      },
      {
        src: 'https://cdn.vuetifyjs.com/images/carousel/bird.jpg'
      },
      {
        src: 'https://cdn.vuetifyjs.com/images/carousel/planet.jpg'
      }
    ]

  }),
  created(){
    HTTP.get(`postdetails/1`)
    .then(response => (this.info = response))
    .catch(e =>{
      this.errors.push(e)
    })
  }
}
</script>
