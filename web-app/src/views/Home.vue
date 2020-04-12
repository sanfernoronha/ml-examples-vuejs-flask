<template>
  <v-app>
    <v-card class="mx-auto mt-10" width="600px">
      <v-app-bar dark color="primary">
        <v-toolbar-title>Train a model</v-toolbar-title>
      </v-app-bar>
      <v-form ref="form" v-model="valid" :lazy-validation="lazy">
        <v-card-text>
          <v-row>
            <v-col cols="12" sm="6" md="12">
              <v-text-field
                prepend-icon="mdi-rename-box"
                v-model="model_name"
                label="Name your model"
                required
                :rules="nameRules"
              ></v-text-field>
              <v-text-field
                prepend-icon="mdi-rename-box"
                v-model="target"
                label="Enter target variable name"
                required
                :rules="nameRules"
              ></v-text-field>
              <v-text-field
                prepend-icon="mdi-rename-box"
                v-model="test_size"
                label="Enter test size percentage(suggested 30)"
                required
                :rules="percentRules"
              ></v-text-field>
              <v-select
                prepend-icon="mdi-rename-box"
                v-model="select"
                :items="items"
                :rules="nameRules"
                label="Select algorithm"
                required
              ></v-select>
            </v-col>
            <!-- <v-col cols="12" sm="6" md="12">
                      
            </v-col>-->

            <!-- <v-col cols="12" sm="6" md="12">
                      
            </v-col>-->

            <v-col cols="12" sm="6" md="12">
              <v-file-input
                v-model="files"
                color="deep-purple accent-4"
                counter
                accept="CSV/csv"
                label="Dataset (CSV file)"
                placeholder="Enter your dataset"
                prepend-icon="mdi-paperclip"
                outlined
                :show-size="1000"
                :rules="fileRules"
              >
                <template v-slot:selection="{ index, text }">
                  <v-chip v-if="index < 2" color="deep-purple accent-4" dark label small>{{ text }}</v-chip>

                  <span
                    v-else-if="index === 2"
                    class="overline grey--text text--darken-3 mx-2"
                  >+{{ files.length - 2 }} File(s)</span>
                </template>
              </v-file-input>
            </v-col>
          </v-row>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" @click="reset()">Close</v-btn>
          <v-btn color="blue darken-1" :disabled="!valid" @click="add()">Save</v-btn>
        </v-card-actions>
      </v-form>
    </v-card>
  </v-app>
</template>

<script>
// @ is an alias to /src

export default {
  name: "Home",
  components: {},
  data: () => ({
    nameRules: [v => !!v || "Title is required"],
    percentRules: [
      v => /^[1-9][0-9]?$|^100$/.test(v) || "Enter percentage (1-100%)"
    ],
    fileRules: [v => !!v || "File is required"],
    select: null,
    items: [
      "Linear Regression",
      "Lasso Regression",
      "Ridge Regression",
      "Bayesian Ridge Regression"
    ],
    files: null,
    model_name: "",
    target: "",
    test_size: "",
    valid: true,
    lazy: true
  }),
  methods: {
    add() {
      if (this.select == "Linear Regression") {
        console.log("Train linear");
      } else if (this.select == "Lasso Regression") {
        console.log("Train Lasso");
      } else if (this.select == "Ridge Regression") {
        console.log("Train Ridge");
      } else if (this.select == "Bayesian Ridge Regression") {
        console.log("Train Ridge");
      }
    },
    reset() {
      this.$router.go();
    }
  }
};
</script>
