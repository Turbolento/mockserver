<template>
  <div class="container">
    <div>
      <div id="login" class="login-form mc">
        <form class="form" method="post">
          <div class="ta-c logo">
            <a>
              <img src="../assets/mockLogo.png" width="174px"/>
            </a>
          </div>
          <div class="item">
            <input type="text" initial="off" name="account" id="account" tabindex="1" maxlength="45" placeholder="账户名"
                   class="text touched dirty" v-bind:class="{ invalid: invalid1}" aria-required="true"
                   aria-invalid="false">
            <p class="tip">{{tip1}}</p>
          </div>
          <div class="item">
            <input type="password" name="password" id="password" initial="off" tabindex="2" placeholder="密码"
                   class="text" v-bind:class="{ invalid: invalid2}" aria-required="true" aria-invalid="false"
                   v-on:keyup.enter="submit()">
            <p class="tip" style="">{{tip2}}</p></div>
          <div class="item">
            <input type="button" tabindex="3" id="login-btn" value="登陆" class="btn" v-on:click="submit()">
          </div>
          <div class="item">
            <div class="col-sm-8">
              <a href="#">忘记密码</a>
              <a href="#">免费注册</a>
            </div>
            <div class="col-sm-4">
              <label>
                <input type="checkbox"> 记住密码</label>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>
<script>
  import JSEncrypt from 'jsencrypt'

  export default {
    name: 'login',
    data: function () {
      return {
        tip1: "",
        tip2: "",
        invalid1: false,
        invalid2: false,
        account: '',
        passwd: '',
        backend: this.getBackendUrl()
      }
    },
    mounted() {
      var backend_url = this.getBackendUrl()
      $.ajax({
        url: backend_url + "mockserverApi/", dataType: "JSON", async: false, success: function (ret) {
          x = ret
        }
      })
      var next = this.getQueryVariable('next')
      if (this.checkNone(next)) {
        this.$message({"type": "warning", "text": "用户未登陆！请先登录！"})
      }
    },
    methods: {
      submit: function () {
        var account = document.getElementById("account").value
        var passwd = document.getElementById("password").value
        if (!this.checkNone(account)) {
          this.invalid1 = true
          this.tip1 = "请输入账户名"
        } else {
          this.invalid1 = false
        }
        if (!this.checkNone(passwd)) {
          this.invalid2 = true
          this.tip2 = "请输入密码"
        } else {
          this.invalid2 = false
        }
        if (this.checkNone(account) && this.checkNone(passwd)) {
          var publick_key = "-----BEGIN PUBLIC KEY-----\n" +
            "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCyBoTW4XaXIU942cz0Vw9v4hMg\n" +
            "wq8HP+ShE+5F52uiTGC4rd3LAhvGv7fFFcyXxWhb21oPsxVEOJybdqEUhv29ViMP\n" +
            "rfZmacdn0iSCfN7wwjdHpUWUEvuM01BIG8dVRhrFqU/Jkes+RD2gMK4cio8rNHYS\n" +
            "6kMqN0pEV9sFAL9oYwIDAQAB\n" +
            "-----END PUBLIC KEY-----"
          const encrypt = new JSEncrypt()
          encrypt.setPublicKey(publick_key)
          var re1 = /[a-zA-Z]/i
          var re2 = /[1-9]/i
          if (passwd.length < 6 || !(re1.test(passwd) && re2.test(passwd))) {
            this.invalid2 = true
            this.tip2 = "密码不合法！"
          } else {
            this.invalid2 = false
            var encryptPwd = encrypt.encrypt(passwd)
            var ret_status = null
            var ret_msg = null
            var onconnect = false
            $.ajax({
              url: this.backend + "mockserverApi/login",
              type: "POST",
              cache: false,
              async: false,
              data: {"account": account, "passwd": encryptPwd, "_xsrf": this.getCookie("_xsrf")},
              success: function (ret) {
                ret_status = ret.status
                ret_msg = ret.msg
              },
              error: function () {
                onconnect = true
              }
            })
            if (onconnect) {
              this.$message({"type": "error", "text": "登录失败，服务器错误！"})
            } else if (ret_status == 0) {
              var next = this.getQueryVariable('next')
              if (this.checkNone(next)) {
                var t = decodeURIComponent(next)
                window.location.href = this.getFrontendUrl() + t
              } else {
                this.$message({"type": "success", "text": "登录成功！"})
                window.location.href = this.getFrontendUrl() + "dashboard"
              }
            } else {
              this.$message({"type": "error", "text": ret_msg})
            }
          }
        }
      }
    }
  }
