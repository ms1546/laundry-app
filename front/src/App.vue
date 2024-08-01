<template>
  <v-app>
    <v-main>
      <v-container>
        <LaundryControl />
      </v-container>
    </v-main>
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
