import { createApp } from 'vue'
import { Quasar } from 'quasar'
import Fullcalendar from '@fullcalendar/vue3'




// Import icon libraries
import '@quasar/extras/material-icons/material-icons.css'

// Import Quasar css
import 'quasar/src/css/index.sass'
import App from './App.vue'
import './assets/style.css'
import router from './router'



const app = createApp(App)
app.use(router)
app.use(Fullcalendar)
app.use(Quasar, {
    plugins: {}, // import Quasar plugins and add here
  })
app.mount('#app')
