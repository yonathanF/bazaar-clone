<template>
<div class ="overall">
  
  <h1 class="title"> {{ title }}</h1>
  <v-carousel height=300 interval=3000 max="400">
    <v-carousel-item
      v-for="(item,i) in images"
      :key="i"
      :src="item.src"
    ></v-carousel-item>
    
  </v-carousel>

  <div class="img"><v-img class="imgs" src="https://picsum.photos/510/300?random" height=300 width=300></v-img></div>
  
  <v-subheader> {{ details }} </v-subheader>
  <v-btn class="white--text" to='profile' color="pink darken-2" left=true>Profile</v-btn>
  
  <p>A bunch of description things that make it look cool what else can you put in here </p>
    <p>A bunch of description things that make it look cool what else can you put in here </p>
  <p>A bunch of description things that make it look cool what else can you put in here </p>
  <p>A bunch of description things that make it look cool what else can you put in here </p>
  <p>A bunch of description things that make it look cool what else can you put in here </p>
  <p>A bunch of description things that make it look cool what else can you put in here </p>
  <p>A bunch of description things that make it look cool what else can you put in here </p>

  

</div>
  
</template>
<style scoped>
  .overall{
    position: absolute;
    width: 100%;
    top: 30px;
  }
  .title{
    padding-bottom: 30px;
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
  }

  .imgs{
    border-radius: 50%;
  }
</style>



<script>
export default {
  data: () => ({
    info: null, // To hold the data from our API call
    title: "Some Title",
    details: "Details",
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

  })
  // mounted(){
  //   axios.get(`https://localhost:8000/api/v1/post/${route.params.post_id}`)
  //   .then(response => (this.info = response))
  // }
}
</script>
