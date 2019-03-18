<template>
  <v-container fill-height v-if="errors == null">
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
                :rules="[rules.required, rules.min]"
                :type="show1 ? 'text' : 'password'"
                single-line
                solo
                required
                @click:append="show1 = !show1"
              ></v-text-field>
            </v-flex>

            <v-flex lg12>
              <v-btn
                :disabled="invalid_form"
                color="#880E4F"
                class="white--text"
                block
                large
                >Login</v-btn
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
export default {
  name: "LoginPage",
  data: () => ({
    show1: false,
    password: "",
    email: "",
    rules: {
      required: value => !!value || "Required.",
      min: v => v.length >= 8 || "Min 8 characters",
      emailMatch: () => "The email and password you entered don't match"
    }
  })
};
</script>
