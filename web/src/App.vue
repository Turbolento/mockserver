<template>
  <div id="app">
    <router-view></router-view>
    <div class="ant-message">
        <div class="ant-content">
          <div class="ant-message-notice" :class="[type=='success'?'ant-message-success':'',type=='error'?'ant-message-error':'',type=='info'?'ant-message-info':'',type=='warning'?'ant-message-warning':'']">
              <span>{{message}}</span>
          </div>
        </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App',
  data:function(){
    return{
      type:'',
      message:''
    }
  },
  mounted(){
    if(!this.$route.matched || this.$route.matched.length === 0){
      window.location.href = this.getBackendUrl()+'errorpage/404/404.html?path='+this.$route.path
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
body{
    font: 13px/1.5 consolas,'Microsoft Yahei',tahoma,sans-serif;
    color: #333;
    background-color: #fff;
    min-width: 1255px;
}
html {
    font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;
    font-size: 16px;
    font-weight: 400;
    line-height: 1.5;
    -webkit-text-size-adjust: 100%;
    -ms-text-size-adjust: 100%;
    background: #fff;
    color: #666;
}
a.active {
    color: #1e87f0!important;
}
a, area, button, input, label, select, summary, textarea {
    touch-action: manipulation;
}
a {
    color: #1e87f0;
    text-decoration: none;
    cursor: pointer;
}
a {
    background-color: transparent;
    -webkit-text-decoration-skip: objects;
}
a, area, button, input, label, select, summary, textarea {
    touch-action: manipulation;
}
  .ant-message{
        position: fixed;
        z-index: -1;
        width:100%;
        top: 51px;
      }
      .ant-content{
        font-family: "Helvetica Neue For Number", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "Helvetica Neue", Helvetica, Arial, sans-serif;
        font-size: 14px;
        line-height: 1.5;
        color: rgba(0, 0, 0, 0.65);
        -webkit-box-sizing: border-box;
        box-sizing: border-box;
        pointer-events: none;
        display: inline-block;
      }
      .ant-message-notice{
        padding:16px 30px;
        font-size: 16px;
        color:black;
        border-radius: 4px;
        box-shadow:0 4px 12px rgba(0,0,0,0.15);
        background: white;
        display: none;
        pointer-events: all;
        box-sizing:border-box;
      }
      .ant-message-error:before{
        content:"\f057";
        font-family: FontAwesome;
        font-style: normal;
        font-weight: normal;
        font-size: 18px;
        margin-right:5px;
        z-index: 3;
        color:red;
      }
      .ant-message-info:before{
        content:"\f05a";
        font-family: FontAwesome;
        font-style: normal;
        font-weight: normal;
        font-size: 18px;
        margin-right:5px;
        z-index: 3;
        color: #4d7dff;
      }
      .ant-message-warning:before{
        content:"\f071";
        font-family: FontAwesome;
        font-style: normal;
        font-weight: normal;
        font-size: 18px;
        margin-right:5px;
        z-index: 3;
        color: #ffdd65;
      }
      .ant-message-success:before{
        content:"\f058";
        font-family: FontAwesome;
        font-style: normal;
        font-weight: normal;
        font-size: 18px;
        margin-right:5px;
        z-index: 3;
        color: #3da638;
      }
</style>
