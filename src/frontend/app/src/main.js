import Vue from 'vue'
import './plugins/vuetify'
import App from './App.vue'
import HomePage from './components/HomePage'
import UserProfile from './components/UserProfile'
import UserComments from './components/UserComments'
import UserPosts from './components/UserPosts'
import AllCategory from './components/CategoryAll'
import PostDetail from './components/PostDetail'
import PostCreate from './components/PostCreate'
import Error404 from './components/Error404'
import VueRouter from 'vue-router'

Vue.config.productionTip = false

//Route setup
Vue.use(VueRouter)

const routes = [
  { path: '/', component: HomePage},
  { path: '/profile', component: UserProfile},
  { path: '/posts', component: UserPosts},
  { path: '/postCreate', component: PostCreate},
  { path: '/comments', component: UserComments},
  { path: '/category/:category_id', component: AllCategory},
  { path: '/postDetail/:post_id', name:'postDetail', component: PostDetail},
  { path: '*', component: Error404},
]

const router = new VueRouter({
  routes 
})


new Vue({
  router,
  render: h => h(App),
}).$mount('#app')


