<template>
   <div class="container-fluid home-back left-sidebar-margin">
      <br><br><br><br>
      <!-- HEADER -->
      <div class="row">

         <div class="col-md-5">

         </div>

         <div class="col-md-7">
            <div class="card mb-3">
                  <div class="row no-gutters">
                    <div class="col-md-8">
                      <div class="card-body">
                        <h5 class="card-title font-weight-bold">{{ $t('index.card.title') }}</h5>
                        <p class="card-text">
                          {{ $t('index.card.subtitle') }}
                        </p>
                        <hr>
                        <p>
                          <span class="text-muted">
                            {{ $t('index.card.text') }}
                          </span>
                        </p>
                      </div>
                    </div>
                    <div class="col-md-4">
                     <img src="img/dmorgam.png" class="card-img-top borderless-round" alt="">
                    </div>
                  </div>
                </div>
            </div>

         </div>
      <br>
      <div class="row mt-5">
         <div class="col" id="who">
            <div class="alert alert-info" role="alert">
              <h1 class="ms-5">
                <BIconInfoCircle />
                {{ $t('who.title') }}
              </h1>
              <div class="alert bg-white text-dark">
                <br>
                <div class="row">
                  <div class="col-md-6">
                    <p>
                      {{ $t('who.text1') }}
                    </p>
                    <p>
                      {{ $t('who.text2') }}
                    </p>
                    <p>
                      {{ $t('who.text3')}}
                    </p>
                  </div>
                  <div class="col-md-6">
                    <p>
                      {{ $t('who.text4')}}
                    </p>
                    <p>
                      {{ $t('who.text5')}}
                    </p>
                  </div>
                </div>
              </div>
            </div>
         </div>
      </div>
      <br>
      <div class="row mt-5">
         <div class="col" id="tech">
            <div class="alert alert-primary text-dark" role="alert">
              <h1 class="ms-5">
                <BIconServer />
                {{ $t('tech.title') }}
              </h1>
              <div class="alert bg-white">
                <br>
                <div class="row">
                  <div class="col-md-6">
                    <p><b>{{ $t('tech.text1') }}</b> {{ $t('tech.text5') }}</p>
                    <p><b>{{ $t('tech.text2') }}</b> {{ $t('tech.text6') }}</p>
                  </div>
                  <div class="col-md-6">
                    <p><b>{{ $t('tech.text3') }}</b> {{ $t('tech.text7') }}</p>
                    <p><b>{{ $t('tech.text4') }}</b> {{ $t('tech.text8') }}</p>
                  </div>
                </div>
              </div>
            </div>
         </div>
      </div>
      <br>
      <div class="row mt-5">
         <div class="col" id="credly">
            <div class="text-center" role="alert">

              <div class="container alert alert-light p-4">
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

            </div>
         </div>
      </div>
    <br>
    <br>
   </div>
</template>

<script lang="ts">
import { onMounted } from 'vue'
import { BIconServer, BIconInfoCircle } from 'bootstrap-icons-vue'

export default {
  components: {
    BIconServer,
    BIconInfoCircle
  },

  setup () {
    onMounted(() => {
      // Load credly badges script on mounted
      const credlyScript = document.createElement('script')
      credlyScript.setAttribute('src', 'https://cdn.credly.com/assets/utilities/embed.js')
      document.head.appendChild(credlyScript)
    })
  }
}
</script>
