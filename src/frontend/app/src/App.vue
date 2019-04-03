<template>
  <v-app v-if="isFullScreen()">
    <router-view />
  </v-app>
  <v-app v-else-if="!isFullScreen()" id="inspire">
    <v-navigation-drawer class="drawer" v-model="drawer" fixed app>
      <v-list>
        <v-list-group v-if="isAuthenticated()" no-action value="true">
          <v-list-tile slot="activator">
            <v-list-tile-content>
              <v-list-tile-title>Account</v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>

          <v-list-tile
            :to="info.url"
            v-for="info in account_info"
            :key="info.title"
          >
            <v-list-tile-action>
              <v-icon color="pink darken-2" medium>{{ info.icon }}</v-icon>
            </v-list-tile-action>
            <v-list-tile-content>
              <v-list-tile-title>{{ info.title }}</v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>

          <v-list-tile @click="logout()">
            <v-list-tile-action>
              <v-icon color="pink darken-2" medium>directions_walk</v-icon>
            </v-list-tile-action>
            <v-list-tile-content>
              <v-list-tile-title>Logout</v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>
        </v-list-group>

        <v-list-group no-action value="true">
          <v-list-tile slot="activator">
            <v-list-tile-content>
              <v-list-tile-title>Categories</v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>

          <v-list-tile
            :to="service.category_url"
            v-for="service in services"
            :key="service.title"
          >
            <v-list-tile-action>
              <v-icon color="pink darken-2" medium>{{ service.icon }}</v-icon>
            </v-list-tile-action>
            <v-list-tile-content>
              <v-list-tile-title>{{ service.title }}</v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>
        </v-list-group>
      </v-list>
    </v-navigation-drawer>
    <v-toolbar class="toolbar" dark fixed app>
      <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
      <v-toolbar-title
        ><router-link class="toolbar-title" to="/"
          >Bazaar</router-link
        ></v-toolbar-title
      >
      <v-spacer></v-spacer>

      <router-link :to="{ name: 'createPost' }">
        <v-btn v-if="isAuthenticated()" round light>Create Post</v-btn>
      </router-link>

      <router-link :to="{ name: 'createPost' }">
        <v-btn v-if="!isAuthenticated()" round light>Login to Post</v-btn>
      </router-link>
    </v-toolbar>
    <v-content>
      <v-container grid-list-lg wrap fill-height>
        <router-view />
      </v-container>
    </v-content>
    <v-footer class="footer" app>
      <v-spacer></v-spacer>
      <span class="white--text"
        >&copy; Bazaar {{ new Date().getFullYear() }}</span
      >
    </v-footer>
  </v-app>
</template>

<style scoped>
#app {
  font: helvetica;
}
.footer {
  background-color: #880e4f;
}

.drawer {
  background-color: #ffffff;
}

.toolbar {
  background-color: #880e4f;
}

.toolbar-title {
  color: #ffffff;
  text-decoration-color: #880e4f;
  font-size: 1.4em;
}

.drawer-list {
  color: #000000;
}
</style>

<script>
import HomePage from "./components/HomePage";
import PostDetail from "./components/PostDetail";
import { isAuthenticated } from "./services/AuthService";
import { logout } from "./services/AuthService";
import { router } from "./routers/MainRouter";

export default {
  name: "App",
  components: {
    HomePage,
    PostDetail
  },
  data: () => ({
    drawer: null,
    auth: false,
    account_info: [
      {
        title: "Profile",
        url: "/profile",
        icon: "account_circle"
      },
      {
        title: "Posts",
        url: "/posts",
        icon: "notes"
      },
      {
        title: "Comments",
        url: "/comments",
        icon: "comment"
      }
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
      }
    ]
  }),
  props: {
    source: String
  },
  methods: {
    isAuthenticated() {
      return isAuthenticated();
    },
    isFullScreen() {
      let name = this.$router.currentRoute.name;
      return name === "login" || name === "register";
    },
    logout() {
      logout();
      router.push({ name: "login" });
    }
  }
};
</script>
