<template>
  <div class="w-100 mb-4">
    <div v-if="tipo === 'url'" class="w-100">
      <div class="input-group mb-3">
        <div class="input-group-prepend">
          <label class="input-group-text">{{ $t('qrcode.formatMenu.url') }}</label>
        </div>
        <input type="text" class="form-control" v-model="urlFormatted">
      </div>
      <hr>
      <button type="button" v-on:click="generateUrlCode()" class="btn btn-success">
        {{ $t('qrcode.button') }}
      </button>
    </div>

    <div v-if="tipo === 'vcard'" class="w-100">
      <div class="row">
        <div class="input-group mb-3 col-sm-6">
          <div class="input-group-prepend">
            <label class="input-group-text">{{ $t('qrcode.vcard.name') }}</label>
          </div>
          <input type="text" v-model="vCardData.name" class="form-control">
        </div>
        <div class="input-group mb-3 col-sm-6">
          <div class="input-group-prepend">
            <label class="input-group-text">{{ $t('qrcode.vcard.surn') }}</label>
          </div>
          <input type="text" v-model="vCardData.last" class="form-control">
        </div>
      </div>
      <div class="row">
        <div class="input-group mb-3 col-sm-6">
          <div class="input-group-prepend">
            <label class="input-group-text">{{ $t('qrcode.vcard.tlf') }}</label>
          </div>
          <input type="text" v-model="vCardData.tlf" class="form-control">
        </div>
        <div class="input-group mb-3 col-sm-6">
          <div class="input-group-prepend">
            <label class="input-group-text">{{ $t('qrcode.vcard.cell') }}</label>
          </div>
          <input type="text" v-model="vCardData.cell" class="form-control">
        </div>
      </div>
      <div class="row">
        <div class="input-group mb-3 col-sm-12">
          <div class="input-group-prepend">
            <label class="input-group-text">{{ $t('qrcode.vcard.email') }}</label>
          </div>
          <input type="text" v-model="vCardData.email" class="form-control">
        </div>
      </div>
      <div class="row">
        <div class="input-group mb-3 col-sm-12">
          <div class="input-group-prepend">
            <label class="input-group-text">{{ $t('qrcode.vcard.web') }}</label>
          </div>
          <input type="text" v-model="vCardData.web" class="form-control">
        </div>
      </div>
      <div class="row">
        <div class="input-group mb-3 col-sm-6">
          <div class="input-group-prepend">
            <label class="input-group-text">{{ $t('qrcode.vcard.org') }}</label>
          </div>
          <input type="text" v-model="vCardData.org" class="form-control">
        </div>
        <div class="input-group mb-3 col-sm-6">
          <div class="input-group-prepend">
            <label class="input-group-text">{{ $t('qrcode.vcard.title') }}</label>
          </div>
          <input type="text" v-model="vCardData.title" class="form-control">
        </div>
      </div>
      <div class="row">
        <div class="input-group mb-3 col-sm-12">
          <div class="input-group-prepend">
            <label class="input-group-text">{{ $t('qrcode.vcard.st') }}</label>
          </div>
          <input type="text" v-model="vCardData.street" class="form-control">
        </div>
      </div>
      <div class="row">
        <div class="input-group mb-3 col-sm-6">
          <div class="input-group-prepend">
            <label class="input-group-text">{{ $t('qrcode.vcard.city') }}</label>
          </div>
          <input type="text" v-model="vCardData.city" class="form-control">
        </div>
        <div class="input-group mb-3 col-sm-6">
          <div class="input-group-prepend">
            <label class="input-group-text">{{ $t('qrcode.vcard.country') }}</label>
          </div>
          <input type="text" v-model="vCardData.country" class="form-control">
        </div>
      </div>
      <hr>
      <button type="button" v-on:click="generateVcardCode()" class="btn btn-success">
        {{ $t('qrcode.button') }}
      </button>
    </div>

    <div v-if="tipo === 'text'" class="w-100">
      <textarea class="form-control" rows="5" v-model="textFormatted"></textarea>
      <hr>
      <button type="button" v-on:click="generateTextCode()" class="btn btn-success">
        {{ $t('qrcode.button') }}
      </button>
    </div>
  </div>
</template>

<script lang="ts">
import { ref, reactive } from 'vue'

export default {

  components: {
  },

  props: {
    tipo: String
  },
  emits: ['generateQr'],

  setup (props: Object, ctx: any) {
    const urlFormatted = ref('')
    const textFormatted = ref('')

    const vCardData = reactive({
      name: '',
      last: '',
      tlf: '',
      cell: '',
      email: '',
      web: '',
      org: '',
      title: '',
      street: '',
      city: '',
      country: ''
    })

    function generateUrlCode () {
      ctx.emit('generateQr', urlFormatted.value)
    }

    function generateTextCode () {
      ctx.emit('generateQr', textFormatted.value)
    }

    function generateVcardCode () {
      let vcardStr = 'BEGIN:VCARD\nVERSION:3.0'
      vcardStr += '\nN:' + vCardData.last + ';' + vCardData.name
      vcardStr += '\nFN:' + vCardData.name + ' ' + vCardData.last
      vcardStr += '\nORG:' + vCardData.org
      vcardStr += '\nTITLE:' + vCardData.title
      vcardStr += '\nADR:;;' + vCardData.street + ';' + vCardData.city + ';;;' + vCardData.country
      vcardStr += '\nTEL;WORK;VOICE:' + vCardData.tlf
      vcardStr += '\nTEL;CELL:' + vCardData.cell
      vcardStr += '\nTEL;FAX:'
      vcardStr += '\nEMAIL;WORK;INTERNET:' + vCardData.email
      vcardStr += '\nURL:' + vCardData.web
      vcardStr += '\nEND:VCARD'

      ctx.emit('generateQr', vcardStr)
    }

    return {
      props,
      urlFormatted,
      textFormatted,
      vCardData,
      generateUrlCode,
      generateTextCode,
      generateVcardCode
    }
  }
}
</script>
