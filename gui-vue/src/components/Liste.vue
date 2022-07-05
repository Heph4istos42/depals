<template>
    <div id="listWrapper">
        <div class="list" v-for="item in lebensmittel">
            <img :src="item.img" :alt="item.bezeichnung" width="100" height="100" />
            <button class="listitem">
                {{ item.bezeichnung }}
            </button>
        </div>
    </div>

</template>

<script>

import { getAllLebensmittel } from '../httprequest'

    export default {
      data() {
        return {
            lebensmittel: []
        }
      },
      mounted() {
        getAllLebensmittel().then(response => { 
          console.debug(response);
          this.lebensmittel = response['lebensmittel'];
          
          console.debug(this.lebensmittel[0]['bezeichnung']);
        });
      }
    }
</script>
<style>
    .listitem{
        width: 80%;
        height: 100px;
        margin-left: 10px;
        margin-top: 5px;
        border: none;
        border-radius: 16px;
        background: gray;
        font-size: 32px;
        /* font-weight: 600; */
        color: white;
    }
    #listWrapper {
      margin-bottom: 75px;
    }
</style>
