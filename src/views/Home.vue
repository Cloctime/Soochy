<template>
  <div class="home">
    <FilmDuJour/>
  </div>
</template>

<script>
// @ is an alias to /src
import FilmDuJour from '@/components/FilmDuJour.vue'

export default {
  name: 'home',
  components: {
    FilmDuJour
  }
}
</script>
