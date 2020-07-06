export default function ({ app }: { app: Vue }) {
  const params = window.location.search
    .replace(/^\?/, '')
    .split('&')
    .map((x) => x.split('='))
  for (const [key, value] of params) {
    if (key === 'lang') {
      console.info(`Language overriden to ${value}`)
      app.i18n.locale = value
      return
    }
  }
}
