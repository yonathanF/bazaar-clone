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
                  <v-list-tile-title>Profile</v-list-tile-title>
                </v-list-tile-content>
        </v-list-tile>

        <v-list-tile @click="">
          <v-list-tile-action>
            <v-icon color="pink darken-2" medium >account_circle</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>Account</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>

        <v-list-tile @click="">
          <v-list-tile-action>
            <v-icon color="pink darken-2" medium >notes</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>Posts</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>


        <v-list-tile @click="">
          <v-list-tile-action>
            <v-icon color="pink darken-2" medium >comment</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>Comments</v-list-tile-title>
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


        <v-list-tile @click="">
          <v-list-tile-action>
            <v-icon color="pink darken-2" medium>desktop_mac</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>Tech</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
   </v-list-group>

      </v-list>
    </v-navigation-drawer>
    <v-toolbar class="toolbar" dark fixed app>
      <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
      <v-toolbar-title>Application</v-toolbar-title>
    </v-toolbar>
    <v-content>
      <v-container fluid fill-height>
        <v-layout
          justify-center
          align-center
        >
          <v-flex text-xs-center>
            <v-tooltip left>
              <v-btn slot="activator" :href="source" icon large target="_blank">
                <v-icon large>code</v-icon>
              </v-btn>
              <span>Source</span>
            </v-tooltip>
            <v-tooltip right>
              <v-btn slot="activator" icon large href="https://codepen.io/johnjleider/pen/rJdVMq" target="_blank">
                <v-icon large>mdi-codepen</v-icon>
              </v-btn>
              <span>Codepen</span>
            </v-tooltip>
          </v-flex>
        </v-layout>
      </v-container>
    </v-content>
    <v-footer class="footer" app>
      <span class="white--text">&copy; Bazaar 2019</span>
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
</style>

<script>
import HelloWorld from './components/HelloWorld'

export default {
  name: 'App',
  components: {
    HelloWorld
  },
  data: () => ({
      drawer: null
    }),
    props: {
      source: String
    }
}
</script>
