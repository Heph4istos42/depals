<script setup>
    import HeaderElem from './parts/Header.vue'
</script>

<template>
  <HeaderElem title="DEPALS"/>
  <div class="start">
    <p class="text" >Sign In</p>
    <input v-model="inputName" placeholder="Name" />
    <input v-model="inputName" placeholder="Password" />
    <div class="link">
        <router-link to="/">No Account? <br> Register <font-awesome-icon icon="fa-solid fa-arrow-right" /></router-link>
    </div>
    <div class="routerWrapper">
        <router-link :event="['keyup']" to="/plan" class="btn">Login</router-link>
    </div>
  </div>  
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
    .start {
        padding-top: 130px; 
        text-align: center;
        flex-wrap: wrap;
    }
    #menuWrapper {
    }
    .text {
        font-size: 64px;
        color: black;
        text-align: center;
        text-decoration: none;
        font-family: Arial, Helvetica, sans-serif;
        margin: 0;
    }
    .link {
        font-size: 20px;
        color: grey;
        text-align: center;
        text-decoration: none;
        font-family: Arial, Helvetica, sans-serif;
        margin: 16px 0;
    }
    a {
        font-size: 20px;
        color: grey;
        text-align: center;
        text-decoration: none;
        font-family: Arial, Helvetica, sans-serif;
    }
    .routerWrapper {
        display: flex;
        align-items: center;
        justify-content: center;
    }
</style>