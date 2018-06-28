// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import './assets/css/button.css'
import './assets/css/bootstrap.min.css'
import './assets/css/font-awesome.min.css'
import './assets/js/bootstrap.min'
import VueDND from 'awe-dnd'

Vue.use(VueDND)

Vue.config.productionTip = false

Vue.prototype.getCookie = function(name){
        var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
        return r ? r[1] : undefined;
      }
Vue.prototype.checkNone = function(obj){
  if(obj == '' || obj == undefined || obj == null || obj == false){
    return false
  }else{
    return true
  }
}
Vue.prototype.$message = function(option){
    // this.$emit("antMessage",option.text,option.type)
    $('.ant-message-notice span').html(option.text)
     $('.ant-message-notice').addClass('ant-message-'+option.type)
     $('.ant-message').css('z-index',9999)
    $ ('.ant-message-notice').show ().delay (3000).fadeOut (function () {
              $('.ant-message').css('z-index',-1)
              $('.ant-message-notice').removeClass('ant-message-'+option.type)
            });
  }
Vue.prototype.getBackendUrl = function(){
  var runenv = process.env.NODE_ENV
  var backend_url = runenv=="development"?"http://localhost:8000/":"/"
  return backend_url
}
Vue.prototype.getFrontendUrl = function(){
  var runenv = process.env.NODE_ENV
  var frontend_url = runenv=="development"?"/":"/mockserver/"
  return frontend_url
}
Vue.prototype.getQueryVariable = function (variable) {
       var query = window.location.search.substring(1);
       var vars = query.split("&");
       for (var i=0;i<vars.length;i++) {
               var pair = vars[i].split("=");
               if(pair[0] == variable){return pair[1];}
       }
       return(false);
      }
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
