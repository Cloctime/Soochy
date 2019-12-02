<template>
  <div class="home">
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <FilmDuJour></FilmDuJour>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'
import FilmDuJour from '@/components/FilmDuJour.vue'

export default {
  name: 'home',
  components: {
    // HelloWorld
    FilmDuJour
  }
}
</script>
