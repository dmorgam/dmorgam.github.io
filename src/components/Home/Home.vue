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
                {{ $t('who.text1') }} <b><a href="https://laravel.com/">Laravel</a></b>, php,
                <b><a href="https://vuejs.org/">Vue.js</a></b> {{ $t('who.text2') }}
                {{ $t('who.text3')}}
              </p>
              <p>
                {{ $t('who.text4')}}
              </p>
                <p>{{ $t('who.text5') }} <router-link to="projects">{{ $t('who.text6') }}</router-link>.</p>
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

   </div>
</template>

<script lang="ts">
import { onMounted } from 'vue'

export default {
  setup () {
    onMounted(() => {

    })
  }
}
</script>
