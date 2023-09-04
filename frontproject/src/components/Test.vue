<template>
    <div>
        <el-card>
            <el-radio-group v-model="chooseToken">
                <el-radio label="useToken"></el-radio>
                <el-radio label="nouseToken"></el-radio>
            </el-radio-group>
            <el-header style="margin-left:-20px;"><h2>
                这是一个测试前后端交互的接口
            </h2></el-header>
            <el-container>
                <el-aside width="500px">
                    <el-row style="margin-bottom: 20px;">
                        <el-radio-group v-model="radio1" class="ml-4">
                            <el-radio label="get" size="large"></el-radio>
                            <el-radio label="post" size="large"></el-radio>
                        </el-radio-group>
                    </el-row>
                    <el-button icon="el-icon-plus" size="large"
                    @click="oprKV('add');"></el-button>
                    <span v-for="item in get_key_value" :key="item.id" style="margin:0px 5px 0px 5px" >
                        <el-input style="width:50px;vertical-align:middle;" placeholder="key" v-model="item.key" :ref="`input${item.id}`" />
                        <span style="font-size:20px;vertical-align:middle;margin:0px 5px 0px 5px">:</span>
                        <el-input style="width:50px;vertical-align:middle;" placeholder="value" v-model="item.value"/>
                    </span>
                    <el-button icon="el-icon-minus" size="large" @click="oprKV('remove')"></el-button>
                </el-aside>
                <el-main>
                    <el-input type="textarea" style="height:70px;" v-model="inputarea" />
                </el-main>
            </el-container>

            <el-container>
                <el-footer>
                    <el-button type="info" @click="send">send</el-button>
                </el-footer>
            </el-container>
            <el-container>
                <el-header style="margin-left:-20px;"><h2>
                    这是一个测试数据库的接口
                </h2></el-header>
                <el-container>
                    <el-aside width="500px">
                        <div style="margin:20px 0px 10px 0px">
                            <el-radio-group v-model="radio2" class="ml-4">
                                <el-radio label="built-in" size="large"></el-radio>
                                <el-radio label="customized" size="large"></el-radio>
                            </el-radio-group>
                        </div>

                        <el-button type="info" style="margin-top:20px;"  @click="sendUser('get')">send GET</el-button>
                        <el-button type="info" style="margin-top:20px;"  @click="sendUser('post')">send POST</el-button>
                        <el-button type="info" style="margin-top:20px;"  @click="sendUser('put')">send PUT</el-button>
                        <el-button type="info" style="margin-top:20px;"  @click="sendUser('delete')">send DELETE</el-button>
                        
                        <el-row>
                            <el-col><h3>id</h3></el-col>
                            <el-col><el-input style="width:230px;" v-model="pk"/></el-col>
                        </el-row>
                        <el-row>
                            <el-col><h3>password</h3></el-col>
                            <el-col><el-input style="width:230px;" v-model="userInfo.password" type="password"  /></el-col>
                        </el-row>
                        <el-row>
                            <el-col><h3>username</h3></el-col>
                            <el-col><el-input style="width:230px;" v-model="userInfo.username"  /></el-col>
                        </el-row>
                    </el-aside>
    
                    <el-main>
                        <el-table :data="tableData">
                            <el-table-column prop="id" label="id"></el-table-column>
                            <el-table-column prop="password" label="password"></el-table-column>
                            <el-table-column prop="username" label="username"></el-table-column>
                        </el-table>
                    </el-main>

                </el-container>
            </el-container>

        </el-card>
    </div>
</template>
<script>
import {nanoid} from 'nanoid'
export default {
    name:'Test',
    data(){
        return {
            radio1:"get",
            radio2:"built-in",
            get_key_value:[{id:nanoid(),key:"k1",value:"v1"}],
            inputarea:"",
            tableData:[],
            userInfo:{password:"123456",username:"root"},
            pk:1,
            chooseToken:"useToken",
        }
    },
    methods:{
        oprKV(type){
            const len=this.get_key_value.length+1;
            if(type==='add'){
                this.get_key_value.push({id:nanoid(),key:`k${len}`,value:`v${len}`})
            }else{
                this.get_key_value.pop(-1);
            }
            // console.log( this.$refs[`input${this.get_key_value[0].id}`])
            // Object.values(this.$refs)[1].focus()
            this.$nextTick(()=>{
                this.$refs[`input${this.get_key_value[len-1].id}`][0].focus()
            })
        },
        async send(){
            if(this.radio1==='get'){
                let getInfo=""
                this.get_key_value.forEach((value,index,array)=>{
                    getInfo+=`${value.key}=${value.value}&`
                })
                getInfo=getInfo.slice(0,getInfo.length-1)
                console.log(getInfo)
                await this.$ajax
                .get(`/test/son?${getInfo}`)
                .then(res=>{console.log(res.data.data);this.inputarea=res.data.data})
                .catch(err=>{console.log(err)});
            }else{
                let getInfo={}
                this.get_key_value.forEach((value,index,array)=>{
                    getInfo[value.key]=value.value;
                })
                console.log(getInfo);
                await this.$ajax
                .post('/test/son/',getInfo)
                .then(res=>{console.log(res.data.data);this.inputarea=res.data.data})
                .catch(err=>{console.log(err)});
            }

        },
        async sendUser(type){
            if(type==="get"){
                await this.$ajax
                .get(`test/${this.urlName}/`)
                .then(res=>{
                    console.log(res.data.data);
                    this.tableData=res.data.data;
                })
                .catch(err=>{console.log(err)})
            }else if(type==='post'){
                await this.$ajax
                .post(`test/${this.urlName}/`,this.userInfo)
                .then(res=>{
                    console.log(res.data.data)
                })
                .catch(err=>{console.log(err)})
            }else if(type==='put'){
                await this.$ajax
                .put(`test/${this.urlName}/${this.pk}/`,this.userInfo)
                .then(res=>{
                    console.log(res.data.data)
                })
                .catch(err=>{console.log(err)})
            }else if(type==='delete'){
                await this.$ajax
                .delete(`test/${this.urlName}/${this.pk}/`)
                .then(res=>{
                    console.log(`已经删除了${this.pk}`)
                })
                .catch(err=>{console.log(err)})
            }

        },

    },
    computed:{
        urlName(){
          return (this.radio2==='built-in')?"configuser":"customuser";
        },
    },
    watch:{
        chooseToken(){
            this.$ajax.defaults.headers.common['Authorization']=(this.chooseToken==='useToken')?'Token '+sessionStorage.getItem('token'):''
            console.log(this.$ajax.defaults.headers.common['Authorization'])
        }
    }
    
}
</script>
<style lang="css">
    
</style>