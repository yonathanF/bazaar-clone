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
import VueRouter from "vue-router";
import { isAuthenticated } from "../services/AuthService";
import Vue from "vue";

//Route setup
Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    component: HomePage,
    meta: { title: "Bazaar | Your Homepage", requiresAuth: true }
  },
  {
    path: "/profile",
    component: UserProfile,
    meta: { title: "Bazaar | Your Profile", requiresAuth: true }
  },
  {
    path: "/posts",
    component: UserPosts,
    meta: { title: "Bazaar | Your Posts", requiresAuth: true }
  },
  {
    path: "/postCreate",
    component: PostCreate,
    meta: { title: "Bazaar | Create Post", requiresAuth: true }
  },
  {
    path: "/comments",
    component: UserComments,
    meta: { title: "Bazaar | Your Comments", requiresAuth: true }
  },
  {
    path: "/category/:category_id",
    component: AllCategory,
    meta: { title: "Bazaar | Posts", requiresAuth: true }
  },
  {
    path: "/postDetail/:post_id",
    name: "postDetail",
    component: PostDetail,
    meta: { title: "Bazaar | Post Detail", requiresAuth: true }
  },
  {
    path: "/login/",
    name: "login",
    component: LoginPage,
    meta: { title: "Bazaar | Login", requiresAuth: false }
  },
  {
    path: "/register/",
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
