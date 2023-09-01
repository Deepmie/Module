<template>
    <div>
        <el-container>
            <el-card style="margin:0px auto 0px;">
                <h2>用户名</h2>
                <el-input style="width:200px;" v-model="userInfo.username"/>
                <h2>密码</h2>
                <el-input style="width:200px;" type="password" v-model="userInfo.password"/>
                <div style="margin-top:20px;">
                    <el-button @click.event="Signup">Signup</el-button>
                </div>
            </el-card>
        </el-container>
    </div>
</template>
<script>
export default {
    name:"Signup",
    data(){
        return {
            userInfo:{username:"",password:""},
        }
    },
    methods:{
        Signup(){
            console.log('您正在准备注册...')
            this.$ajax
            .post('test/configuser/',this.userInfo)
            .then(res=>{console.log(res.data)})
            .catch(err=>{console.log(err)});
        }
    }
}
</script>
<style lang="css">
    
</style>