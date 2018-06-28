<template>
  <div class="container" style="margin-top:55px;color: #333;">
    <div style="padding: 10px 50px;font-size: 16px">
      <ul class="uk-list uk-list-bullet">
          <li v-for="api in apis"><a :href="getUrl(mid,api.aid)">{{api.aname}}</a></li>
      </ul>
    </div>
  </div>
</template>
<script>
  export default{
    name:'chooseModule',
    data:function () {
      return{
        apis:[],
        frontend:'',
        pid:''
      }
    },
    methods:{
      getUrl:function(mid,aid){
        var timestamp = (new Date()).valueOf()
       var mleng = String(mid).length
        return this.frontend+'project?pid='+this.pid+'&ln='+timestamp.toString().slice(0,9-mleng)+this.mid+mleng+'2'+aid;
      }
    },
    mounted(){
      this.frontend=this.getFrontendUrl()
      this.pid = this.getQueryVariable('pid')
      var x = null
      $.ajax({
        url:this.getBackendUrl()+"mockserverApi/listApisByMid?mid="+this.mid,
        async: false,
        success:function(ret){
          x = ret
        }
      })
      if (x.status == 0) {
          this.apis=x.data
        } else {
          this.$message({"type": "error", "text": x.msg})
        }

    },
    props:['mid'],
    watch:{
      mid:function(newValue){
        this.frontend=this.getFrontendUrl()
      this.pid = this.getQueryVariable('pid')
      var x = null
      $.ajax({
        url:this.getBackendUrl()+"mockserverApi/listApisByMid?mid="+newValue,
        async: false,
        success:function(ret){
          x = ret
        }
      })
      if (x.status == 0) {
          this.apis=x.data
        } else {
          this.$message({"type": "error", "text": x.msg})
        }
      }
    }
  }
</script>
<style scoped>
li{
  text-align: left;
  margin:15px 5px;
}
</style>
