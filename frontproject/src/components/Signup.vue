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
            err:""
        }
    },
    methods:{
        Signup(){
            console.log('您正在准备注册...')
            this.$ajax
            .post('test/configuser/',this.userInfo)
            .then(res=>{console.log(res.data)})
            .catch(err=>{
                console.log(err.response.data);
                const err_data=err.response.data.data
                const new_err=new Object();
                for(let i=0;i<Object.values(err_data).length;i++){
                    new_err[Object.keys(err_data)[i]]=Object.values(err_data)[i][0]
                }
                console.log(new_err)
                this.err=new_err;
            });
        },
        check(type){
            if(type==='username'){
                console.log('校验用户名')
            }
        }
        
    }
}
</script>
<style lang="css">
    
</style>