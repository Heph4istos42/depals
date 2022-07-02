<template>
    <ul>
    <li class="list" v-for="item in items">
    <img :src="item.src" :alt="item.alt" width="100" height="100" />
    <button class="listitem">
    {{ item.text }}
    </button>
    
    </li>
    </ul>

</template>

<script>
  export default {
      data() {
        return {
            items: [
            {text:'Lebensmittel1', src:'https://image.freepik.com/free-photo/image-human-brain_99433-298.jpg', alt:'L1'},
            {text:'Lebensmittel2', src: '../assets/logo.svg', alt:'L2'},
            {text:'Lebensmittel3'}, 
            {text:'Lebensmittel4'}, 
            {text:'Lebensmittel5'}]
        }
      },
      
  }
</script>
<style>
    .listitem{
        width: 80%;
        height: 100px;
        margin-left: 10px;
        margin-top: 5px;
    }
</style>
