<script setup>
    import IconRedDot from './icons/RedDot.vue'
    import IconGreenDot from './icons/GreenDot.vue'
</script>
<template>
    <div class="plan">
        <div v-if="!activated"> <IconRedDot /> <button class="btnActivate" @click="activated = true"> Activate Plan </button></div>
        <div v-else> <IconGreenDot /> <button class="btnActivate" disabled> Active Plan </button> </div>
        <div> <button class="btnRate" @click="activated = false">Reset</button></div>  
        <div><button class="btnRate"> Rate Your Plan </button> </div>
    </div>
</template>

<script>
  export default {
      data() {
        return {
            activated: false
        }
      },
      
  }
</script>

<style>
    .btnActivate {
        height: 50px;
        width: 250px;
        margin-left: 3%;
        margin-top: 5px;
    }

    .btnRate {
        height: 50px;
        width: 340px;
        margin-top: 5px;
    }
    .plan {
        width: 100%;
        text-align: center;
    }
</style>