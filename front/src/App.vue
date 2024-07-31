<template>
  <v-app>
    <v-app-bar app color="primary" dark>
      <v-toolbar-title>洗濯物アプリ</v-toolbar-title>
    </v-app-bar>
    <v-main>
      <v-container>
        <LaundryControl />
      </v-container>
    </v-main>
    <v-footer app color="primary" dark>
      <span class="white--text">&copy; 2024 洗濯物アプリ</span>
    </v-footer>
  </v-app>
</template>

<script>
import LaundryControl from './components/LaundryControl.vue'

export default {
  components: {
    LaundryControl,
  },
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap');

#app {
  font-family: 'Roboto', sans-serif;
}

.v-application {
  font-family: 'Roboto', sans-serif;
}
</style>
