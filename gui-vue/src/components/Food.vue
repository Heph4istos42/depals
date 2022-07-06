<script setup>
    import HeaderElem from './parts/Header.vue'
    import Menu from './parts/Menu.vue'
    import { getAllLebensmittel, getlebensmittelbyinput } from '../httprequest'
    import router from '../router';
</script>

<template>
    <HeaderElem title="Food" />
    <div class="plan">
        <img :src="food.img" width="300" height="300">
        <div class="foodinfowrapper">
            <div class="food-bez-ampel">
                <div class="half">
                {{ food.bezeichnung }}
                </div>
                <div class="kreis-wrapper half">
                    <div class="kreis green"  :class="{ active: green }" ></div>
                    <div class="kreis yellow" :class="{ active: yellow }"></div>
                    <div class="kreis red" :class="{ active: red }"></div>
                </div>
            </div>
            <div class="food-info">
                <div class="half">kcal:</div>
                <div class="half"> {{ food.kcal }}kcal</div>
            </div>
            <div class="food-info">
                <div class="half">contains:</div>
                <div class="half"> {{ food.contains}} </div>
            </div>
            <div class="food-info">
                <div class="half">protein:</div>
                <div class="half"> {{ food.protein }}g </div>
            </div>
            <div class="food-info">
                <div class="half">carbohydrates:</div>
                <div class="half"> {{ food.carbohydrates }}g </div>
            </div>
            <div class="food-info">
                <div class="half">fat:</div>
                <div class="half"> {{ food.fat }}g </div>
            </div>
            <div class="food-info">
                <button class="btn half"> + add to plan</button>
                <button class="btn half" @click="toAlternatives"> supplement and alternative food </button>
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
            food: {
                barcodeID: "",
                bezeichnung: "bezeichnung",
                carbohydrates: 42,
                contains: 42,
                fat: 42,
                img: "http://localhost/img/depals/mt.jpg",
                kcal: 42,
                protein: 21,
            },
            ampel: 0 
        }
    },
    methods: {
        toAlternatives(event) {
            console.debug("click")
            router.push( { name: "alternatives", params: { img: this.food.img } });
        }
    },
    mounted() {
        console.debug(this.$route.params);
        getlebensmittelbyinput(this.$route.params.barcodeID, "SimonUgar").then(response => { 
            console.debug(response);
            this.ampel = response['ampelindikator'];
            this.food = response['lebensmittel'];
            console.debug(this.food);
            
            switch (this.ampel) {
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

                case 0: 
                this.green= false;
                this.yellow = false;
                this.red = true;
                break;

                default:
                this.green= false;
                this.yellow = false;
                this.red = false;
            }
        });
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