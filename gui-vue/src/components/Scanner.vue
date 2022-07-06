<script setup>
  import HeaderElem from './parts/Header.vue'
  import Menu from './parts/Menu.vue'
  import { StreamBarcodeReader } from "vue-barcode-reader";
  import router from '../router'
</script>

<template>
  <div class="bg"></div>
  <HeaderElem title="Scanner"/>
  <div class="scannerWrapper">
    <StreamBarcodeReader class="scanner-comp"
      @decode="onDecode"
      @loaded="onLoaded"
      />
  </div>
  <Menu activate="barcodeActive"/>
</template>

<script>
export default {
  data () {
    return {
      detecteds: []
    }
  },
  methods: {
    onDecode(text) {
      let string = text.toString();
      if (string == "4056489126669") { //only apfelsaft
        router.push({ name: 'food', params: { barcodeID: string } });
      }
    },
    onLoaded() {
    },
  }
}
</script>

<style>
.bg {
  background-color: #2a2a2a;
  width: 100%;
  height: 100%;
  position: absolute;
}
.scannerWrapper {
  padding-top: 120px;
}
.scannerWrapper > .scanner-comp > div > video {
    width: 100%;
    height: 100%;
    border-radius: 16px;
}
</style>