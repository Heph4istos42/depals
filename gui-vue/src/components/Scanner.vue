<script setup>
  import HeaderElem from './parts/Header.vue'
  import Menu from './parts/Menu.vue'
  import { StreamBarcodeReader } from "vue-barcode-reader";
</script>

<template>
  <HeaderElem title="Scanner"/>
  <StreamBarcodeReader class="scanner-comp"
    @decode="onDecode"
    @loaded="onLoaded"
    />
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
        console.log(` ${text}`);
    },
    onLoaded() {
    },
  }
}
</script>

<style>
.scanner-comp {
    width: 100%;
}
.scanner-comp > div > video {
    width: 100%;
    height: 100%;
}
</style>