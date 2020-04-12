<template>
  <v-app>
    <v-card class="mx-auto mt-10" width="600px">
      <v-app-bar dark color="primary">
        <v-toolbar-title>Test your model</v-toolbar-title>
      </v-app-bar>
      <v-form ref="predictform" v-model="valid" :lazy-validation="lazy">
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
    valid: true,
    lazy: true
  }),
  methods: {
    reset() {
      this.$router.go();
    },
    add() {
      console.log("predict");
    }
  }
};
</script>
