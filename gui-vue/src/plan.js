/* Set up using Vue 3 */
import { createApp } from 'vue'
import Plan from './components/Plan.vue'

/* import the fontawesome core */
import { library } from '@fortawesome/fontawesome-svg-core'

/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

/* import specific icons */
import { faUserSecret } from '@fortawesome/free-solid-svg-icons'
import { faAppleWhole } from '@fortawesome/free-solid-svg-icons'
import { faCirclePlus } from '@fortawesome/free-solid-svg-icons'
import { faGears } from '@fortawesome/free-solid-svg-icons'
import { faList } from '@fortawesome/free-solid-svg-icons'
import { faBarcode } from '@fortawesome/free-solid-svg-icons'


/* add icons to the library */
library.add(faUserSecret)
library.add(faAppleWhole)
library.add(faCirclePlus)
library.add(faGears)
library.add(faList)
library.add(faBarcode)

createApp(Plan)
.component('font-awesome-icon', FontAwesomeIcon)
.mount('#app')
