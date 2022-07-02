<template>

 <div class="head"> <font-awesome-icon icon="fa-solid fa-apple-whole" /> {{ title }}</div> 
</template>


<script>
export default {
    data(){

        return {
            title: 'Your Plan'
        }
    }
    
}

</script>

<style>
    .head{
        background-color: #9e9a9a;
        text-align: center;
        padding: 20px;
        margin-right: 10px;
        border-bottom: 1px solid #9e9a9a;
        width: 100%;
    }
</style>