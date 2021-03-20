<template>

    <!-- Sidebar -->
    <div class="bg-light border-right" id="sidebar-wrapper" :style="{ 'margin-left': toggle + 'rem' }" >
      <div class="sidebar-heading">{{ props.title }}</div>
      <div class="list-group list-group-flush">
        <a v-for="i in sections" :key="i.title" :href="i.link" class="list-group-item list-group-item-action bg-light" @click="toggleBar()">
          {{ i.title }}
        </a>
      </div>
      <button type="button" class="btn btn-info menu-toggle" @click="toggleBar()" >
          <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-list" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
              <path fill-rule="evenodd" d="M2.5 11.5A.5.5 0 0 1 3 11h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5zm0-4A.5.5 0 0 1 3 7h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5zm0-4A.5.5 0 0 1 3 3h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5z"/>
          </svg>
      </button>

      <currencyApplet />
    </div>
    <!-- /#sidebar-wrapper -->

</template>

<script lang="ts">
import currencyApplet from './Applets/CurrencyComponent.vue'
import { ref, onMounted } from 'vue'

export default {
  components: {
    currencyApplet
  },
  props: {
    title: String,
    sections: { required: true }
  },

  setup (props: any) {
    const toggle = ref(0)

    function toggleBar () {
      if (window.innerWidth < 768) {
        toggle.value = toggle.value === 0 ? -15 : 0
      }
    }

    onMounted(() => {
      toggleBar()
    })

    return {
      props,
      toggle,
      toggleBar
    }
  }
}
</script>
