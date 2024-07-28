<template>
  <div id="app">
    <header>
      <h1>洗濯物アプリ</h1>
    </header>
    <main>
      <LaundryControl />
    </main>
  </div>
</template>

<script>
import LaundryControl from './components/LaundryControl.vue';

export default {
  components: {
    LaundryControl,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

header {
  background-color: #42b983;
  padding: 20px;
  color: white;
}

main {
  padding: 20px;
}
</style>
