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
                        <p>
                          <small class="text-muted">
                            {{ $t('index.card.text') }}
                          </small>
                        </p>
                      </div>
                    </div>
                    <div class="col-md-4">
                     <img src="img/dmorgam.png" class="card-img-top" alt="">
                    </div>
                  </div>
                </div>
            </div>

         </div>
      <br>
      <div class="row">
         <div class="col" id="who">
            <div class="alert alert-info text-center" role="alert">
              <h1>{{ $t('who.title') }}</h1>
              <br>
              <p>
                {{ $t('who.text1') }}
              </p>
              <p>
                {{ $t('who.text2') }}
              </p>
              <p>
                {{ $t('who.text3')}}
              </p>
              <p>
                {{ $t('who.text4')}}
              </p>
            </div>
         </div>
      </div>
      <br>
      <div class="row">
         <div class="col" id="tech">
            <div class="alert alert-success text-center" role="alert">
              <h1>{{ $t('tech.title') }}</h1>
              <br>
              <p><b>{{ $t('tech.text1') }}</b> {{ $t('tech.text5') }}</p>
              <p><b>{{ $t('tech.text2') }}</b> {{ $t('tech.text6') }}</p>
              <p><b>{{ $t('tech.text3') }}</b> {{ $t('tech.text7') }}</p>
              <p><b>{{ $t('tech.text4') }}</b> {{ $t('tech.text8') }}</p>
            </div>
         </div>
      </div>
      <br>
      <div class="row">
         <div class="col" id="credly">
            <div class="alert alert-light text-center" role="alert">

              <div class="container">
                <div class="row">
                  <!-- Kubernetes Badge -->
                  <div class="col-sm m1">
                    <div data-iframe-width="150" data-iframe-height="270" data-share-badge-id="8dcbf360-1bda-4406-a372-9bff3ba56ca2"
                         data-share-badge-host="https://www.credly.com"></div>
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

   </div>
</template>

<script lang="ts">
import { onMounted } from 'vue'

export default {
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
