<script setup>
    import HeaderElem from './parts/Header.vue'
    import Menu from './parts/Menu.vue'
</script>

<template>
    <HeaderElem title="Food" />
    <div class="plan">
        <img :src="item.src" width="300" height="300">
        <div class="foodinfowrapper">
            <div class="food-bez-ampel">
                <div class="half">
                {{ item.name }}
                </div>
                <div class="kreis-wrapper half">
                    <div class="kreis green"  :class="{ active: green }" ></div>
                    <div class="kreis yellow" :class="{ active: yellow }"></div>
                    <div class="kreis red" :class="{ active: red }"></div>
                </div>
            </div>
            <div class="food-info">
                <div class="half">kcal:</div>
                <div class="half"> {{ item.kcal }}</div>
            </div>
            <div class="food-info">
                <div class="half">contains:</div>
                <div class="half"> {{ item.contains}} </div>
            </div>
            <div class="food-info">
                <div class="half">protein:</div>
                <div class="half"> {{ item.protein }} </div>
            </div>
            <div class="food-info">
                <div class="half">carbohydrates:</div>
                <div class="half"> {{ item.carbohydrates }} </div>
            </div>
            <div class="food-info">
                <div class="half">fat:</div>
                <div class="half"> {{ item.fat }} </div>
            </div>
            <div class="food-info">
                <button class="btn half "> + add to plan</button>
                <button class="btn half"> supplement and alternative food </button>
            </div>
        </div>
    </div>
    <Menu />
</template>


<script>
export default {
    data(){
        return {
            green: false,
            yellow: false,
            red: false,
            item: {
                name: 'Milch',
                kcal: '42 kcal',
                contains: '/',
                protein: '3,4g',
                carbohydrates: '5g',
                fat: '1g',
                src: 'https://image.freepik.com/free-photo/image-human-brain_99433-298.jpg',
                ampel: 3
            }
        }
    },
    mounted() {
      switch (this.item.ampel) {
        case 1:
          this.green= true;
          this.yellow = false;
          this.red = false;
          break; 

        case 2:
          this.green= false;
          this.yellow = true;
          this.red = false;
          break;

        case 3: 
          this.green= false;
          this.yellow = false;
          this.red = true;
          break;

        default:
          this.green= false;
          this.yellow = false;
          this.red = false;
      }
    }
    
}

</script>

<style scoped>
    .plan {
        text-align: center;
        justify-content: center;
        padding-top: 80px;
        padding-bottom: 70px;
        font-size: 20px;
        color: black;
        text-align: center;
        text-decoration: none;
        font-family: Arial, Helvetica, sans-serif;
        padding-right: 4px;
        padding-left: 4px;
    }

    img {
        width: 100%;
        height: auto;
        border-radius: 16px;
    }
    .foodinfowrapper{
        background: lightgray; 
        padding-top: 16px;
        border-radius: 16px;
    }

    .kreis-wrapper {
        display: flex;
    }   
    .kreis {
        width: 35px;
        height: 35px;
        -moz-border-radius: 20px;
        -webkit-border-radius: 20px;
        border-radius: 20px;
        margin: auto;
    }
    .green {
        background-color: #7CFC00;
    }
    .yellow {
        background-color: #FFFF00;
    }
    .red {
        background-color: #FF0000;
    }
    .active {
        border: 5px solid #0000FF;
    }

    .food-bez-ampel {
        display: flex;
        justify-content: center;
        font-size: 38px;
        font-weight: 800;
        padding-bottom: 4px;
    }
    .food-info {
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 4px 0;
        text-align: left;
        padding-left: 8px;
    
    }
    .half {
        width: 50%;
    }
    .btn {
        margin-top: 8px;
        margin-left: 8px;
        margin-right: 8px;
    }

</style>