import Vue from 'vue'
import VueI18n from 'vue-i18n'
import i18n_zh from '~/lang/zh.json'
import i18n_en from '~/lang/en.json'
// import i18n_ja from '~/lang/ja'

Vue.use(VueI18n)

declare module 'vue/types/vue' {
  interface Vue {
    i18n: VueI18n
  }
}

export default ({ app }: { app: any }) => {
  app.i18n = new VueI18n({
    locale: 'zh',
    fallbackLocale: 'en',
    messages: {
      en: i18n_en,
      //   ja: i18n_ja,
      zh: i18n_zh,
    },
  })
}
