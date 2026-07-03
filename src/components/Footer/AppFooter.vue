<template>
  <footer class="site-footer">
    <div class="footer-inner">
      <div class="footer-brand">
        <div class="footer-logo">DM</div>
        <div>
          <p class="footer-name">{{ $t('index.card.title') }}</p>
          <p class="footer-role">{{ $t('index.card.subtitle') }}</p>
        </div>
      </div>

      <ul class="footer-social">
        <li>
          <a href="https://github.com/dmorgam/" target="_blank" rel="noopener" aria-label="GitHub">
            <BIconGithub />
          </a>
        </li>
        <li>
          <a href="https://www.linkedin.com/in/dmorgam/" target="_blank" rel="noopener" aria-label="LinkedIn">
            <BIconLinkedin />
          </a>
        </li>
      </ul>
    </div>

    <div class="footer-bottom">
      <span>© {{ year }} {{ $t('index.card.title') }}</span>
      <a class="footer-tag" href="https://github.com/dmorgam/dmorgam.github.io" target="_blank" rel="noopener">
        src: github.com/dmorgam/dmorgam.github.io
      </a>
    </div>
  </footer>
</template>

<script lang="ts">
import { computed } from 'vue'
import { BIconGithub, BIconLinkedin } from 'bootstrap-icons-vue'

export default {
  components: {
    BIconGithub,
    BIconLinkedin
  },
  setup () {
    const year = computed(() => new Date().getFullYear())
    return { year }
  }
}
</script>
