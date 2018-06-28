<template>
  <div class="home-body">
      <div class="mc home-projects">
        <div class="cb home-p-title">
          <div class="col-sm-4">项目名称</div>
          <div class="col-sm-2">拥有者</div>
          <div class="col-sm-2">创建时间</div>
          <div class="col-sm-4 p-actions">操作</div>
        </div>
        <div class="cb row" v-for="i in projects">
          <div class="col-sm-4">
            <a :href="fronturl+'project?pid='+i.pid">&nbsp;{{i.pname}} </a></div>
          <div class="col-sm-2">&nbsp;{{i.powner}}</div>
          <div class="col-sm-3">&nbsp;{{i.pctime}} </div>
          <div class="col-sm-2" style=""><a><i class="fa fa-edit"></i> 修改</a></div>
        </div>
      </div>
        <div class="new-project">
          <div class="new-project-btn ta-c">
            <newButton></newButton>
          </div>
        </div>
    </div>
</template>
<script>
  import newButton from './newButton.vue'
  export default{
    name:'dashboardBody',
    data:function(){
      return{
        projects:[],
        fronturl:this.getFrontendUrl()
      }
    },
    mounted(){
      var x = {}
      $.ajax({
        url: this.getBackendUrl() + "mockserverApi/listAllProjects",
        cache: false,
        async: false,
        success: function (ret) {
          x=ret
        },
     })
      if (x.status == 0) {
        this.projects = x.data
      } else {
        this.$message({"type": "error", "text": x.msg})
      }
    },
    components:{
      newButton
    }
  }
</script>
<style scoped>
  .ta-c {
    text-align: center;
}
.mc {
    width: 1200px;
    margin: 0 auto;
}
.home-body{
  margin-top:75px;
  text-align: center;
}
.home-projects {
    width: 800px;
    margin-top: 80px;
}
.home-projects .home-p-title {
    background-color: transparent;
    box-shadow: none;
}
.home-projects>div {
    background-color: #fff;
    padding: 0 20px;
    margin-top: 10px;
    height: 40px;
    line-height: 40px;
    box-shadow: 0px 2px 10px #ccc;
}
.col-sm-2 {
    width: 16.66666667%;
}
.col-sm-3 {
    width: 25%;
}
.col-sm-4 {
    width: 33.33333333%;
}
.col-sm-1, .col-sm-10, .col-sm-11, .col-sm-12, .col-sm-2, .col-sm-3, .col-sm-4, .col-sm-5, .col-sm-6, .col-sm-7, .col-sm-8, .col-sm-9 {
    float: left;
    padding-left: 15px;
}
div, p {
    box-sizing: border-box;
}
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
div {
    display: block;
}

  .home-body .new-project-btn {
    margin: 0 auto;
    width: 200px;
    padding-top: 50px;
    padding-bottom: 50px;
}
</style>
