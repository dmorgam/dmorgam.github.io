<template>
   <div class="d-flex home-back min-vh-100" id="wrapper">
     <div class="container">
        <br><br><br><br>
        <h1 class="mb-5">
          <span class="badge badge-pill badge-secondary">Generador de QR</span>
        </h1>
        <div class="row">
          <div class="col-sm-6">
            <div class="input-group mb-3">
              <div class="input-group-prepend">
                <label class="input-group-text">Formato</label>
              </div>
              <select v-model="tipo" class="custom-select">
                <option value="url">Url</option>
                <option value="vcard">Vcard</option>
                <option value="text">Texto</option>
              </select>
            </div>
            <hr>

            <FillDataForm :tipo="tipo" v-on:generateQr="getQr($event)" />

          </div>
          <div class="col-sm-6">
            <div class="card">
              <div class="card-body">
                <h5 class="card-title">Código Generado</h5>
                <hr>
                <img :src="imageData">

                <div class="w-100">
                  <button v-if="imageData !== ''" v-on:click="downloadImg()" class="btn btn-info">
                    Descargar
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
     </div>
   </div>
</template>

<script lang="ts">
import { ref } from 'vue'
import FillDataForm from './components/QR/DataForm.vue'
import QRCode from 'qrcode'

export default {
  components: {
    FillDataForm
  },

  setup () {
    const tipo = ref('url')
    const imageData = ref('')

    function getQr (text:String) {
      imageData.value = ''
      QRCode.toDataURL(text as string)
        .then(url => {
          imageData.value = url
        })
        .catch(err => {
          console.error(err)
        })
    }

    function downloadImg () {
      const link = document.createElement('a')
      link.href = imageData.value
      link.download = 'QrCode.png'
      link.click()
    }

    return {
      tipo,
      getQr,
      imageData,
      downloadImg
    }
  }
}
</script>
