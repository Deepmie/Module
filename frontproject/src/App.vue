<template>
  <div>
    <Navigator />
    <router-view></router-view>
    <!-- <Test /> -->
  </div>
</template>

<script>
import Navigator from './components/Navigator'
import Test from './components/Test'
import Login from './components/Login'
import Signup from './components/Signup'
export default {
  name: 'App',
  components: {
    Test,Login,Signup,Navigator,
  },
}
</script>

<style>

</style>
