<template>
  <v-container fill-height>
    <v-layout align-center justify-center>
      <v-flex xs6 lg3>
        <v-card>
          <v-card-title>
            <h1 class="new-post">Register with Bazaar</h1>
          </v-card-title>
          <v-card-text>
            <v-flex lg12>
              <v-text-field
                id="name"
                label="First name"
                v-model="firstname"
                single-line
                solo
                required
                :rules="[rules.required]"
              ></v-text-field>
            </v-flex>

            <v-flex lg12>
              <v-text-field
                id="last_name"
                label="Last name"
                v-model="lastname"
                single-line
                solo
                required
                :rules="[rules.required]"
              ></v-text-field>
            </v-flex>

            <v-flex lg12>
              <v-text-field
                id="email"
                label="Email"
                v-model="email"
                single-line
                solo
                required
                :rules="[rules.required]"
              ></v-text-field>
            </v-flex>

            <v-flex lg12>
              <v-text-field
                id="password"
                label="Password"
                v-model="password"
                :append-icon="show1 ? 'visibility' : 'visibility_off'"
                :rules="[rules.required, rules.min]"
                :type="show1 ? 'text' : 'password'"
                single-line
                solo
                required
                @click:append="show1 = !show1"
              ></v-text-field>
            </v-flex>
            <v-flex>
              <ul>
                <li v-for="(key, value) in errors">{{ value }} is required.</li>
              </ul>
            </v-flex>

            <v-flex lg12>
              <v-btn
                id="register"
                :disabled="invalid_form"
                color="#880E4F"
                class="white--text"
                block
                large
                @click="sendUser()"
                >Register</v-btn
              >
            </v-flex>
            <v-flex>
              <router-link to="/login/"
                >Already have an account? Login!</router-link
              >
            </v-flex>
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<style scoped>
.new-post {
  font-size: 2.3em;
  color: #880e4f;
}
</style>

<script>
import { register } from "../services/AuthService";
import { router } from "../routers/MainRouter";

export default {
  name: "RegisterPage",
  data: () => ({
    errors: "",
    post: "",
    show1: false,
    password: "",
    email: "",
    firstname: "",
    lastname: "",
    rules: {
      required: value => !!value || "Required.",
      min: v => v.length >= 8 || "Min 8 characters",
      emailMatch: () => "The email and password you entered don't match"
    }
  }),
  methods: {
    sendUser() {
      var firstname = this.$data.firstname;
      var lastname = this.$data.lastname;
      var email = this.$data.email;
      var password = this.$data.password;
      register(firstname, lastname, email, password)
        .then(data => {
          this.$data.post = data;
          router.push({ name: "home" });
        })
        .catch(e => {
          this.$data.errors = e["response"]["data"]["Status"];
        });
    }
  }
};
</script>
