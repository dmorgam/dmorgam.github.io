import { createI18n } from 'vue-i18n'
import enLang from './locales/EN.json'
import projectsEN from './locales/projectsEN.json'
import esLang from './locales/ES.json'
import projectsES from './locales/projectsES.json'

esLang.projects = projectsES
enLang.projects = projectsEN

const messages = {
  es: esLang,
  en: enLang
}

const i18n = createI18n({
  locale: 'en',
  messages
})

export default i18n
