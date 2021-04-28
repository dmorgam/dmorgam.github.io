<template>
      <div class="card mb-4">
        <div class="card-body">
          <h3 v-html="data.title"></h3>
          <hr>
          <div class="row">
            <div class="col-sm-6">
               <video v-if="data.video !== undefined" :style="data.video.style" controls>
                  <source :src="data.video.src" :type="data.video.type">
               </video>
               <Carousel v-else :name="data.name + 'Slides'" :slides="data.slides"/>
            </div>
            <div class="col-sm-6">
              <p v-for="(item, index) in data.texts" :key="index">{{ item.text }}</p>
              <p>
                <a target="_blank" :href="data.link.link" >
                  {{ data.link.text }}
                </a>
              </p>
              <p v-if="data.link2 !== undefined">
                <a target="_blank" :href="data.link2.link" >
                  {{ data.link2.text }}
                </a>
              </p>
            </div>
          </div>
        </div>
      </div>
</template>

<script lang="ts">
import { } from 'vue'
import Carousel from '../Carousel.vue'

export default {
  components: {
    Carousel
  },

  props: {
    item: Object
  },

  setup (props: any) {
    return {
      data: props.item
    }
  }
}
</script>
