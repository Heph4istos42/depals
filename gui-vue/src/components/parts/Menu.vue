<script setup>
  defineProps({
    activate: {
      type: String,
    }
  })
</script>

<template>
  <div id="menuWrapper">
    <router-link :event="['keyup']" to="/scanner" class="menu-icon-wrapper menu-icon-wrapper-left" :class="{ menuIconWrapperActive: barcodeActive }">
      <font-awesome-icon class="menu-icon" icon="fa-solid fa-barcode" />
    </router-link>

    <router-link :event="['keyup']" to="/search" class="menu-icon-wrapper" :class="{ menuIconWrapperActive: addActive}">
        <font-awesome-icon class="menu-icon" icon="fa-solid fa-circle-plus" />
    </router-link>

    <router-link :event="['keyup']" to="/planlist" class="menu-icon-wrapper" :class="{ menuIconWrapperActive: listActive}">
      <font-awesome-icon class="menu-icon" icon="fa-solid fa-list" />
    </router-link>

    <router-link :event="['keyup']" to="/plan" class=" menu-icon-wrapper menu-icon-wrapper-right" :class="{ menuIconWrapperActive: settingsActive}">
        <font-awesome-icon class="menu-icon" icon="fa-solid fa-gears" />
    </router-link>
  </div>
</template>

<script>
  export default {
    data() {
      return {
          barcodeActive: false,
          addActive: false,
          listActive: false,
          settingsActive: false
      }
    } ,
    mounted() {
      console.debug(this.activate);
      switch (this.activate) {
        case "barcodeActive":
          this.barcodeActive= true;
          this.addActive = false;
          this.listActive = false;
          this.settingsActive = false
          break; 

        case "addActive": 
          this.barcodeActive= false;
          this.addActive = true;
          this.listActive = false;
          this.settingsActive = false
          break;

        case "listActive": 
          this.barcodeActive= false;
          this.addActive = false;
          this.listActive = true;
          this.settingsActive = false
          break;

        case "settingsActive": 
          this.barcodeActive= false;
          this.addActive = false;
          this.listActive = false;
          this.settingsActive = true
          break;
      }
      
    }
  }
</script>
 
 <style scoped>
  #menuWrapper {
    display: flex;  
    position: fixed;
    width: 100%;
    bottom: 0;
    color: black;
    box-shadow: rgba(0, 0, 0, 0.24) 0px -3px 8px; 
    border-top-right-radius: 20px;
    border-top-left-radius: 20px;
  }
  .menu-icon-wrapper {
    background-color: grey;
    text-align: center;
    width: 25%;
    padding: 20px;
    border-radius: 0%;
    border: none ;
    color: black;
    border-top: 1px solid #565656;
  }
  .menu-icon-wrapper:hover{
    background-color:#b6b6b6;
  }
  .menuIconWrapperActive {
    background-color: #b6b6b6;
    text-align: center;
    width: 25%;
    padding: 20px;
    border-radius: 0%;
    border: none;
    border-top: 1px solid #565656;
    color: rgb(177, 13, 13);
  }
  .menu-icon {
    width: 25px;
    height: 25px;
  }
 .menu-icon-wrapper-left {
    border-top-left-radius: 20px;
    border-left: 1px solid #565656;
 }
 .menu-icon-wrapper-right {
    border-top-right-radius: 20px;
    border-right: 1px solid #565656;
 }
 </style>