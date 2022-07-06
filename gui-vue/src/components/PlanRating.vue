<script setup>
    import HeaderElem from './parts/Header.vue'
    import Menu from './parts/Menu.vue'
</script>

<template>
  <div class="rating">
    
    <table border="0"> 
        <tr>
            <th>
                <ul class="list">
                    <star-rating @update:rating ="setRating"></star-rating>
                </ul>
            </th>
        </tr>
            <tr>
                <th>How would you f****** rate your f****** plan</th>
            </tr>
            <tr>
                <th> 
                <textarea v-model="message" placeholder="Your comment"></textarea>
            </th>
            </tr>
            <tr>
                <th> 
                <td><button class="btnRate"> SAVE </button></td>
            </th>
            </tr>
        </table>
  </div>
</template>

<script>
export default {
    methods: {
        setRating(rating){
            this.rating= rating;
        }
    },
    data() {
        return{
            rating: 0
        }
    }
}
</script>


<style scoped>
    .btnActivate {
        height: 50px;
        width: 250px;
        margin-left: 3%;
        margin-top: 5px;
    }

    .btnRate {
        height: 50px;
        width: 340px;
        margin-top: 5px;
    }
    .plan {
        width: 100%;
        text-align: center;
        justify-content: center;
        display: flex;
    }
    #kreis-green {
    background-color: #7CFC00;
    width: 35px;
    height: 35px;
    -moz-border-radius: 20px;
    -webkit-border-radius: 20px;
	border-radius: 20px;
    }
    #kreis-yellow {
        background-color: #FFFF00;
        width: 35px;
        height: 35px;
        -moz-border-radius: 20px;
        -webkit-border-radius: 20px;
        border-radius: 20px;
    }
    #kreis-red {
        background-color: #FF0000;
        width: 35px;
        height: 35px;
        -moz-border-radius: 20px;
        -webkit-border-radius: 20px;
        border-radius: 20px;
    }
    textarea {
    resize: none;
    min-width: 267px;
    max-width: 267px;
    min-height:150px;
    max-height:150px;
    }
</style>