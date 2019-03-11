import Vue from "vue";
import "./plugins/vuetify";
import App from "./App.vue";
import HomePage from "./components/HomePage";
import UserProfile from "./components/UserProfile";
import UserComments from "./components/UserComments";
import UserPosts from "./components/UserPosts";
import AllCategory from "./components/CategoryAll";
import PostDetail from "./components/PostDetail";
import PostCreate from "./components/PostCreate";
import Error404 from "./components/Error404";
import LoginPage from "./components/LoginPage";
import RegisterPage from "./components/RegisterPage";
import VueRouter from "vue-router";

Vue.config.productionTip = false;

//Route setup
Vue.use(VueRouter);

const routes = [
  { path: "/", component: HomePage, meta: { title: "Bazaar | Your Homepage" } },
  {
    path: "/profile",
    component: UserProfile,
    meta: { title: "Bazaar | Your Profile" }
  },
  {
    path: "/posts",
    component: UserPosts,
    meta: { title: "Bazaar | Your Posts" }
  },
  {
    path: "/postCreate",
    component: PostCreate,
    meta: { title: "Bazaar | Create Post" }
  },
  {
    path: "/comments",
    component: UserComments,
    meta: { title: "Bazaar | Your Comments" }
  },
  {
    path: "/category/:category_id",
    component: AllCategory,
    meta: { title: "Bazaar | Posts" }
  },
  {
    path: "/postDetail/:post_id",
    name: "postDetail",
    component: PostDetail,
    meta: { title: "Bazaar | Post Detail" }
  },
  {
    path: "/login/",
    name: "login",
    component: LoginPage,
    meta: { title: "Bazaar | Login" }
  },
  {
    path: "/register/",
    name: "register",
    component: RegisterPage,
    meta: { title: "Bazaar | Register" }
  },
  { path: "*", component: Error404 }
];

const router = new VueRouter({
  routes
});

router.beforeEach((to, from, next) => {
  document.title = to.meta.title;
  next();
});

new Vue({
  router,
  render: h => h(App)
}).$mount("#app");
