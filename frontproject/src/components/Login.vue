<template>
    <div>
        <el-container>
            <el-card style="margin:0px auto 0px;">
                <h2>用户名</h2>
                <el-input style="width:200px;" v-model="userInfo.username" @blur="check('username')"/>
                <div class="warning">
                    {{err.username}}
                </div>
                <h2>密码</h2>
                <el-input style="width:200px;" type="password" v-model="userInfo.password"/>
                <div class="warning">
                    {{err.password}}
                    {{err.non_field_errors}}
                </div>
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
            err:"",
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
                this.$router.push('manage/')
                // console.log(this.$ajax)
            })
            .catch(err=>{
                console.log(err.response.data);
                const err_data=err.response.data
                const new_err=new Object();
                for(let i=0;i<Object.values(err_data).length;i++){
                    new_err[Object.keys(err_data)[i]]=Object.values(err_data)[i][0];
                }
                console.log(new_err)
                this.err=new_err;
            });
        },
        check(type){
            console.log('您即将过...')

        }
    }
}
</script>
<style lang="css">
    
</style>