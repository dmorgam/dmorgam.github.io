<template>
   <div class="container-fluid home-back left-sidebar-margin px-0">
      <!-- HERO -->
      <section class="hero d-flex align-items-center justify-content-center text-center">
        <div class="hero-inner container">
          <img src="img/dmorgam.png" class="hero-avatar mb-4" :alt="$t('index.card.title')" />

          <h1 class="hero-title mb-2">{{ $t('index.card.title') }}</h1>

          <p class="hero-role mb-4">
            {{ $t('index.card.subtitle') }}
          </p>

          <p class="hero-bio mx-auto mb-4">
            {{ $t('index.card.text') }}
          </p>

          <div class="hero-cta d-flex flex-wrap justify-content-center gap-2">
            <a href="https://github.com/dmorgam/" target="_blank" class="btn btn-primary btn-lg hero-btn">
              <BIconGithub /> GitHub
            </a>
            <a href="https://www.linkedin.com/in/dmorgam/" target="_blank" class="btn btn-outline-light btn-lg hero-btn">
              <BIconLinkedin /> LinkedIn
            </a>
            <a href="#who" class="btn btn-link btn-lg hero-btn-link">
              {{ $t('who.title') }}
              <BIconArrowDown />
            </a>
          </div>
        </div>
      </section>

      <div class="home-content">
      <section class="section-block section-who" id="who">
        <header class="section-head">
          <h2 class="section-heading">{{ $t('who.title') }}</h2>
        </header>
        <div class="section-body">
          <div class="row">
            <div class="col-md-6">
              <p>{{ $t('who.text1') }}</p>
              <p>{{ $t('who.text2') }}</p>
              <p>{{ $t('who.text3') }}</p>
            </div>
            <div class="col-md-6">
              <p>{{ $t('who.text4') }}</p>
              <p>{{ $t('who.text5') }}</p>
            </div>
          </div>
        </div>
      </section>

      <section class="section-block section-tech" id="tech">
        <header class="section-head">
          <h2 class="section-heading">{{ $t('tech.title') }}</h2>
        </header>
        <div class="section-body">
          <div class="row g-4">
            <div class="col-md-6">
              <h6 class="skill-group-title">{{ $t('tech.text1') }}</h6>
              <div class="skill-row" v-for="item in $tm('tech.text5')" :key="item.name">
                <div class="skill-row-head">
                  <span class="skill-name">{{ item.name }}</span>
                </div>
                <div class="progress">
                  <div class="progress-bar" role="progressbar"
                       :style="{ width: visible ? item.skill + '%' : '0%' }"
                       :aria-valuenow="item.skill" aria-valuemin="0" aria-valuemax="100"></div>
                </div>
              </div>

              <h6 class="skill-group-title mt-4">{{ $t('tech.text2') }}</h6>
              <div class="skill-row" v-for="item in $tm('tech.text6')" :key="item.name">
                <div class="skill-row-head">
                  <span class="skill-name">{{ item.name }}</span>
                </div>
                <div class="progress">
                  <div class="progress-bar" role="progressbar"
                       :style="{ width: visible ? item.skill + '%' : '0%' }"
                       :aria-valuenow="item.skill" aria-valuemin="0" aria-valuemax="100"></div>
                </div>
              </div>
            </div>
            <div class="col-md-6">
              <h6 class="skill-group-title">{{ $t('tech.text3') }}</h6>
              <div class="skill-row" v-for="item in $tm('tech.text7')" :key="item.name">
                <div class="skill-row-head">
                  <span class="skill-name">{{ item.name }}</span>
                </div>
                <div class="progress">
                  <div class="progress-bar" role="progressbar"
                       :style="{ width: visible ? item.skill + '%' : '0%' }"
                       :aria-valuenow="item.skill" aria-valuemin="0" aria-valuemax="100"></div>
                </div>
              </div>

              <h6 class="skill-group-title mt-4">{{ $t('tech.text4') }}</h6>
              <div class="skill-row" v-for="item in $tm('tech.text8')" :key="item.name">
                <div class="skill-row-head">
                  <span class="skill-name">{{ item.name }}</span>
                </div>
                <div class="progress">
                  <div class="progress-bar" role="progressbar"
                       :style="{ width: visible ? item.skill + '%' : '0%' }"
                       :aria-valuenow="item.skill" aria-valuemin="0" aria-valuemax="100"></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
      <div class="row mt-5">
         <div class="col" id="credly">
            <section class="section-block">
              <header class="section-head">
                <h2 class="section-heading">{{ $t('menus.indexSidebar.credly') }}</h2>
              </header>
              <div class="text-center">
                <div class="row flex-nowrap overflow-auto">
                  <!-- Kubernetes Badge -->
                  <div class="col-sm m1">
                    <div data-iframe-width="150" data-iframe-height="270" data-share-badge-id="8dcbf360-1bda-4406-a372-9bff3ba56ca2"
                         data-share-badge-host="https://www.credly.com"></div>
                  </div>
                  <!-- LPIC Badge -->
                  <div class="col-sm m1 d-flex justify-content-center">
                    <div class="card text-center border" style="border-radius: 1px;width: 10em;height: 15em;">
                      <div class="card-body">
                        <a target="_blank" href="https://lpi.org/v/LPI000516556/asr4dtr22v">
                          <img class="mb-4" style="width: 60%;" src="https://www.lpi.org/wp-content/uploads/2023/04/cropped-favicon-192x192.png">
                        </a>
                        <p class="card-title nowrap-text">LPIC-1: Linux Administrator</p>
                        <p class="nowrap-text"><small class="card-text">Issuer: Linux Professional Institute</small></p>
                      </div>
                      <div class="card-footer">
                        <small class="text-muted">Linux Institute</small>
                      </div>
                    </div>
                  </div>
                  <!-- Google Automation Badge -->
                  <div class="col-sm m1">
                    <div data-iframe-width="150" data-iframe-height="270" data-share-badge-id="134972d3-8684-49f8-a79d-be6540590d7b"
                         data-share-badge-host="https://www.credly.com"></div>
                  </div>
                  <!-- Ibm badge -->
                  <div class="col-sm m1">
                    <div data-iframe-width="150" data-iframe-height="270" data-share-badge-id="c7621f80-725b-42b1-a257-8da0dc907c71"
                         data-share-badge-host="https://www.credly.com"></div>
                  </div>
                  <!-- Ibm containers badge -->
                  <div class="col-sm m1">
                    <div data-iframe-width="150" data-iframe-height="270" data-share-badge-id="661db282-2f1a-461a-9615-4921ea060b55"
                         data-share-badge-host="https://www.credly.com"></div>
                  </div>
                  <!-- Ibm agile badge -->
                  <div class="col-sm m1">
                    <div data-iframe-width="150" data-iframe-height="270" data-share-badge-id="ca24e472-31b8-449d-a4b2-7895e01abb37"
                         data-share-badge-host="https://www.credly.com"></div>
                  </div>
                  <!-- Ibm ai 1 badge -->
                  <div class="col-sm m1">
                    <div data-iframe-width="150" data-iframe-height="270" data-share-badge-id="8afe0491-9780-4f25-95b5-bde4ac9ff53f"
                         data-share-badge-host="https://www.credly.com"></div>
                  </div>
                  <!-- Ibm ai 2 badge -->
                  <div class="col-sm m1">
                    <div data-iframe-width="150" data-iframe-height="270" data-share-badge-id="55cfd7d8-8c5a-4e4d-8af3-9e6243ccdb85"
                         data-share-badge-host="https://www.credly.com"></div>
                  </div>
                  <!-- Ibm design think 2 badge -->
                  <div class="col-sm m1">
                    <div data-iframe-width="150" data-iframe-height="270" data-share-badge-id="28bf57be-f973-44c2-a162-5bf7b92f1a5f"
                         data-share-badge-host="https://www.credly.com"></div>
                  </div>
                </div>
              </div>
            </section>
         </div>
      </div>
      </div>
   </div>
</template>

<script lang="ts">
import { onMounted, ref } from 'vue'
import {
  BIconGithub,
  BIconLinkedin,
  BIconArrowDown
} from 'bootstrap-icons-vue'

export default {
  components: {
    BIconGithub,
    BIconLinkedin,
    BIconArrowDown
  },

  setup () {
    const visible = ref(false)

    onMounted(() => {
      const credlyScript = document.createElement('script')
      credlyScript.setAttribute('src', 'https://cdn.credly.com/assets/utilities/embed.js')
      document.head.appendChild(credlyScript)

      const tech = document.getElementById('tech')
      if (!tech) { visible.value = true; return }

      const obs = new IntersectionObserver((entries) => {
        entries.forEach(e => {
          if (e.isIntersecting) {
            visible.value = true
            obs.disconnect()
          }
        })
      }, { threshold: 0.15 })
      obs.observe(tech)
    })

    return { visible }
  }
}
</script>
