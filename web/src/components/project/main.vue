<template>
  <div class="container">
    <sidebar v-bind:locate="locate" v-bind:right="right" :curmid="curmid" v-on:changeLocation="doLocate"></sidebar>
    <rightArea v-bind:locate="locate" v-bind:right="right"></rightArea>
  </div>
</template>
<script>
  import sidebar from './sidebar.vue'
  import rightArea from './rightArea.vue'

  export default {
    name: 'project',
    data: function () {
      return {
        locate: 0,      //0为空 , 1的时候取right为mid,  2的时候取right为aid
        right: 0
      }
    },
    methods: {
      doLocate: function (locate, right) {
        this.locate = locate
        this.right = right
      }
    },
    components: {
      sidebar,
      rightArea
    },
    created() {
      var ln = this.getQueryVariable('ln') || ""      //ln用来定位当前选项；规则：第10位表示moudleid的长度X，10位之前的倒数X位表示moudleid，
      //第11位表示位置，0初始，1选中模块，2选中模块中的api，3选中根路径下的api
      //从第12位到最后，具体选项定位，代表moudle_id或者api_id
      this.locate = ln.slice(10, 11) || 0
      this.curmid = 0;
      if (this.locate == '2') {
        var cmleng = ln.slice(9, 10)
        this.curmid = ln.slice(9 - cmleng, 9) || 0
      }
      this.right = ln.slice(11) || 0
    },
    mounted() {
      var runenv = process.env.NODE_ENV
      if (runenv != "development") {
        var x = {}
        var frontendurl = this.getFrontendUrl()
        var backend = this.getBackendUrl()
        $.ajax({
          url: backend + "mockserverApi/getauthinfo", dataType: "JSON", async: false, success: function (ret) {
            x = ret
          }
        })
        if (x.status == 10001) {
          var t = this.$route.fullPath.slice(1)
          window.location.href = frontendurl + 'login?next=' + encodeURIComponent(t)
        } else if (x.status == 0) {
          this.user = x.data
        }
      }
    }
  }
</script>
<style scoped>
</style>
