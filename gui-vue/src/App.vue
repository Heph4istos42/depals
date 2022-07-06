<template >
  <router-view></router-view>
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
  /* trenner element styling */
  .trenner {
      width: 100%;
      height: 4px;
      background-color: rgb(161, 159, 159);
      border-radius: 5px;
      margin-top: 5px;
      margin-bottom: 5px;
  }

  /* default button styling */
  .btn {
    width: 80%;
    padding: 16px 0;
    border: none;
    border-radius: 16px;
    background: gray;
    font-size: 20px;
    color: white;
    text-align: center;
    text-decoration: none;
    font-family: Arial, Helvetica, sans-serif;
    box-shadow: rgb(0 0 0) 0px 2px 3px;
    margin: auto;
  }
  .btn:active {
    transform: translateY(0.5px);
    opacity: 0.9;
  }

  /* default input style */
  input {
    width: 70%;
    padding: 12px 20px;
    margin: 16px 0;
    box-sizing: none;
    border: none;
    background: lightgrey;
    font-size: 32px;
  }
  
  /* disable scrollbar */
  body {
    scrollbar-width: none;  /* Firefox */
  -ms-overflow-style: none;  /* IE and Edge */
  }
  body::-webkit-scrollbar {
    display: none; /*Chrome, Safari and Opera */
  }

</style>