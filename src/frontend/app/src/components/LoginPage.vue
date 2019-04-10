<template>
  <v-container fill-height>
    <v-layout align-center justify-center>
      <v-flex xs6 lg3>
        <v-card>
          <v-card-title>
            <h1 class="new-post">Login to Bazaar</h1>
          </v-card-title>
          <v-card-text>
            <v-flex lg12>
              <v-text-field
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
                label="Password"
                v-model="password"
                :append-icon="show1 ? 'visibility' : 'visibility_off'"
                :rules="[rules.required]"
                :type="show1 ? 'text' : 'password'"
                single-line
                solo
                required
                @click:append="show1 = !show1"
              ></v-text-field>
            </v-flex>

            <v-flex lg12>
              {{ errors }}
            </v-flex>
            <v-flex lg12>
              <v-btn
                :disabled="invalid_form"
                color="#880E4F"
                class="white--text"
                block
                large
                @click="loginUser()"
                >Login</v-btn
              >
            </v-flex>
            <v-flex>
             <router-link to="/register/">Don't have an account? Sign up!</router-link>
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
import { login } from "../services/AuthService";
import { isAuthenticated } from "../services/AuthService";
import { router } from "../routers/MainRouter";

export default {
  name: "LoginPage",
  data: () => ({
    show1: false,
    password: "",
    errors: "",
    invalid_form: false,
    email: "",
    rules: {
      required: value => !!value || "Required.",
      emailMatch: () => "The email and password you entered don't match"
    }
  }),

  methods: {
    loginUser() {
      let emailInput = this.$data.email;
      let passwordInput = this.$data.password;
      login(emailInput, passwordInput)
        .then(data => {
          router.push(this.$route.query.returnUrl || "/");
        })
        .catch(e => {
          this.$data.errors = e["response"]["data"]["Status"];
        });
    }
  }
};
</script>
