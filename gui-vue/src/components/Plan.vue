<script setup>
import HeaderElem from './Header.vue'
import Listen from './Liste.vue'
import PlanManager from './PlanManager.vue'
import Trenner from './Trenner.vue'
import MenuElem from './Menu.vue'
</script>

<template>
  <HeaderElem />
  <PlanManager />
  <Trenner /> 
  <Listen /> 
  <MenuElem />
</template>

<script>
  export default {
    data() {
      return {
      } 
    }
  }
  
</script>

<style>
.list {
  display: flex;
  align-items: center;
  justify-content: center;
}

#app {
  max-width: 1280px;
  margin: 0 auto;
  font-weight: normal;
}
</style>