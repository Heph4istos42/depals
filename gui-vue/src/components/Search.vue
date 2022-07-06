<script setup>
  import HeaderElem from './parts/Header.vue'
  import Menu from './parts/Menu.vue'
  import Liste from './parts/FoodElements.vue'
  import { getlebensmittelbyinput } from '../httprequest'
  import router from './../router'
</script>

<template>
  <HeaderElem title="Search"/>
  <div class="searchWrapper">
    <input v-model="input" placeholder="Search..." />
    <button class="btn" v-on:click="onSearch">
        <font-awesome-icon icon="fa-solid fa-magnifying-glass" />
    </button>
  </div>      
  <Liste :list=list />
  <Menu activate="addActive" />
</template>

<script>
  export default {
    data () {
      return {
          input: "",
          list: []
      }
    },
    methods: {
      onSearch() {
        //TODO: UserName Speichern
        getlebensmittelbyinput(this.input, "SimonUgar").then(res => {
          console.debug(res);
          if (res["ampelindikator"]) {
            console.debug("barcode abfrage");
            router.push("/food");
          } else {
            this.list = res;
          }
        });
      },
    }
  }
</script>

<style scoped>
  .searchWrapper {
    padding-top: 80px;
    text-align: center;
    justify-content: center;
    display: flex;
    padding-left: 8px;
    padding-right: 8px;
  }
  input {
    width: 300%;
  }
  .btn {
    margin-left: 8px;
    padding: 16px;
  }

</style>