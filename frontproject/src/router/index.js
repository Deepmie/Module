import VueRouter from 'vue-router'
import Vue from 'vue'
import Home from '../components/Home'
import Login from '../components/Login'
import Signup from '../components/Signup'
import Test from '../components/Test'
import store from '../store'

Vue.use(VueRouter)

const routes = [
  {
    path:"/",
    name:"home",
    component:Home,
    meta:{needLogin:false},
  },
  {
    path:"/login",
    name:"login",
    component:Login,
    meta:{needLogin:false},
  },
  {
    path:"/signup",
    name:"signup",
    component:Signup,
    meta:{needLogin:false},
  },
  {
    path:"/manage",
    name:"manage",
    component:Test,
    meta:{needLogin:true},
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to,from,next)=>{
  // console.log(to)
  if((to.name!=='signup' || to.name!=='login') && (to.meta.needLogin) ){
    console.log('对不起您需要登录...')
    if(store.state.isLogined){
      next()
    }else{
      next('/login')
    }
  }else{
    next()
  }
})

export default router
