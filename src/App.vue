<template>
  <div id="app">
    <Sidebar></Sidebar>
    <div id="header">
      <img src="./assets/soochy120px.png" alt="logo Soochy">
    </div>
    <router-view/>
  </div>
</template>

<script>
import Sidebar from '@/components/Sidebar.vue'

export default {
  name: 'app',
  components: {
    Sidebar
  }
}
</script>

<style scoped>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  background-color: #deddd2;
  background-clip: padding-box;
}

#header {
  height: 130px;
  background-color: #CF2431;
  padding: 0 20px;
  text-align: left;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
