<script setup>
    import IconRedDot from '../icons/RedDot.vue'
    import IconGreenDot from '../icons/GreenDot.vue'
</script>
<template>
    <div class="planManager">
        <div v-if="!activated" class="btnWrapper"> <button class="btn" :event="['keyup']" @click="activated = true"> <IconRedDot /> Activate Plan </button></div>
        <div v-else class="btnWrapper">  <button class="btn" :event="['keydkeyupwn']" disabled><IconGreenDot /> Active Plan </button> </div>
        <div class="btnWrapper"><button class="btn" :event="['keyup']" @click="activated = false">Reset</button></div>  
        <div class="btnWrapper"><router-link class="btn" :event="['keyup']" to="/planrating"> Rate Your Plan </router-link> </div>
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

<style scoped>
    .planManager {
        width: 100%;
        text-align: center;
        padding-top: 84px;
    }
    .btnWrapper {
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 8px;
    }
</style>