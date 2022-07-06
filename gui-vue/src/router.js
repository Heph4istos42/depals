// import routing
import {createRouter, createWebHistory}  from 'vue-router'
import Login from './components/Login.vue'
import Plan from './components/Plan.vue'
import Scanner from './components/Scanner.vue'
import Food from './components/Food.vue'
import FoodList from './components/FoodList.vue'
import PlanRating from './components/PlanRating.vue'
import PlanList from './components/PlanList.vue'
import Search from './components/Search.vue'
import Alternatives from './components/Alternatives.vue'

//navigartion
const routes = [
  { path: '/', component: Login },
  { path: '/scanner', component: Scanner },
  { path: '/search', component: Search },
  { path: '/planlist', component: PlanList },
  //TODO: data übergeben
  { name: 'plan', path: '/plan', component: Plan, props: { plan: {} }},
  { name: 'food', path: '/food', component: Food, props: { food: {} }},
  { path: '/foodplan', component: FoodList },
  { path: '/planrating', component: PlanRating },
  { name: 'alternatives', path: '/alternatives', component: Alternatives, props: { food: {} }},
  //TODO: seiten erstellen
  { path: '/register', component: Login },
  { path: '/settings', component: Login },
]

const router = createRouter({
  // 4. Provide the history implementation to use. We are using the hash history for simplicity here.
  history: createWebHistory(),
  routes, // short for `routes: routes`
})

export default router;