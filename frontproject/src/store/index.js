import Vuex from 'vuex'
import Vue from 'vue'
//使用插件
Vue.use(Vuex)
const actions={
    
}

const mutations={

}

const state={
    isLogined:sessionStorage.getItem('token') || false,
}

const getters={

}

export default new Vuex.Store({
    actions,
    mutations,
    state,
    getters,
})