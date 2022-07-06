<script setup>
  import HeaderElem from './parts/Header.vue'
  import Menu from './parts/Menu.vue'
  import Liste from './parts/Liste.vue'
</script>

<template>
  <HeaderElem title="Search"/>
  <div class="searchWrapper">
    <input v-model="input" placeholder="Suche..." />
    <button class="btn" v-on:click="onSearch">
        <font-awesome-icon icon="fa-solid fa-magnifying-glass" />
    </button>
  </div>      
  <Liste />
  <Menu activate="addActive" />
</template>

<script>
export default {
  data () {
    return {
        input: "",
        liste: ['mobile', 'tablet', 'dada']
    }
  },
  methods: {
    onSearch() {
        console.log(` ${this.input}`);
    },
  }
}
</script>

<style scoped>
  .searchWrapper {
    padding-top: 80px;
    text-align: center;
    justify-content: center;
    flex-wrap: wrap;
    display: flex;
    padding-left: 8px;
    padding-right: 8px;
  }
  input {
    width: 65%;
  }
  .btn {
    margin-left: 8px;
    width: 15%;
  }

</style>