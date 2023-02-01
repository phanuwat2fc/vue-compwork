import index from '../pages/index.vue'
import login from '../pages/login.vue'
import member from '../pages/member.vue'
import workhome from '../pages/workhome.vue'
import calendar  from '../pages/calendar.vue'
import add_member from '../pages/add_member.vue'
import edit_member from '../pages/edit_member.vue'

import { createRouter, createWebHistory } from "vue-router"


const routes = [
    {
        path:'/index',
        name:'Home',
        component: index
    },
    {
        path:'/',
        name:'login',
        component:login
    },
    {
        path:'/member',
        name:'member',
        component:member
    },
    {
        path:'/workhome',
        name:'workhome',
        component:workhome
    },
    {
        path:'/calendar',
        name:'calendar',
        component:calendar
    },
    {
        path:'/add_member',
        name:'add_member',
        component:add_member
    },
    {
        path:'/edit_member',
        name:'edit_member',
        component:edit_member
    },
    

]
const router = createRouter({
    history:createWebHistory(),routes
})

export default router
