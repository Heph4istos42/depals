<script setup>
import HeaderElem from './components/Header.vue'
import Listen from './components/Liste.vue'
import PlanManager from './components/PlanManager.vue'
import Trenner from './components/Trenner.vue'
import MenuElem from './components/Menu.vue'
</script>

<template>
    <header>
      <HeaderElem />
    </header>
    <div></div>
    <div >
      <ul>
        <li> <PlanManager /></li>
        <li> <Trenner /> </li>
        <li> <Listen /> </li>
      </ul>
      </div>
      <div></div>
      
      <MenuElem />
    
</template>

<script>
  export default {
      data() {
        return {
            items: [
            { text:'Lebensmittel1',src:'logo.svg', alt:'Lebensmittel1'},
            {text:'Lebensmittel2'},
            {text:'Lebensmittel3'}, 
            {text:'Lebensmittel4'}, 
            {text:'Lebensmittel5'}]
        }
      },

  
      
  }
</script>

<style>

ul {
  list-style-type: none;
  padding: unset;
}

.list {
  display: flex;
  align-items: center;
  justify-content: center;
}

#app {
  max-width: 1280px;
  margin: 0 auto;
  padding: 2rem;
  font-weight: normal;
}
</style>