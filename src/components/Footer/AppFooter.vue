<template>
     <div class="container">
      <footer class="d-flex flex-wrap justify-content-between align-items-center py-3 my-4">
        <div class="col-md-4 d-flex align-items-center">
          <span class="mb-3 mb-md-0 text-secondary">© 2023 - David Moreno Gamez</span>
        </div>

        <ul class="nav col-md-4 justify-content-end list-unstyled d-flex">
          <li class="ms-3">
            <a class="text-secondary p-2" target="_blank" href="https://github.com/dmorgam/">
              <BIconGithub /> GitHub
            </a>
          </li>
          <li class="ms-3">
            <a class="text-secondary p-2" target="_blank" href="https://www.linkedin.com/in/dmorgam/">
              <BIconLinkedin /> LinkedIn
            </a>
          </li>
        </ul>
      </footer>
     </div>
</template>

<script lang="ts">
import { } from 'vue'
import { BIconGithub, BIconLinkedin } from 'bootstrap-icons-vue'

export default {
  components: {
    BIconGithub,
    BIconLinkedin
  },

  setup () {
  }
}
</script>
