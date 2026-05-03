<template>
  <div class="currency-applet">
    <div class="currency-head">
      <span class="currency-title">
        <BIconCash />
        {{ $t('currencyApplet.title') }}
      </span>
      <span class="currency-live" :class="{ 'is-on': loaded }" :title="loaded ? 'Live' : 'Loading'"></span>
    </div>

    <div class="currency-row">
      <div class="currency-from">
        <span class="currency-flag">€</span>
        <span class="currency-code">EUR</span>
      </div>
      <div class="currency-to">
        <span class="currency-value">{{ formattedSelected }}</span>
        <select class="currency-select" v-model="currency.selected">
          <option v-for="item in Object.entries(currency.rates)" :key="item[0]" :value="item[1]">
            {{ item[0] }}
          </option>
        </select>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { reactive, ref, computed, onMounted } from 'vue'
import { BIconCash } from 'bootstrap-icons-vue'
import axios from 'axios'

export default {
  components: {
    BIconCash
  },
  setup () {
    const currency = reactive({
      rates: {} as Record<string, number>,
      base: '',
      selected: '0.0' as string | number,
      start: 'CLP'
    })
    const loaded = ref(false)

    const formattedSelected = computed(() => {
      const n = Number(currency.selected)
      if (!isFinite(n) || n === 0) return '—'
      return n.toLocaleString(undefined, { maximumFractionDigits: 2 })
    })

    onMounted(() => {
      fetchCurrency()
    })

    function fetchCurrency () {
      const exchageStr:any = sessionStorage.getItem('exchange')

      if (exchageStr === null) {
        axios.get('https://pcmt93kogj.execute-api.eu-central-1.amazonaws.com/exchange')
          .then((response) => {
            currency.rates = response.data.rates
            currency.base = response.data.base
            currency.selected = response.data.rates[currency.start]
            loaded.value = true
            sessionStorage.setItem('exchange', JSON.stringify(response.data))
          })
      } else {
        const exchange:any = JSON.parse(exchageStr)
        currency.rates = exchange.rates
        currency.base = exchange.base
        currency.selected = exchange.rates[currency.start]
        loaded.value = true
      }
    }

    return {
      currency,
      loaded,
      formattedSelected
    }
  }
}
</script>
