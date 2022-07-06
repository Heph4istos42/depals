<script setup>
    import ListenElem from './parts/Liste.vue'
</script>
<template>
    <div class="center">
        <img :src="item.src" width="300" height="300">
    </div>
    <div class="trenner"></div>
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

<style scoped>
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
</style>