</script>
<style scoped>
  /*.container{*/
  /*padding-left:38.5%;*/
  /*}*/
  .form {
    width: 400px;
    text-align: left;
  }

  .iconfont {
    margin: 0 4px;
    font-size: inherit;
  }

  .login-form [type='button']:hover {
    background-color: #0061c1;
  }

  .login-form [type='button'] {
    width: 100%;
    padding: 10px 0;
    background: #0f6ecd;
    color: #fff;
  }

  [v-cloak] {
    display: none;
  }

  [class*=uk-modal-close-] {
    left: auto !important;
  }

  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }

  ::-webkit-scrollbar-track {
    -webkit-box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.3);
    background-color: #fff;
  }

  ::-webkit-scrollbar {
    width: 6px;
    background-color: #fff;
  }

  ::-webkit-scrollbar:horizontal {
    height: 6px;
  }

  ::-webkit-scrollbar-thumb {
    background-color: #8A8A8A;
    border-radius: 2px;
    -webkit-box-shadow: inset 0 0 6px rgba(0, 0, 0, .3);
  }

  input:-webkit-autofill,
  input:-webkit-autofill:hover,
  input:-webkit-autofill:focus,
  input:-webkit-autofill:active {
    transition: background-color 5000s ease-in-out 0s;
  }

  article, aside, footer, header, main, nav, section, code {
    display: block;
  }

  pre, xmp, plaintext, listing {
    font: 13px/1.5 consolas, 'Microsoft Yahei', tahoma, sans-serif;
  }

  code {
    background: #E7E7E7;
    padding: 5px;
    box-sizing: border-box;
  }

  li {
    list-style: none;
  }

  div, p {
    box-sizing: border-box;
  }

  img {
    border: none;
  }

  body ul {
    padding: 0;
    margin: 0;
  }

  .cb:after {
    clear: both;
    content: '';
    display: block;
  }

  .fl {
    float: left;
  }

  .fr {
    float: right;
  }

  .ta-c {
    text-align: center;
  }

  a {
    text-decoration: none;
    cursor: pointer;
    color: #1e87f0;
  }

  a:hover {
    color: #0f6ecd;
  }

  a.active {
    color: #1e87f0 !important;
  }

  .mc {
    width: 1200px;
    margin: 0 auto;
  }

  input, textarea {
    outline: none;
  }

  .text {
    width: 100%;
    padding: 10px 12px;
    font-size: 14px;
    border: 1px solid #C3C3C3;
    box-sizing: border-box;
    font-family: consolas, 'Microsoft Yahei', tahoma, sans-serif
  }

  .text:focus {
    border-color: #1e87f0;
  }

  .select {
    width: 100%;
    border: 1px solid #C3C3C3;
    padding: 2px 8px;
    box-sizing: border-box;
    outline: none;
    /*-webkit-appearance: none;*/
    -webkit-border-radius: 0;
  }

  @-webkit-keyframes sk-stretchdelay {
    0%, 40%, 100% {
      -webkit-transform: scaleY(0.4);
      -moz-transform: scaleY(0.4);
      -ms-transform: scaleY(0.4);
      -o-transform: scaleY(0.4);
      transform: scaleY(0.4);
    }
    20% {
      -webkit-transform: scaleY(1);
      -moz-transform: scaleY(1);
      -ms-transform: scaleY(1);
      -o-transform: scaleY(1);
      transform: scaleY(1);
    }
  }

  @-ms-keyframes sk-stretchdelay {
    0%, 40%, 100% {
      -webkit-transform: scaleY(0.4);
      -moz-transform: scaleY(0.4);
      -ms-transform: scaleY(0.4);
      -o-transform: scaleY(0.4);
      transform: scaleY(0.4);
    }
    20% {
      -webkit-transform: scaleY(1);
      -moz-transform: scaleY(1);
      -ms-transform: scaleY(1);
      -o-transform: scaleY(1);
      transform: scaleY(1);
    }
  }

  @-moz-keyframes sk-stretchdelay {
    0%, 40%, 100% {
      -webkit-transform: scaleY(0.4);
      -moz-transform: scaleY(0.4);
      -ms-transform: scaleY(0.4);
      -o-transform: scaleY(0.4);
      transform: scaleY(0.4);
    }
    20% {
      -webkit-transform: scaleY(1);
      -moz-transform: scaleY(1);
      -ms-transform: scaleY(1);
      -o-transform: scaleY(1);
      transform: scaleY(1);
    }
  }

  @keyframes sk-stretchdelay {
    0%, 40%, 100% {
      -webkit-transform: scaleY(0.4);
      -moz-transform: scaleY(0.4);
      -ms-transform: scaleY(0.4);
      -o-transform: scaleY(0.4);
      transform: scaleY(0.4);
    }
    20% {
      -webkit-transform: scaleY(1);
      -moz-transform: scaleY(1);
      -ms-transform: scaleY(1);
      -o-transform: scaleY(1);
      transform: scaleY(1);
    }
  }

  @-webkit-keyframes sk-bounce {
    0%, 100% {
      -webkit-transform: scale(0.0);
      transform: scale(0.0);
      opacity: 0.7;
    }
    50% {
      -webkit-transform: scale(1.0);
      transform: scale(1.0);
      opacity: 1
    }
  }

  @-ms-keyframes sk-bounce {
    0%, 100% {
      -ms-transform: scale(0.0);
    }
    50% {
      -ms-transform: scale(1.0);
      opacity: 1
    }
  }

  @keyframes sk-bounce {
    0%, 100% {
      transform: scale(0);
    }
    50% {
      transform: scale(1);
    }
  }

  .form .item {
    border-bottom: 1px solid #efefef;
    margin: 0;
    padding: 10px 0;
  }

  .form .item:after {
    clear: both;
    content: '';
    display: block;
  }

  .form .item:last-child {
    border-bottom: none;
  }

  .form .tip {
    margin: 5px 0;
    color: #ffa3a3;
    display: none;
  }

  .form .hint {
    color: #919191;
    margin-top: 5px;
  }

  .form .error {
    color: #ffa3a3;
  }

  .form .error .text {
    border-color: #ffa3a3;
  }

  .form .invalid {
    border-color: #ffa3a3;
  }

  .form .invalid ~ .tip {
    color: #ffa3a3;
    display: inherit;
  }

  .form .title {
    font-size: 18px;
    padding-left: 15px;
  }

  .form .label {
    text-align: right;
    display: inline-block;
    padding-top: 10px;
  }

  .form .label-content {
    padding-top: 10px;
  }

  .form .full-text {
    padding-top: 6px;
  }

  .div-table {
    width: 100%;
  }

  .div-table-header li {
    background-color: #fff;
    padding: 8px 10px;
    border-top: 1px solid #ccc !important
  }

  .div-table .sortable-placeholder {
    width: 100%;
    height: 32px;
    background-color: #ddecf4;
  }

  .div-table .icon-drag-copy {
    cursor: move;
  }

  .div-table-line li {
    padding: 10px 0 10px 10px;
    box-sizing: border-box;
    border: 1px solid #ccc;
    border-left: none;
    border-top: none;
    outline: none;
    position: relative;
    height: 35px;
  }

  .div-table-line li .value {
    overflow: hidden;
    height: 20px;
    text-overflow: ellipsis;
  }

  .div-table-line li .hover {
    display: none;
    word-break: break-all;
    z-index: 10;
  }

  .div-table-line li .hover.name {
    left: 0;
    background: #f0f0f0;
  }

  .div-table-line li .hover.description {
    left: 0;
    background: #f0f0f0;
    padding-left: 10px;
  }

  .div-table-line li:hover {
    background: #f0f0f0;
  }

  .div-table-line li:hover .hover {
    position: absolute;
    display: block;
  }

  .div-table-line li:hover .value {
    display: none;
  }

  .div-table-line li:first-child {
    border-left: 1px solid #ccc;
  }

  .div-table-line .sub {
    padding: 0;
    border: none;
    height: auto;
  }

  .div-table-line .name {
    color: red;
  }

  .div-table.editing .input {
    overflow: hidden;
    padding: 0;
  }

  .div-table.editing .input .text {
    border-color: transparent;
  }

  .div-table.editing .in-text {

  }

  .div-table-line .name {
    padding-left: 10px;
    overflow: visible;
    position: relative;
  }

  .div-table-line .name .iconfont {
    color: #666;
    font-size: 14px;
    position: absolute;
    left: -16px;
    top: 8px;
    width: 16px;
    height: 16px;
    background-position: center;
    background-repeat: no-repeat;
  }

  .div-table-line .name .icon-my {
    background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAQAAAAHCAQAAACFbCRbAAAAIGNIUk0AAHolAACAgwAA+f8AAIDpAAB1MAAA6mAAADqYAAAXb5JfxUYAAAACYktHRAD/h4/MvwAAAAlwSFlzAAALEwAACxMBAJqcGAAAAAl2cEFnAAAABAAAAAcAwQJp2AAAACVJREFUCNctxjEBACAMA7BQsXgCs+UYV+K0qsIthGmY/uyVgQw83VQKohVhLVcAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTQtMDktMjNUMTQ6MzM6NDgrMDg6MDBYHUu3AAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE0LTA5LTIzVDE0OjMzOjQ4KzA4OjAwKUDzCwAAAABJRU5ErkJggg==");
  }

  .div-table-line .name .icon-my.open {
    background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAcAAAAECAQAAADoz+32AAAAIGNIUk0AAHolAACAgwAA+f8AAIDpAAB1MAAA6mAAADqYAAAXb5JfxUYAAAACYktHRAD/h4/MvwAAAAlwSFlzAAALEwAACxMBAJqcGAAAAAl2cEFnAAAABwAAAAQAbLtItQAAACdJREFUCNdNiMENAEAIg6jDdienrQ9zOfkQUIdDWT+sgjcsIITQWQ/KugrMocu3oAAAACV0RVh0ZGF0ZTpjcmVhdGUAMjAxNC0wOS0yM1QxNDozMzo0OCswODowMFgdS7cAAAAldEVYdGRhdGU6bW9kaWZ5ADIwMTQtMDktMjNUMTQ6MzM6NDgrMDg6MDApQPMLAAAAAElFTkSuQmCC");
  }

  .div-table-line .div-table-line .name {
    padding-left: 25px;
  }

  .div-table-line .div-table-line .div-table-line .name {
    padding-left: 40px;
  }

  .div-table-line .div-table-line .div-table-line .div-table-line .name {
    padding-left: 55px;
  }

  .div-table-line .div-table-line .div-table-line .div-table-line .div-table-line .name {
    padding-left: 70px;
  }

  .div-table-line .div-table-line .div-table-line .div-table-line .div-table-line .div-table-line .name {
    padding-left: 85px;
  }

  .div-table-line .div-table-line .div-table-line .div-table-line .div-table-line .div-table-line .div-table-line .name {
    padding-left: 100px;
  }

  .div-table-line .div-table-line .div-table-line .div-table-line .div-table-line .div-table-line .div-table-line .div-table-line .name {
    padding-left: 115px;
  }

  .div-table-line .div-table-line .div-table-line .div-table-line .div-table-line .div-table-line .div-table-line .div-table-line .div-table-line.name {
    padding-left: 130px;
  }

  .div-table-line .div-table-line .div-table-line .div-table-line .div-table-line .div-table-line .div-table-line .div-table-line .div-table-line .div-table-line .name {
    padding-left: 145px;
  }

  .div-table-line .div-table-line .div-table-line .div-table-line .div-table-line .div-table-line .div-table-line .div-table-line .div-table-line .div-table-line .div-table-line.name {
    padding-left: 160px;
  }

  .col-sm-1, .col-sm-10, .col-sm-11, .col-sm-12, .col-sm-2, .col-sm-3, .col-sm-4, .col-sm-5, .col-sm-6, .col-sm-7, .col-sm-8, .col-sm-9 {
    float: left;
    padding-left: 15px
  }

  .col-sm-12 {
    width: 100%
  }

  .col-sm-11 {
    width: 91.66666667%
  }

  .col-sm-10 {
    width: 83.33333333%
  }

  .col-sm-9 {
    width: 75%
  }

  .col-sm-8 {
    width: 66.66666667%
  }

  .col-sm-7 {
    width: 58.33333333%
  }

  .col-sm-6 {
    width: 50%
  }

  .col-sm-5 {
    width: 41.66666667%
  }

  .col-sm-4 {
    width: 33.33333333%
  }

  .col-sm-3 {
    width: 25%
  }

  .col-sm-2 {
    width: 16.66666667%
  }

  .col-sm-1 {
    width: 8.33333333%
  }

  ul[uk-tab] {
    margin-top: 10px;
    margin-bottom: 10px;
  }

  .uk-modal-dialog {
    margin-top: 80px !important;
  }

  .uk-button {
    padding: 0 15px !important;
    line-height: 28px !important;
    border-radius: 4px;
  }

  /*************** ç™»å½•ã€æ³¨å†Œã€å¿˜è®°å¯†ç ã€æ‰¾å›žå¯†ç  start*******************/

  .login-form {
    width: 400px !important;
    margin-top: 120px !important;
  }

  .login-form.succeed {
    width: 600px;
  }

  .login-form .logo {
    margin-bottom: 30px;
  }

  .login-form .text {
    padding-top: 10px;
    padding-bottom: 10px;
  }

  .login-form [type='button'] {
    width: 100%;
    padding: 10px 0;
    background: #0f6ecd;
    color: #fff;
  }

  .login-form [type='button']:hover {
    background-color: #0061c1;
  }

  .login-third {
    margin: 10px 0;
  }

  .login-third img {
    width: 28px;
    margin-right: 2px;
  }

  .login-register-body .forget-succeed {
    border: 1px solid #c0ebd0;
    background-color: #f4fbf6;
    color: #47b26f;
    line-height: 30px;
    padding: 20px;
  }

  .lf-gotomail {
    padding: 10px 25px;
  }

  .lf-gotomail:hover {
    color: #fff;
  }

  .lr-friendly-tip {
    margin-top: 30px;
    color: #9e9e9e;
  }

  /*************** ç™»å½•ã€æ³¨å†Œã€å¿˜è®°å¯†ç ã€æ‰¾å›žå¯†ç  end*******************/

  /****** component *******/
  .x-ul {
  }

  .x-ul .x-li {
    padding: 0 15px;
    white-space: nowrap;
  }

  .x-ul.horiz:after {
    clear: both;
    content: ' ';
    display: block;
  }

  .x-ul.horiz > li {
    float: left;
    position: relative;
  }

  .x-ul .x-sub-ul {
    display: none;
    position: absolute;
    line-height: 30px;
    z-index: 10;
    background-color: #fff;
    box-shadow: 2px 2px 4px #ccc;
  }

  .x-ul .x-sub-ul .x-li:hover {
    background-color: #f0f0f0;
  }

  .x-ul li:hover .x-sub-ul {
    display: block;
  }

  /****/
  .user-account-logo {
    width: 40px;
    height: 40px;
    border-radius: 100%;
  }
</style>
