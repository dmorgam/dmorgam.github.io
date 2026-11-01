<template>
  <div class="w-100 mb-4">
    <div v-if="tipo === 'password'" class="w-100">
      <div class="input-group mb-3">
        <span class="input-group-text">{{ $t('tokengen.password.length') }}</span>
        <input type="number" min="4" max="128" v-model.number="passwordData.length" class="form-control">
      </div>
      <div class="form-check mb-2">
        <input type="checkbox" id="passUpper" v-model="passwordData.upper" class="form-check-input">
        <label for="passUpper" class="form-check-label">{{ $t('tokengen.password.upper') }}</label>
      </div>
      <div class="form-check mb-2">
        <input type="checkbox" id="passLower" v-model="passwordData.lower" class="form-check-input">
        <label for="passLower" class="form-check-label">{{ $t('tokengen.password.lower') }}</label>
      </div>
      <div class="form-check mb-2">
        <input type="checkbox" id="passDigits" v-model="passwordData.digits" class="form-check-input">
        <label for="passDigits" class="form-check-label">{{ $t('tokengen.password.digits') }}</label>
      </div>
      <div class="form-check mb-2">
        <input type="checkbox" id="passSymbols" v-model="passwordData.symbols" class="form-check-input">
        <label for="passSymbols" class="form-check-label">{{ $t('tokengen.password.symbols') }}</label>
      </div>
      <div class="form-check mb-2">
        <input type="checkbox" id="passAmbiguous" v-model="passwordData.ambiguous" class="form-check-input">
        <label for="passAmbiguous" class="form-check-label">{{ $t('tokengen.password.ambiguous') }}</label>
      </div>
      <hr>
      <button type="button" v-on:click="generatePasswordToken()" :disabled="sets.length === 0" class="btn btn-success">
        {{ $t('tokengen.button') }}
      </button>
    </div>

    <div v-if="tipo === 'hex'" class="w-100">
      <div class="input-group mb-3">
        <span class="input-group-text">{{ $t('tokengen.bytes') }}</span>
        <input type="number" min="1" max="256" v-model.number="hexBytes" class="form-control">
      </div>
      <hr>
      <button type="button" v-on:click="generateHexToken()" class="btn btn-success">
        {{ $t('tokengen.button') }}
      </button>
    </div>

    <div v-if="tipo === 'base64'" class="w-100">
      <div class="input-group mb-3">
        <span class="input-group-text">{{ $t('tokengen.bytes') }}</span>
        <input type="number" min="1" max="256" v-model.number="base64Data.bytes" class="form-control">
      </div>
      <div class="form-check mb-2">
        <input type="checkbox" id="base64Url" v-model="base64Data.urlSafe" class="form-check-input">
        <label for="base64Url" class="form-check-label">{{ $t('tokengen.urlSafe') }}</label>
      </div>
      <hr>
      <button type="button" v-on:click="generateBase64Token()" class="btn btn-success">
        {{ $t('tokengen.button') }}
      </button>
    </div>

    <div v-if="tipo === 'uuid'" class="w-100">
      <button type="button" v-on:click="generateUuidToken()" class="btn btn-success">
        {{ $t('tokengen.button') }}
      </button>
    </div>
  </div>
</template>

<script lang="ts">
import { ref, reactive, computed } from 'vue'

export default {

  components: {
  },

  props: {
    tipo: String
  },
  emits: ['generateToken'],

  setup (props: Object, ctx: any) {
    const hexBytes = ref(32)

    const passwordData = reactive({
      length: 20,
      upper: true,
      lower: true,
      digits: true,
      symbols: true,
      ambiguous: false
    })

    const base64Data = reactive({
      bytes: 32,
      urlSafe: false
    })

    const sets = computed(() => {
      const list: string[] = []
      if (passwordData.upper) list.push('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
      if (passwordData.lower) list.push('abcdefghijklmnopqrstuvwxyz')
      if (passwordData.digits) list.push('0123456789')
      if (passwordData.symbols) list.push('!@#$%^&*()-_=+[]{}<>?')
      return passwordData.ambiguous ? list.map(s => s.replace(/[Il1O0]/g, '')) : list
    })

    function clamp (value: number, min: number, max: number) {
      return Math.min(Math.max(Math.floor(value) || min, min), max)
    }

    function randomString (charset: string, length: number) {
      const limit = 256 - (256 % charset.length)
      let result = ''
      while (result.length < length) {
        for (const byte of crypto.getRandomValues(new Uint8Array(length))) {
          if (byte < limit && result.length < length) {
            result += charset[byte % charset.length]
          }
        }
      }
      return result
    }

    function generatePasswordToken () {
      passwordData.length = clamp(passwordData.length, 4, 128)

      let password = ''
      do {
        password = randomString(sets.value.join(''), passwordData.length)
      } while (!sets.value.every(set => [...set].some(c => password.includes(c))))

      ctx.emit('generateToken', password)
    }

    function generateHexToken () {
      hexBytes.value = clamp(hexBytes.value, 1, 256)
      const bytes = crypto.getRandomValues(new Uint8Array(hexBytes.value))

      ctx.emit('generateToken', Array.from(bytes, b => b.toString(16).padStart(2, '0')).join(''))
    }

    function generateBase64Token () {
      base64Data.bytes = clamp(base64Data.bytes, 1, 256)
      const bytes = crypto.getRandomValues(new Uint8Array(base64Data.bytes))
      let token = btoa(String.fromCharCode(...bytes))
      if (base64Data.urlSafe) {
        token = token.replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '')
      }

      ctx.emit('generateToken', token)
    }

    function generateUuidToken () {
      ctx.emit('generateToken', crypto.randomUUID())
    }

    return {
      props,
      hexBytes,
      passwordData,
      base64Data,
      sets,
      generatePasswordToken,
      generateHexToken,
      generateBase64Token,
      generateUuidToken
    }
  }
}
</script>
