<script setup>
import HeaderElem from './parts/Header.vue'
</script>

<template>
  <HeaderElem />
  <div>
    <p>Input is: {{ input }}</p>
    <input v-model="input" placeholder="Suche..." />
    <button class="listitem" v-on:click="onSearch">
        Knoppf
    </button>
  </div>      
</template>

<script>
export default {
  data () {
    return {
        input: "",
    }
  },
  methods: {
    onSearch() {
        console.log(` ${this.input}`);
    },
  }
}
</script>

<style>
.scanner-comp {
    width: 100%;
}
.scanner-comp > div > video {
    width: 100%;
    height: 100%;
}
</style>