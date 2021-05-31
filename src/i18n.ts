import { createI18n } from 'vue-i18n'
import enLang from './locales/EN.json'
import esLang from './locales/ES.json'

const messages = {
  es: esLang,
  en: enLang
}

const i18n = createI18n({
  locale: 'en',
  messages
})

export default i18n
