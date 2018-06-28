<template>
  <div class="container">
    <dashboardHeader></dashboardHeader>
    <dashboardBody></dashboardBody>
  </div>
</template>
<script>
  import dashboardHeader from './dashboardHeader.vue'
  import dashboardBody from './dashboardBody.vue'

  export default {
    name: 'dashboardMain',
    data: function () {
      return {
        user: ""
      }
    },
    components: {
      dashboardHeader,
      dashboardBody
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
<style scoped></style>
