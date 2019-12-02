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
}

#header {
  position: fixed;
  height: 130px;
  padding: 0 20px;
  background-color: #CF2431;
  text-align: left;
}

</style>

<!-- blanc : #DEDDD2 | rgb(222, 221, 210) -->
<!-- bleu  : #0E2633 | rgb(14, 38, 51) -->
<!-- rouge : #CF2431 | rgb(207, 36, 49) -->
