<template>
<div :id="props.name" class="carousel slide" data-ride="carousel">
  <ol class="carousel-indicators">
    <li v-for="item in props.slides" :key="item.id" data-target="#carouselExampleIndicators" :data-slide-to="item.id" :class="{active: item.id == 0}"></li>
  </ol>
  <div class="carousel-inner">
    <div v-for="item in props.slides" :key="item.id" class="carousel-item" :class="{active: item.id == 0}">
      <img class="d-block w-100 rounded" :src="item.src">
    </div>
  </div>
  <a class="carousel-control-prev" :href="'#'+props.name" role="button" data-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="sr-only">Previous</span>
  </a>
  <a class="carousel-control-next" :href="'#'+props.name" role="button" data-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="sr-only">Next</span>
  </a>
</div>
</template>


<script lang="ts">
import {  } from 'vue'


export default {
   props: {
     slides: Array,
     name: String
   },

   setup(props: any){
      
     return{
      props
     }

   }
}

</script>
