<template>
  <div class="home-header">
    <div class="mc cb ta-c">
        <span href="/" class="fl"><img src="../../assets/mockLogo.png" alt="logo"><div class="ftext">MOCKSERVER</div></span>
        <span class="header-titles">
                <a href="" class="active">我的</a>
                <a class="">回收站</a>
                <a class="">归档项目</a>
                <a >常见问题</a>
            </span>
        <div class="user-account fr" aria-expanded="false">
            <a href=""><img :src="userico" class="user-account-logo" alt=""> <span>管理员</span></a>
            <div class="account-menu"><a :href="frontend+'logout'">退出登录</a></div>
        </div>
    </div>
    <div class="line"></div>
  </div>
</template>
<script>
  export default{
    name:'dashboardHeader',
    data:function(){
      return{
        frontend: this.getFrontendUrl(),
        userico:require('../../assets/userdefault.jpg')
      }
    }
  }
</script>
<style scoped>
  .account-menu{
    display:none;
    position: absolute;
    z-index: 1020;
    box-sizing: border-box;
    min-width: 150px;
    padding: 15px;
    background: #fff;
    color: #666;
    box-shadow: 0 5px 12px rgba(0,0,0,.15);
    right: -90px;
  }
  .user-account:hover .account-menu{
    display: block;
  }
.home-header {
    background-color: #fff;
    height: 50px;
    position: relative;
}
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
div {
    display: block;
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
.fl {
    float: left;
}
.ftext{
  display: inline-block;
  font-size:large;
  letter-spacing: 0.05em;
  position:absolute;
  bottom: 10px;
  text-indent: 0.3em;
}
.ta-c {
    text-align: center;
}
.mc {
    width: 1200px;
    margin: 0 auto;
}
.cb:after {
    clear: both;
    content: '';
    display: block;
}
  .header-titles {
    width: 500px;
    margin: 0 auto;
}

  .fr {
    float: right;
}
  [v-cloak] {
    display: none;
}

body ul {
    padding: 0;
    margin: 0;
}
ol, ul {
    padding-left: 30px;
}
address, dl, fieldset, figure, ol, p, pre, ul {
    margin: 0 0 20px 0;
}
ol, ul {
    padding-right: 30px;
}
address, dl, fieldset, figure, ol, p, pre, ul {
    margin: 0 0 20px 0;
}


ul, menu, dir {
    display: block;
    list-style-type: disc;
    -webkit-margin-before: 1em;
    -webkit-margin-after: 1em;
    -webkit-margin-start: 0px;
    -webkit-margin-end: 0px;
    -webkit-padding-start: 40px;
}

  li {
    list-style: none;
}


li {
    display: list-item;
    text-align: -webkit-match-parent;
}

ul, menu, dir {
    display: block;
    list-style-type: disc;
    -webkit-margin-before: 1em;
    -webkit-margin-after: 1em;
    -webkit-margin-start: 0px;
    -webkit-margin-end: 0px;
    -webkit-padding-start: 40px;
}
Style Attribute {
    text-align: left;
    top: 50px;
    left: 1357px;
}
li {
    list-style: none;
}

li {
    display: list-item;
    text-align: -webkit-match-parent;
}

.uk-nav ul {
    margin: 0;
    padding: 0;
    list-style: none;
}

.uk-nav ul {
    margin: 0;
    padding: 0;
    list-style: none;
}

ul, menu, dir {
    display: block;
    list-style-type: disc;
    -webkit-margin-before: 1em;
    -webkit-margin-after: 1em;
    -webkit-margin-start: 0px;
    -webkit-margin-end: 0px;
    -webkit-padding-start: 40px;
}

.line {
    width: 100%;
    height: 1px;
    background-color: #f0f0f0;
}
  .home-header img {
    height: 40px;
    margin: 5px 0;
}
.user-account-logo {
    width: 40px;
    height: 40px;
    border-radius: 100%;
}
.user-account-logo {
    width: 40px;
    height: 40px;
    border-radius: 100%;
}

audio, canvas, img, video {
    max-width: 100%;
    height: auto;
    box-sizing: border-box;
}
audio, canvas, iframe, img, svg, video {
    vertical-align: middle;
}

audio, canvas, img, video {
    max-width: 100%;
    height: auto;
    box-sizing: border-box;
}
audio, canvas, iframe, img, svg, video {
    vertical-align: middle;
}

img {
    border: none;
    border-style: none;
}
audio, canvas, img, video {
    max-width: 100%;
    height: auto;
    box-sizing: border-box;
}
audio, canvas, iframe, img, svg, video {
    vertical-align: middle;
}
audio, canvas, img, video {
    max-width: 100%;
    height: auto;
    box-sizing: border-box;
}
audio, canvas, iframe, img, svg, video {
    vertical-align: middle;
}

.header-titles a {
    line-height: 50px;
    padding: 0 5px;
    color: #000;
}
::selection {
    background: #39f;
    color: #fff;
    text-shadow: none;
}
div, p {
    box-sizing: border-box;
}
::-webkit-scrollbar {
    width: 6px;
    background-color: #fff;
}
::-webkit-scrollbar-thumb {
    background-color: #8A8A8A;
    border-radius: 2px;
    -webkit-box-shadow: inset 0 0 6px rgba(0,0,0,.3);
}
::-webkit-scrollbar-track {
    -webkit-box-shadow: inset 0 0 6px rgba(0,0,0,0.3);
    background-color: #fff;
}
a {
    text-decoration: none;
    cursor: pointer;
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




</style>
