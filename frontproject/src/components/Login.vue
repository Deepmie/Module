<template>
    <div>
        <el-container>
            <el-card style="margin:0px auto 0px;">
                <h2>用户名</h2>
                <el-input style="width:200px;" v-model="userInfo.username"/>
                <h2>密码</h2>
                <el-input style="width:200px;" type="password" v-model="userInfo.password"/>
                <div style="margin-top:20px;">
                    <el-button @click.event="Login">Login</el-button>
                </div>
            </el-card>
        </el-container>
    </div>
</template>
<script>
export default {
    name:"Login",
    data(){
        return {
            userInfo:{username:"",password:""},
        }
    },
    methods:{
        Login(){
            console.log('您正在准备登陆...');
            this.$ajax
            .post('getoken/',this.userInfo)
            .then(res=>{
                console.log(res.data)
                this.$ajax.defaults.headers.common['Authorization']='Token ' + res.data.token
                sessionStorage.setItem('token',res.data.token)
                this.$store.state.isLogined=true;
                // console.log(this.$ajax)
            })
            .catch(err=>{console.log(err)});
        },
    }
}
</script>
<style lang="css">
    
</style>