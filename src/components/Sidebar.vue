<template>
  <div class="sidebar">
    <ul class="sidebar-panel-nav">
      <li><router-link to="/">Home</router-link></li>
      <li><router-link to="/research">Recherche</router-link></li>
      <li><router-link to="/playlist">Playlist</router-link></li>
    </ul>
  </div>
</template>

<style scoped>
.sidebar {
  overflow-y:auto ;
  color: rgba(0, 0, 0, 0); /* couleur des puces */
  text-align: center;
  background-color: #0E2633;
  position: fixed;
  left: 10px;
  top: 0;
  height: 90vh;
  z-index: 1;
  padding: 3rem 20px 2rem 20px;
  width: 300px;
}

a.router-link-exact-active {
  background-color: rgba(222, 221, 210, 0.39);
  color: #deddd2; /*ca marche pas*/
}

ul.sidebar-panel-nav > li > a {
  color: #ee0d0d;
  text-decoration: none;
  font-size: 1.5rem;
  display: block;
  padding-bottom: 0.5em;
}
</style>
