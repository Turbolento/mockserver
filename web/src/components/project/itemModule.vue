<template>
  <div class="panel">
        <div class="panel-heading">
            <h4 class="panel-title" :class="'pt'+mid" v-on:click="changeLocation()" :id="'mid'+mid" data-toggle="collapse" :href="'#collapseOne'+mid" data-parent="#accordion">
                <a>
                  {{moduleName}}
                </a>


                <div class="dropdown item-setting" >
                      <div class="dropdown-toggle " data-toggle="dropdown" data-submenu="" aria-expanded="false">
                        <i class="fa fa-caret-down"></i>
                      </div>

                      <div class="dropdown-menu" x-placement="bottom-start" style="top: 12px;">
                        <div class="dropdown dropright dropdown-submenu">
                            <button class="dropdown-item dropdown-toggle" type="button" data-toggle="dropdown">新建<i class="fa fa-caret-right"/></button>
                            <div class="dropdown-menu">
                              <button class="dropdown-item" type="button" :id="'modal-'+mid" :href="'#modal-container-'+mid"  data-toggle="modal">mock响应</button>
                              <button class="dropdown-item" type="button" disabled="">mock请求</button>
                            </div>

                        </div>
                        <li class="divider"></li>
                        <button class="dropdown-item" type="button">重命名</button>
                        <button class="dropdown-item" type="button">删除</button>

                      </div>
                    </div>

            </h4>
        </div>

        <div :id="'collapseOne'+mid" class="collapse" :class="mid==curmid?'in panel-collapse'+mid:'panel-collapse'+mid">
            <div v-for="x in apis">
                <div class="panel-body" :id="'aid'+x.aid">
                  <a v-on:click="changeLocate_api(x.aid)">{{x.apiName}}</a>
                </div>
            </div>
        </div>
        <div class="modal fade" :id="'modal-container-'+mid" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
          <div class="modal-dialog">
            <div class="modal-content">
              <div class="modal-body" style="text-align: left">
                <label>请输入接口名称：</label>
                <input type="text" autofocus class="uk-input" :id="'newApiName'+mid"/>
              </div>
              <div class="modal-footer">
                 <button type="button" class="btn btn-default" data-dismiss="modal">取消</button> <button type="button" class="btn btn-primary" v-on:click="newApi()">创建</button>
              </div>
            </div>
          </div>
        </div>
    </div>
</template>
<script>
  import '../../assets/css/bootstrap-submenu.css'
  import '../../assets/js/bootstrap-submenu.js'
  export default {
    name:"itemModule",
    data:function () {
      return{
      }
    },
    methods:{
      newApi:function(){
        var apiName = document.getElementById('newApiName'+this.mid).value
        var x = null
        $.ajax({
          url:this.getBackendUrl()+"mockserverApi/newApi",
          type:"POST",
          async: false,
          data: {"aname": apiName, "mid": this.mid, "_xsrf": this.getCookie("_xsrf")},
          success: function (ret) {
                x=ret
              }
        })
        if (x.status == 0) {
          var pid = this.getQueryVariable('pid')
          var timestamp = (new Date()).valueOf()
          var mleng = String(this.mid).length
           window.location.href = this.getFrontendUrl()+"project?pid="+pid+"&ln="+timestamp.toString().slice(0,9-mleng)+this.mid+mleng+'2'+x.data;
        } else {
          this.$message({"type": "error", "text": x.msg})
        }
      },
      changeLocation:function () {
        this.$emit("changeLocation",1,this.mid)
      },
      changeLocate_api:function(aid){
        this.$emit("changeLocation",2,aid)
      }
    },
    mounted(){
      $('[data-submenu]').submenupicker();
      var mid = this.mid
       $('.panel-collapse'+mid).on('show.bs.collapse', function () {
         $('.pt'+mid).addClass('open');
                });
       $('.panel-collapse'+mid).on('hide.bs.collapse', function () {
         $('.pt'+mid).removeClass('open');
                });
    },
    props:['mid','moduleName','apis','curmid']
  }
