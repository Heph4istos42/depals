<script setup>
defineProps({
  title: {
    type: String,
    required: true
  }
})
</script>

<template>
 <div class="head"> <font-awesome-icon icon="fa-solid fa-apple-whole" /> {{ title }}
 </div> 
</template>

<script>
export default {
    data(){
        return {
            title: '',
        }
    },
}

</script>

<style scoped>
    .head{
        position: fixed;
        background-color: grey;
        text-align: center;
        padding: 20px 0;
        border-bottom: 1px solid grey;
        width: 100%;
        border-bottom-right-radius: 20px;
        border-bottom-left-radius: 20px;
        color: black;
        font-size: 32px;
        text-align: center;
        text-decoration: none;
        font-family: Arial, Helvetica, sans-serif;
        box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;
        border-bottom: 1px solid #565656;
    }
</style>