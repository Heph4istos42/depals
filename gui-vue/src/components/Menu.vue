<template >
<div>
    <button v-if="!barcodeActive" class="iconElem" @click="barcodeActive = true; addActive = false; listActive = false; settingsActive = false"><font-awesome-icon class="icon" icon="fa-solid fa-barcode" /></button>
    <button v-else class="iconElemActive"><font-awesome-icon class="icon" icon="fa-solid fa-barcode" /></button>
    <button v-if="!addActive" class="iconElem" @click="barcodeActive = false; addActive = true; listActive = false; settingsActive = false"><font-awesome-icon class="icon" icon="fa-solid fa-circle-plus" /></button>
    <button v-else class="iconElemActive"><font-awesome-icon class="icon" icon="fa-solid fa-circle-plus" /></button>
    <button v-if="!listActive" class="iconElem" @click="barcodeActive = false; addActive = false; listActive = true; settingsActive = false"><font-awesome-icon class="icon" icon="fa-solid fa-list" /></button>
    <button v-else class="iconElemActive"><font-awesome-icon class="icon" icon="fa-solid fa-list" /></button>
    <button v-if="!settingsActive" class="iconElem" @click="barcodeActive = false; addActive = false; listActive = false; settingsActive = true"><font-awesome-icon class="icon" icon="fa-solid fa-gears" /></button>
    <button v-else class="iconElemActive"><font-awesome-icon class="icon" icon="fa-solid fa-gears" /></button>
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
    border: 0px solid ;
 }

  .iconElemActive {
    background-color: #b6b6b6;
    text-align: center;
    width: 25%;
    padding: 20px;
    border-radius: 0%;
    border: 1px solid ;
 }



 .iconElem:hover{
    background-color:#b6b6b6;

 }

 .icon {
   width: 25px;
   height: 25px;
 }

 </style>