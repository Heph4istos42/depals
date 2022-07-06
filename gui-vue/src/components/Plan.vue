<script setup>
  import HeaderElem from './parts/Header.vue'
  import Liste from './parts/Liste.vue'
  import PlanManager from './parts/PlanManager.vue'
  import Menu from './parts/Menu.vue'
  import { getAllLebensmittel, getlebensmittelbyinput } from '../httprequest'
</script>

<template>
  <HeaderElem title="Plan"/>
  <PlanManager />
  <div class="trenner"></div>
  <Liste :list=liste /> 
  <Menu activate="settingsActive"/>
</template>

<script>
  export default {
    data() {
      return {
        liste: ['mobile', 'tablet', 'dada']
      } 
    },
    mounted() {
      getAllLebensmittel().then(response => { 
        console.debug(response);
        this.liste = response['lebensmittel'];
        console.debug(this.liste[0]['bezeichnung']);
      });
    },
  }
</script>

<style scoped>
</style>