<template>
  <div id="app">
    <div id="header">
      <img id="logo-soochy" src="./assets/soochy2x.png" alt="logo Soochy">
    </div>
    <Sidebar/>
    <router-view/>
  </div>
</template>

<script>
import Sidebar from '@/components/TheSidebar.vue'

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
  color: #0E2633;
}

#logo-soochy {
  height: 120px;
  width: auto;
}

#header {
  position: absolute;
  height: 130px;
  width: 100%;
  padding: 0 20px;
  background-color: #CF2431;
  text-align: left;
  z-index: 100;
}

.Sidebar {
  z-index: 99;
}

.router-view {
  z-index: 98;
  position: fixed;
}

</style>

<!-- blanc : #DEDDD2 | rgb(222, 221, 210) -->
<!-- bleu  : #0E2633 | rgb(14, 38, 51) -->
<!-- rouge : #CF2431 | rgb(207, 36, 49) -->
