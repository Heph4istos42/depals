<script setup>
    defineProps({
    list: Array
    })
</script>


<template>
    <div id="listWrapper">
        <div class="listElm" v-for="item in list">
            <div class="listTextElm">
                Plan {{item.planID}}
                <div :class="{kreis: item.activePlan }"></div>
            </div>
            <router-link :event="['keyup']" to="/{{item.link}}" class="btn">
              <div v-if="item.activePlan">
                  to active plan
              </div>
              <div v-else>
                  to the plan
              </div>
            </router-link>
        </div>
        <div class="listElm">
          <router-link :event="['keyup']" to="/{{item.link}}" class="btn">
            Add a plan
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
      }
    }
</script>
<style scoped >
    #listWrapper {
      margin-bottom: 64px;
      padding: 12px;
      padding-top: 80px;
    }
    .listElm {
      display: flex;
      align-items: center;
      justify-content: center;
      margin: 8px;;
      text-align: center;
      text-decoration: none;
      font-family: Arial, Helvetica, sans-serif;
      font-size: 32px;
    }   
    .kreis {
        width: 35px;
        height: 35px;
        -moz-border-radius: 20px;
        -webkit-border-radius: 20px;
        border-radius: 20px;
        margin: auto;
        background-color: #7CFC00;
    }
    .green {
        background-color: #7CFC00;
    }
    .btn {
      width: 50%;
    }
    .listTextElm {
      display: flex;
      width: 50%;
    }
</style>
