<template>
  <div class="sidebar">
    <ul class="sidebar-panel-nav">
      <li><router-link to="/">Accueil</router-link></li>
      <li><router-link to="/research">Recherche</router-link></li>
      <li><router-link to="/playlist">Playlist</router-link></li>
    </ul>
  </div>
</template>

<style scoped>
.sidebar {
  color: rgba(0, 0, 0, 0); /* couleur des puces */
  text-align: center;
  background-color: #0E2633;
  position: absolute;
  top: 0;
  left: 10px;
  bottom: 10px;
  z-index: 1;
  padding: 3rem 20px 2rem 20px;
  width: 250px;
}
ul.sidebar-panel-nav {
   margin-top: 110px;
 }
ul.sidebar-panel-nav > li {
  padding: 10px 0 10px 0;
}

ul.sidebar-panel-nav > li >  a {
  color: #deddd2;
  background-color: rgb(222, 221, 210, 0.33);
  padding: 10px 0 10px 0;
  margin-left: -40px;
  border-radius: 5px;
  text-decoration: none; /*retire l'aspect "souligné"*/
  font-size: 1.8rem;
  display: block;
}

/* Le link actif ne fonctionne plus; à réparer */
a.router-link-exact-active {
  color: rgb(207, 36, 49);
  text-decoration: none; /*retire l'aspect "souligné"*/
  background-color: rgb(207, 36, 49, 0.33);
  text-decoration: none; /*retire l'aspect "souligné"*/
}
</style>
