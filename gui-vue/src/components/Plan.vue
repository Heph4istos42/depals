<script setup>
  import HeaderElem from './parts/Header.vue'
  import Liste from './parts/FoodElements.vue'
  import PlanManager from './parts/PlanManager.vue'
  import Menu from './parts/Menu.vue'
  import { getAllLebensmittel, getlebensmittelbyinput } from '../httprequest'
</script>

<template>
  <HeaderElem title="Plan"/>
  <PlanManager />
  <div class="trenner"></div>
  <Liste :list=list /> 
  <Menu activate="settingsActive"/>
</template>

<script>
  export default {
    data() {
      return {
        list: [],
        plan: {}
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
</style>