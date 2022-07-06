<template>
    <div class="plan">
    <ul style="list-style-type: none; padding: unset">
        <img :src="item.src" width="300" height="300">
        <table border="0"> 
        <tr>
            <th> {{ item.name }}</th>
            <th>
                <div id="kreis-green"></div>
                <div id="kreis-yellow"></div>
                <div id="kreis-red"></div>
            </th>
        </tr>
        <tr>
            <td>kcal:</td>
            <td> {{ item.kcal }}</td>
        </tr>
        <tr>
            <td>contains:</td>
            <td> {{ item.contains}} </td>
        </tr>
        <tr>
            <td>protein:</td>
            <td> {{ item.protein }} </td>
        </tr>
        <tr>
            <td>carbohydrates:</td>
            <td> {{ item.carbohydrates }} </td>
        </tr>
        <tr>
            <td>fat:</td>
            <td> {{ item.fat }} </td>
        </tr>
        <tr>
            <td><button class="btnRate"> + add to plan</button></td>
            <td><button class="btnRate"> supplement and alternative food </button></td>
        </tr>
        </table>
    </ul>
    </div>
</template>


<script>
export default {
    data(){
        return {
            item: {
                name: 'Milch',
                kcal: '42 kcal',
                contains: '/',
                protein: '3,4g',
                carbohydrates: '5g',
                fat: '1g',
                src: 'https://image.freepik.com/free-photo/image-human-brain_99433-298.jpg'
            }
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
</style>