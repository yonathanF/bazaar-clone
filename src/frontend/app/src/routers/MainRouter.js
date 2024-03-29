import HomePage from "../components/HomePage";
import UserProfile from "../components/UserProfile";
import UserComments from "../components/UserComments";
import UserPosts from "../components/UserPosts";
import AllCategory from "../components/CategoryAll";
import PostDetail from "../components/PostDetail";
import PostCreate from "../components/PostCreate";
import Error404 from "../components/Error404";
import LoginPage from "../components/LoginPage";
import RegisterPage from "../components/RegisterPage";
import SearchResult from "../components/SearchResult";
import VueRouter from "vue-router";
import { isAuthenticated } from "../services/AuthService";
import Vue from "vue";

//Route setup
Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    component: HomePage,
    name: "home",
    meta: { title: "Bazaar | Your Homepage", requiresAuth: false }
  },
  {
    path: "/profile",
    component: UserProfile,
    name: "profile",
    meta: { title: "Bazaar | Your Profile", requiresAuth: true }
  },
  {
    path: "/posts",
    component: UserPosts,
    name: "userPosts",
    meta: { title: "Bazaar | Your Posts", requiresAuth: true }
  },
  {
    path: "/postCreate",
    component: PostCreate,
    name: "createPost",
    meta: { title: "Bazaar | Create Post", requiresAuth: true }
  },
  {
    path: "/comments",
    component: UserComments,
    name: "userComments",
    meta: { title: "Bazaar | Your Comments", requiresAuth: true }
  },
  {
    path: "/category/:category_id",
    name: "catgory",
    component: AllCategory,
    meta: { title: "Bazaar | Posts", requiresAuth: false }
  },
  {
    path: "/postDetail/:post_id",
    name: "postDetail",
    component: PostDetail,
    meta: { title: "Bazaar | Post Detail", requiresAuth: false }
  },
  {
    path: "/login/",
    name: "login",
    component: LoginPage,
    meta: { title: "Bazaar | Login", requiresAuth: false }
  },
  {
    path: "/search/:keywords",
    name: "search",
    component: SearchResult,
    meta: { title: "Bazaar | Search", requiresAuth: false }
  },
  {
    path: "/register",
    name: "register",
    component: RegisterPage,
    meta: { title: "Bazaar | Register", requiresAuth: false }
  },
  { path: "*", component: Error404, requiresAuth: false }
];

export const router = new VueRouter({
  routes
});

router.beforeEach((to, from, next) => {
  if (!isAuthenticated() && to.meta.requiresAuth) {
    return next({
      name: "login",
      query: { returnUrl: to.path }
    });
  }

  document.title = to.meta.title;
  next();
});
