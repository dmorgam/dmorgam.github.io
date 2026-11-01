<template>
  <div>
   <div class="d-flex home-back min-vh-100" id="wrapper">
     <div class="container">
        <br><br><br><br>
        <h1 class="mb-5">
          <span class="badge bg-pill bg-secondary">{{ $t('tokengen.title') }}</span>
        </h1>
        <div class="row alert alert-secondary p-4">
          <div class="col-sm-6">
            <div class="input-group mb-3">
              <span class="input-group-text">{{ $t('tokengen.type') }}</span>
              <select v-model="tipo" class="form-select">
                <option value="password">{{ $t('tokengen.typeMenu.password') }}</option>
                <option value="hex">{{ $t('tokengen.typeMenu.hex') }}</option>
                <option value="base64">{{ $t('tokengen.typeMenu.base64') }}</option>
                <option value="uuid">{{ $t('tokengen.typeMenu.uuid') }}</option>
              </select>
            </div>
            <hr>

            <FillOptionsForm :tipo="tipo" v-on:generateToken="getToken($event)" />

          </div>
          <div class="col-sm-6">
            <div class="card">
              <div class="card-body text-center">
                <h5 class="card-title">{{ $t('tokengen.resultTitle') }}</h5>
                <hr>
                <div class="token-output d-flex align-items-center justify-content-center">
                  <code v-if="token !== ''" class="token-value">{{ token }}</code>
                  <div v-else class="token-placeholder">···</div>
                </div>
                <button v-if="token !== ''" v-on:click="copyToken()" class="btn btn-info mt-3">
                  {{ copied ? $t('tokengen.copied') : $t('tokengen.copy') }}
                </button>
              </div>
            </div>
          </div>
        </div>
     </div>
   </div>
   <div class="bg-dark d-flex">
    <AppFooter />
   </div>
  </div>
</template>

<script lang="ts">
import { ref } from 'vue'
import FillOptionsForm from './components/Token/OptionsForm.vue'
import AppFooter from './components/Footer/AppFooter.vue'

export default {
  components: {
    FillOptionsForm,
    AppFooter
  },

  setup () {
    const tipo = ref('password')
    const token = ref('')
    const copied = ref(false)

    function getToken (text:String) {
      token.value = text as string
      copied.value = false
    }

    function copyToken () {
      navigator.clipboard.writeText(token.value)
        .then(() => {
          copied.value = true
          setTimeout(() => {
            copied.value = false
          }, 2000)
        })
        .catch(err => {
          console.error(err)
        })
    }

    return {
      tipo,
      getToken,
      token,
      copied,
      copyToken
    }
  }
}
</script>
