<template>
  <div class="container" style="margin-top:55px;color: #333;">
    <h3 style="text-align: left">{{desc}}</h3>
  </div>
</template>
<script>
  export default{
    name:'projectIndex',
    data:function () {
      return{
        desc:""
      }
    },
    mounted(){
      this.pid=this.getQueryVariable("pid")
      var x = null
      $.ajax({
        url:this.getBackendUrl()+"mockserverApi/getProjectDesc?pid="+this.pid,
        async: false,
        success:function(ret){
          x = ret
        }
      })
      if (x.status == 0) {
          this.desc=x.data
        } else {
          this.$message({"type": "error", "text": x.msg})
        }
    }
  }
</script>
<style scoped>

</style>
