<template>
  <v-container fill-height v-if="errors == null">
    <v-layout justify-center>
      <v-flex xs12 sm10 lg9>
        <v-card>
          <v-card-title>
            <h1 class="new-post">Create a New Post</h1>
          </v-card-title>
          <v-card-text>
            <v-text-field
              label="Post title"
              v-model="title"
              single-line
              solo
              required
            ></v-text-field>

            <v-flex lg12>
              <v-layout align-center justify-space-between>
                <v-flex lg12>
                  <v-menu
                    ref="menu"
                    v-model="menu"
                    :close-on-content-click="false"
                    :nudge-right="40"
                    :return-value.sync="deadline"
                    lazy
                    transition="scale-transition"
                    offset-y
                    full-width
                    min-width="290px"
                    color="#880E4F"
                  >
                    <v-text-field
                      slot="activator"
                      v-model="deadline"
                      label="Deadline"
                      append-icon="event"
                      readonly
                      solo
                    ></v-text-field>
                    <v-date-picker
                      v-model="deadline"
                      color="#880E4F"
                      scrollable
                    >
                      <v-spacer></v-spacer>
                      <v-btn flat color="#880E4F" @click="menu = false"
                        >Cancel</v-btn
                      >
                      <v-btn
                        flat
                        color="#880E4F"
                        @click="$refs.menu.save(deadline)"
                        >OK</v-btn
                      >
                    </v-date-picker>
                  </v-menu>
                </v-flex>

                <v-flex lg12>
                  <v-text-field
                    label="Zip Code"
                    v-model="zipcode"
                    single-line
                    solo
                  ></v-text-field>
                </v-flex>

                <v-flex lg12>
                  <v-overflow-btn
                    :items="contact_options"
                    v-model="preferred_contact"
                    label="Preferred Contact"
                    solo
                    required
                  ></v-overflow-btn>
                </v-flex>

                <v-flex lg12>
                  <v-overflow-btn
                    :items="categories"
                    label="Category"
                    v-model="category"
                    solo
                    required
                  ></v-overflow-btn>
                </v-flex>

                <v-flex lg12>
                  <v-overflow-btn
                    :items="request_options"
                    v-model="request_type"
                    solo
                    required
                  ></v-overflow-btn>
                </v-flex>
              </v-layout>
            </v-flex>

            <v-flex lg12>
              <v-textarea
                solo
                counter="500"
                v-model="details"
                name="input-7-4"
                label="Type your post's details..."
              ></v-textarea>
            </v-flex>

            <v-flex lg12>
              <v-layout align-end justify-end>
                <v-btn color="#880E4F" flat large>Cancel</v-btn>
                <v-btn
                  :disabled="invalid_form"
                  color="#880E4F"
                  class="white--text"
                  @click="createPost()"
                  raised
                  large
                  >Create</v-btn
                >
              </v-layout>
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
import { createPost } from "../services/PostService";

export default {
  name: "PostCreate",
  data: () => ({
    menu: false,
    title: "",
    details: "",
    deadline: "",
    request_type: "Request Type",
    zipcode: "",
    category: "Category",
    preferred_contact: "Contact",
    contact_options: ["Phone", "Email"],
    request_options: ["Offering", "Requesting"],
    categories: [
      "IT",
      "Events",
      "Tutoring",
      "Lifestyle",
      "Art",
      "Household",
      "Labor",
      "Pets",
      "Automotives"
    ]
  }),

  methods: {
    createPost() {
      let data = this.$data;
      var postDetails = {
        title: data.title,
        details: data.details,
        deadline: data.deadline,
        request_type: data.request_type,
        zip_code: data.zipcode,
        category: data.category,
        preferred_contact: data.preferred_contact
      };
      createPost(postDetails).then(data => {
        console.log(data);
      });
    }
  },

  computed: {
    invalid_form() {
      if (this.title.length < 1) return true;

      if (this.details.length < 1) return true;

      if (this.deadline == "") return true;

      if (this.category == "Category") return true;

      if (this.request_type == "Request Type") return true;

      if (this.zipcode == "") return true;

      return false;
    }
  }
};
</script>
