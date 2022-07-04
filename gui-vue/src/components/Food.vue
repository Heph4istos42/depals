<script setup>
    import IconRedDot from './icons/RedDot.vue'
    import IconGreenDot from './icons/GreenDot.vue'
</script>
<template>
    <div class="plan">
    <ul style="list-style-type: none; padding: unset">
        <img src='src:https://image.freepik.com/free-photo/image-human-brain_99433-298.jpg' width="300" height="300">
        <table border="0"> 
        <tr>
            <th>Lebensmittel.bezeichnung</th>
            <th>
            <div id="kreis-green"></div>
            <div id="kreis-yellow"></div>
            <div id="kreis-red"></div>
                </th>
        </tr>
        <tr>
            <td>kcal:</td>
            <td>Lebensmittel.kcal</td>
        </tr>
        <tr>
            <td>contains:</td>
            <td>Lebensmittel.contains</td>
        </tr>
        <tr>
            <td>protein:</td>
            <td>lebensmittel.protein</td>
        </tr>
        <tr>
            <td>carbohydrates:</td>
            <td>Lebensmittel.carbohydrates</td>
        </tr>
        <tr>
            <td>fat:</td>
            <td>lebensmittel.fat</td>
        </tr>
        <tr>
            <td><button class="btnRate"> + add to plan</button></td>
            <td><button class="btnRate"> supplement and alternative food </button></td>
        </tr>
        </table>
    </ul>
    </div>
</template>

<style>
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