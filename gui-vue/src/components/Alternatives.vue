<script setup>
    import Trenner from './Trenner.vue'
    import ListenElem from './Liste.vue'
</script>
<template>
<div class="center">
    <img :src="item.src" width="300" height="300">
    </div>
    <Trenner />
    <ListenElem />


</template>

<script>
export default {
    data(){
        return {
            item: {
                src: 'https://image.freepik.com/free-photo/image-human-brain_99433-298.jpg'
            }
        }
    }
    
}

</script>

<style>

ul {
  list-style-type: none;
  padding: unset;
}

.list {
  display: flex;
  align-items: center;
  justify-content: center;
}

.center {
    display: flex;
    align-items: center;
    justify-content: center;
}

#app {
  max-width: 1280px;
  margin: 0 auto;
  padding: 2rem;
  font-weight: normal;
}
</style>

