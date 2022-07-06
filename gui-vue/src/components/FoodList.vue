<script setup>
    import HeaderElem from './parts/Header.vue'
    import Menu from './parts/Menu.vue'
    import ListenElem from './parts/Liste.vue'
</script>

<template>
    <HeaderElem titele="Food Liste" />
    <div class="center">
        <img :src="item.src" width="300" height="300">
    </div>
    <div class="trenner"></div>
    <ListenElem />
    <Menu />
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

