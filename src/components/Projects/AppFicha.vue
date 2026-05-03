<template>
  <div class="project-card" :class="{ 'is-expanded': showData }">
    <div class="project-thumb" @click="toggleData()">
      <video v-if="data.video !== undefined" muted loop playsinline preload="metadata">
        <source :src="data.video.src" :type="data.video.type">
      </video>
      <img v-else-if="data.slides && data.slides[0]" :src="data.slides[0].src" :alt="$t(data.title)" />
      <div class="project-thumb-overlay">
        <span class="project-thumb-cta">
          <BIconArrowsFullscreen />
          {{ showData ? '' : 'View' }}
        </span>
      </div>
    </div>

    <div class="project-body">
      <div class="project-tags" v-html="data.tags"></div>
      <h4 class="project-title" @click="toggleData()">{{ $t(data.title) }}</h4>

      <p v-if="!showData && data.texts && data.texts[0]" class="project-snippet">
        {{ $t(data.texts[0].text) }}
      </p>

      <div class="project-detail" v-show="showData">
        <div class="project-media mb-3">
          <video v-if="data.video !== undefined" :style="data.video.style" controls>
            <source :src="data.video.src" :type="data.video.type">
          </video>
          <AppCarousel v-else :name="data.name + 'Slides'" :slides="data.slides" />
        </div>
        <p v-for="(item, index) in data.texts" :key="index">{{ $t(item.text) }}</p>
        <p v-if="data.link && data.link.link">
          <a target="_blank" :href="data.link.link">
            <BIconBoxArrowUpRight /> {{ $t(data.link.text) }}
          </a>
        </p>
        <p v-if="data.link2 !== undefined">
          <a target="_blank" :href="data.link2.link">
            <BIconBoxArrowUpRight /> {{ $t(data.link2.text) }}
          </a>
        </p>
      </div>

      <button type="button" class="btn btn-sm project-toggle mt-2" @click="toggleData()">
        <span v-if="showData">
          <BIconChevronUp /> Less
        </span>
        <span v-else>
          <BIconChevronDown /> More
        </span>
      </button>
    </div>
  </div>
</template>

<script lang="ts">
import { ref } from 'vue'
import AppCarousel from '../AppCarousel.vue'
import {
  BIconChevronUp,
  BIconChevronDown,
  BIconArrowsFullscreen,
  BIconBoxArrowUpRight
} from 'bootstrap-icons-vue'

export default {
  components: {
    AppCarousel,
    BIconChevronUp,
    BIconChevronDown,
    BIconArrowsFullscreen,
    BIconBoxArrowUpRight
  },

  props: {
    item: Object
  },

  setup (props: any) {
    const showData = ref(false)

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
