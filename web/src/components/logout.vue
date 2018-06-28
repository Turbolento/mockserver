<template>
  <h4 style="margin-top:30px;">
    <p>已退出！感谢您的登陆！</p>
    <p><a :href="this.getFrontendUrl()+'login'">重新登陆</a>，{{count}}秒后自动跳转到登录页...</p>
  </h4>
</template>
<script>
  export default {
    name: "logout",
    data() {
      return {
        count: 3,
        timer:null
      }
    },
    methods: {},
    mounted() {
      var backend = this.getBackendUrl()
      $.ajax({url: backend + "mockserverApi/logout", async: false})
      if (!this.timer) {
        this.timer = setInterval(() => {
          if (this.count > 0 && this.count <= 3) {
            this.count--;
          } else {
            clearInterval(this.timer);
            this.timer = null;
          }
        }, 1000)
      }
      setTimeout("window.location.href = '" + this.getFrontendUrl() + "login'", 3000)
    }
  }
</script>
<style scoped></style>
