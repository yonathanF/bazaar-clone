import Vue from "vue";
import "./plugins/vuetify";
import App from "./App.vue";
import { router } from "./routers/MainRouter";

Vue.config.productionTip = false;
Vue.use(require("vue-moment"));

new Vue({
  router,
  render: h => h(App)
}).$mount("#app");
