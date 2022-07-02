<script setup>
    import IconRedDot from './icons/RedDot.vue'
    import IconGreenDot from './icons/GreenDot.vue'
</script>
<template>
    <div class="plan">
    <ul style="list-style-type: none; padding: unset">
    <li v-if="!activated"> <IconRedDot /> <button class="btnActivate" @click="activated = true"> Activate Plan </button></li>
    <li v-else> <IconGreenDot /> <button class="btnActivate" disabled> Active Plan </button></li>
    <li> <button class="btnRate" @click="activated = false">Reset</button></li>
    <li><button class="btnRate"> Rate Your Plan </button></li>
    </ul>
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