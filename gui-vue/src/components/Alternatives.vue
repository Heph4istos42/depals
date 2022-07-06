<script setup>
  import HeaderElem from './parts/Header.vue'
  import Liste from './parts/FoodElements.vue'
  import PlanManager from './parts/PlanManager.vue'
  import Menu from './parts/Menu.vue'
  import { getAllLebensmittel, getlebensmittelbyinput } from '../httprequest'
</script>

<template>
  <HeaderElem title="alternative food"/>
  <img :src="food.img" width="300" height="300">
  <div class="trenner"></div>
  <Liste :list=list /> 
  <Menu activate="settingsActive"/>
</template>

<script>
  export default {
    data() {
      return {
        list: [],
        food: {}
      } 
    },
    mounted() {
      console.debug(this.$router.params);
      getAllLebensmittel().then(response => { 
        console.debug(response);
        this.list = response['lebensmittel'];
      });
    },
  }
</script>

<style scoped>
img {
  padding-top: 80px;
    width: 100%;
    height: auto;
    border-radius: 16px;
}
</style>