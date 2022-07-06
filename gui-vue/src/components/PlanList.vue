<script setup>
    import HeaderElem from './parts/Header.vue'
    import Listen from './parts/Liste.vue'
    import Menu from './parts/Menu.vue'
</script>

<template>
  <HeaderElem title="Your plans"/>
  <Listen /> 
  <Menu activate="listActive"/>
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