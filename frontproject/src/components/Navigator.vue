<template>
    <div>
        <el-menu default-active="1" class="el-menu-demo" mode="horizontal">
            <el-menu-item index="1"><router-link to="/login" name="login">
                    登陆</router-link></el-menu-item>
            <el-menu-item index="2"><router-link to="/signup" name="signup">
                注册</router-link></el-menu-item>
            <el-menu-item index="3" v-if="$store.state.isLogined"><router-link to="/manage">
                管理</router-link></el-menu-item>
          </el-menu>
    </div>
</template>
<script>
export default {
    name:"Navigator",
}
</script>
<style lang="css">
</style>