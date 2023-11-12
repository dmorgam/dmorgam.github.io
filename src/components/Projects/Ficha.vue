<template>
      <div class="card mb-4">
        <div class="card-body">
          <button type="button" class="btn" v-on:click="toggleData()">
            <h3>
              <span v-html="data.tags"></span> {{ $t(data.title) }}
              <BIconChevronUp v-if="showData" />
              <BIconChevronDown v-if="!showData" />
            </h3>
          </button>
          <hr v-show="showData">
          <div class="row" v-show="showData">
            <div class="col-sm-6">
               <video v-if="data.video !== undefined" :style="data.video.style" controls>
                  <source :src="data.video.src" :type="data.video.type">
               </video>
               <Carousel v-else :name="data.name + 'Slides'" :slides="data.slides"/>
            </div>
            <div class="col-sm-6">
              <p v-for="(item, index) in data.texts" :key="index">{{ $t(item.text) }}</p>
              <p>
                <a target="_blank" :href="data.link.link" >
                  {{ $t(data.link.text) }}
                </a>
              </p>
              <p v-if="data.link2 !== undefined">
                <a target="_blank" :href="data.link2.link" >
                  {{ $t(data.link2.text) }}
                </a>
              </p>
            </div>
          </div>
        </div>
      </div>
</template>

<script lang="ts">
import { ref } from 'vue'
import Carousel from '../Carousel.vue'
import { BIconChevronUp, BIconChevronDown } from 'bootstrap-icons-vue'

export default {
  components: {
    Carousel,
    BIconChevronUp,
    BIconChevronDown
  },

  props: {
    item: Object
  },

  setup (props: any) {
    const showData = ref(true)

    const toggleData = () => {
      showData.value = !showData.value
    }

    return {
      data: props.item,
      showData,
      toggleData
    }
  }
}
</script>
