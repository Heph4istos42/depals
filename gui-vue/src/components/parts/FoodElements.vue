<script setup>
  defineProps({
    list: Array
  })
</script>
<template>
    <div id="listWrapper">
        <div class="listElm" v-for="item in list">
            <img :src="item.img" :alt="item.bezeichnung" width="100" height="100" />
            <router-link :event="['keyup']" :to="{ name: 'food', params: item }" class="btn">
                {{ item.bezeichnung }}
            </router-link>
        </div>
    </div>
</template>

<script>
    export default {
      data() {
        return {
            list: []
        }
      },
      methods: {
      },
      mounted() {
        console.debug(this.list);
      }
    }
</script>
<style scoped >
    #listWrapper {
      margin-bottom: 64px;
      padding: 12px;
    }
    .listElm {
      display: flex;
      align-items: center;
      justify-content: center;
    }
    img {
      border-radius: 50%;
      box-shadow: rgb(0 0 0 / 50%) 0px 3px 3px;
      margin: 4px;
    }
</style>
