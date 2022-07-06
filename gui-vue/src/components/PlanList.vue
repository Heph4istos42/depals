<script setup>
    import HeaderElem from './parts/Header.vue'
    import Liste from './parts/PlanElements.vue'
    import Menu from './parts/Menu.vue'
    import { getplansbyuser } from '../httprequest'
</script>

<template>
  <HeaderElem title="Your plans"/>
  <Liste :list=list /> 
  <Menu activate="listActive"/>
</template>

<script>
  export default {
    data() {
      return {
        list: []
      } 
    },
    mounted() {
      getplansbyuser("SimonUgar").then(response => { 
        console.debug(response);
        response.planlist[0]["activePlan"] = true;
        this.list = response.planlist;
      });
    },
  }
</script>

<style scoped>
</style>