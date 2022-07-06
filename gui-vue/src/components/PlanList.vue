<script setup>
    import HeaderElem from './parts/Header.vue'
    import Listen from './parts/Liste.vue'
    import Menu from './parts/Menu.vue'
</script>

<template>
  <HeaderElem title="Plan"/>
  <Listen /> 
  <Menu activate="settingsActive"/>
</template>

<script>
  export default {
    data() {
      return {
      } 
    }
  }
</script>

<style scoped>
</style>