</script>
<style scoped>
  .panel-body{
    text-align: left;
    padding:8px 8px 8px 30px;
  }
    .panel-body.active{
    background-color: #d1dbe5;
  }
  .dropdown-menu {
    top: -30px;
    left:80%;
    z-index: 3;
    min-width: 10rem;
    padding: 0.5rem 0;
    margin: 0.125rem 0 0;
    font-size: 1rem;
    color: #212529;
    text-align: left;
    list-style: none;
    background-color: #fff;
    background-clip: padding-box;
    border: 1px solid rgba(0, 0, 0, 0.15);
    border-radius: 0.25rem;
}
  .dropdown-submenu.dropright > .dropdown-toggle {
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.dropdown-item:hover, .dropdown-item:focus {
    color: #16181b;
    text-decoration: none;
    background-color: #f8f9fa;
}
button, html [type="button"], [type="reset"], [type="submit"] {
    -webkit-appearance: button;
}
.dropdown-item {
    display: block;
    width: 100%;
    padding: 0.25rem 1.5rem;
    clear: both;
    font-weight: 400;
    color: #212529;
    text-align: inherit;
    white-space: nowrap;
    background-color: transparent;
    border: 0;
}
.panel-title a{
  font-size: 14px;
  text-decoration: none;
}
.panel-title.active{
  background-color: #d1dbe5;
}
.panel-title:before{
        content:"\f0da";
        font-family: FontAwesome;
        font-style: normal;
        font-weight: normal;
        font-size: 18px;
        z-index: 3;
        position: absolute;
        left:-5px;
        color:#97a8be;
}
.panel-body:hover{
  background-color: #d1dbe5;
}
.panel-title.open:before{
        content:"\f0d7";
        font-family: FontAwesome;
        font-style: normal;
        font-weight: normal;
        font-size: 18px;
        z-index: 3;
        position: absolute;
        left:-5px;
        color:#97a8be;
}
.panel-title{
  padding:10px;
  text-indent: 1rem;
}
.panel-heading{
  text-align: left;
  padding:0px;
}
.panel-heading:hover{
    background: #d1dbe5;
}
.item-setting{
  position: absolute;
  z-index: 3;
  color: #090f3f;
  right:15px;
  display: none;
}
.item-setting:hover{
  cursor: pointer;
}
.panel-title:hover .item-setting{
  display: inline-block;
}
  .uk-input, .uk-select:not([multiple]):not([size]) {
    height: 40px;
    vertical-align: middle;
    display: inline-block;
}

.uk-input, .uk-select, .uk-textarea {
    max-width: 100%;
    width: 100%;
    border: 0 none;
    padding: 0 10px;
    background: #fff;
    color: #666;
    border: 1px solid #e5e5e5;
    -webkit-transition: .2s ease-in-out;
    transition: .2s ease-in-out;
    -webkit-transition-property: color,background-color,border;
    transition-property: color,background-color,border;
}
.uk-input, .uk-textarea {
    -webkit-appearance: none;
}
.uk-input {
    overflow: visible;
}
.uk-checkbox, .uk-input, .uk-radio, .uk-select, .uk-textarea {
    box-sizing: border-box;
    margin: 0;
    border-radius: 0;
    font: inherit;
}

input:not([type]), input[type="email" i], input[type="number" i], input[type="password" i], input[type="tel" i], input[type="url" i], input[type="text" i] {
    padding: 1px 0px;
}
input {
    -webkit-appearance: textfield;
    background-color: white;
    -webkit-rtl-ordering: logical;
    cursor: text;
    padding: 1px;
    border-width: 2px;
    border-style: inset;
    border-color: initial;
    border-image: initial;
}
input, textarea, select, button {
    text-rendering: auto;
    color: initial;
    letter-spacing: normal;
    word-spacing: normal;
    text-transform: none;
    text-indent: 0px;
    text-shadow: none;
    display: inline-block;
    text-align: start;
    margin: 0em;
    font: 400 13.3333px Arial;
}
input, textarea, select, button, meter, progress {
    -webkit-writing-mode: horizontal-tb;
}
</style>
