<template >
  <div id="menuWrapper">
    <button v-if="!barcodeActive" class="iconElem icon-left" @click="barcodeActive = true; addActive = false; listActive = false; settingsActive = false"><font-awesome-icon class="icon" icon="fa-solid fa-barcode" /></button>
    <button v-else class="iconElemActive icon-left"><font-awesome-icon class="icon" icon="fa-solid fa-barcode" /></button>
    <button v-if="!addActive" class="iconElem" @click="barcodeActive = false; addActive = true; listActive = false; settingsActive = false"><font-awesome-icon class="icon" icon="fa-solid fa-circle-plus" /></button>
    <button v-else class="iconElemActive"><font-awesome-icon class="icon" icon="fa-solid fa-circle-plus" /></button>
    <button v-if="!listActive" class="iconElem" @click="barcodeActive = false; addActive = false; listActive = true; settingsActive = false"><font-awesome-icon class="icon" icon="fa-solid fa-list" /></button>
    <button v-else class="iconElemActive"><font-awesome-icon class="icon" icon="fa-solid fa-list" /></button>
    <button v-if="!settingsActive" class="iconElem icon-right" @click="barcodeActive = false; addActive = false; listActive = false; settingsActive = true"><font-awesome-icon class="icon" icon="fa-solid fa-gears" /></button>
    <button v-else class="iconElemActive icon-right"><font-awesome-icon class="icon" icon="fa-solid fa-gears" /></button>
  </div>
</template>

<script>
  export default {
    data() {
      return {
          barcodeActive: false,
          addActive: false,
          listActive: true,
          settingsActive: false
      }
    },      
  }
</script>
 
 <style>
 .iconElem {
    background-color: #9e9a9a;
    text-align: center;
    width: 25%;
    padding: 20px;
    border-radius: 0%;
    border: none ;
 }

  .iconElemActive {
    background-color: #b6b6b6;
    text-align: center;
    width: 25%;
    padding: 20px;
    border-radius: 0%;
    border: none;
    border-top: 1px solid ;
    border-right: 1px solid ;
    border-left: 1px solid ;
 }

 .iconElem:hover{
    background-color:#b6b6b6;
 }

 .icon {
   width: 25px;
   height: 25px;
 }

 .icon-left {
    border-top-left-radius: 20px;
 }
 .icon-right {
    border-top-right-radius: 20px;
 }

 #menuWrapper {
    position: fixed;
    width: 100%;
    bottom: 0;
 }

 </style>