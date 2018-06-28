<template>
  <div id="docLeft" class="doc-left">
    <div class="dl-doc-actions cb">
      <div class="fl dl-doc-action">
        <ul class="nav nav-tabs">
          <li class="cb">
            <div class="dl-doc dl-project-name">
              <div class="doc-name cb " style="margin-left:0px;"><span class="el-tree-expand is-leaf"></span>
                <a :href="frontend+'project?pid='+pid" style="text-decoration: none;color:black;">{{projectName}}</a>
              </div>
            </div>
          </li>
          <li class="dropdown" style="float:right">
            <a href="#" data-toggle="dropdown" class="dropdown-toggle"><i class="fa fa-plus"></i> 新建<strong
              class="caret"></strong></a>
            <ul class="dropdown-menu" style="top:0px;left:80%;">
              <li>
                <a id="modal-608045" href="#modal-container-608045" role="button" data-toggle="modal">功能模块</a>
              </li>
              <li class="divider">
              </li>
              <li>
                <a id="modal-608046" href="#modal-container-608046" role="button" data-toggle="modal">mock响应</a>
              </li>
              <li>
                <a>mock请求</a>
              </li>
            </ul>
          </li>
        </ul>
      </div>
    </div>
    <!--<input type="text" placeholder="搜索..." class="doc-search"/>-->

    <div class="panel-group" id="accordion">
      <itemModule v-for="module in modules" :key="module.mid" v-bind:mid="module.mid" :moduleName="module.moduleName"
                  :apis="module.apis"
                  v-on:changeLocation="doLocate" :curmid="curmid"></itemModule>
      <itemApi v-for="api in apis" v-on:changeLocation="doLocate" :key="'aid'+api.aid" :aid="api.aid"
               :aname="api.aname"></itemApi>
    </div>

    <div class="modal fade" id="modal-container-608045" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-body">
            <label>请输入模块名称：</label>
            <input type="text" autofocus class="uk-input" id="newModuleName"/>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-default" data-dismiss="modal">取消</button>
            <button type="button" class="btn btn-primary" v-on:click="newModule()">创建</button>
          </div>
        </div>
      </div>
    </div>
    <div class="modal fade" id="modal-container-608046" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-body">
            <label>请输入接口名称：</label>
            <input type="text" autofocus class="uk-input" id="newApiName"/>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-default" data-dismiss="modal">取消</button>
            <button type="button" class="btn btn-primary" v-on:click="newApi()">创建</button>
          </div>
        </div>
      </div>
    </div>

    <div class="modal fade" id="modal-container-874431" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>
            <h4 class="modal-title" id="myModalLabel">
              Consul环境配置
            </h4>
          </div>
          <div class="modal-body">
            <div class="tab-content">
              <table class="table table-condensed" id="consulTable">
                <thead>
                <tr>
                  <th>主机IP</th>
                  <th>端口</th>
                  <th>描述</th>
                  <th>操作</th>
                </tr>
                </thead>
                <tbody>
                <tr v-for="c,j in consuls" :id="'consulTr'+j" class="consul-item">
                  <td><input type="text" placeholder="请输入IP" v-model="c.ip" style="width:111px;"/></td>
                  <td><input type="text" placeholder="请输入端口" v-model="c.port" style="width:69px"/></td>
                  <td><input type="text" placeholder="请输入说明" v-model="c.desc"/></td>
                  <td>
                    <button v-on:click="removeConsul(j)"><i class="fa fa-remove"
                                                            style="margin: 0 4px;cursor:pointer;"></i></button>
                  </td>
                </tr>
                </tbody>
                <button class="btn btn-default btn-sm" style="margin-top:10px;" v-on:click="addConsul()"><i
                  class="fa fa-plus"></i>
                  添加环境
                </button>
              </table>
            </div>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-default" data-dismiss="modal">关闭</button>
            <button type="button" class="btn btn-primary" v-on:click="saveConsulEnv()">保存</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
  import itemModule from './itemModule.vue'
  import itemApi from './itemApi.vue'

  export default {
    name: 'sidebar',
    data: function () {
      return {
        backend: this.getBackendUrl(),
        frontend: this.getFrontendUrl(),
        projectName: '',
        pid: '',
        modules: [],
        apis: [],
        consuls: [],
      }
    },
    components: {
      itemModule,
      itemApi
    },
    methods: {
      saveConsulEnv: function () {
        var consulEnvs = []
        var consulTable = document.getElementById("consulTable")
        var Rows = consulTable.getElementsByClassName("consul-item");
        for (var i = 0; i < Rows.length; i++) {
          var Cells = Rows[i].getElementsByTagName('td');
          var ip = Cells[0].getElementsByTagName('input')[0].value
          if (!this.checkNone(ip)) {
            this.$message({"type": "error", "text": "IP不能为空！"})
            return
          }
          var port = Cells[1].getElementsByTagName('input')[0].value
          if (!this.checkNone(port)) {
            this.$message({"type": "error", "text": "端口不能为空！"})
            return
          }
          var desc = Cells[2].getElementsByTagName('input')[0].value
          consulEnvs.push({"ip": ip, "port": port, "desc": desc})
        }
        var x = null
        $.ajax({
          url: this.getBackendUrl() + "mockserverApi/saveConsulEnvInfo",
          type: "POST",
          async: false,
          data: {
            "consulEnvs": JSON.stringify(consulEnvs),
            "_xsrf": this.getCookie("_xsrf")
          },
          success: function (ret) {
            x = ret
          }
        })
        if (x.status == 0) {
          $('#modal-container-874431').modal('hide')
          this.$message({"type": "success", "text": x.msg})
        } else {
          this.$message({"type": "error", "text": x.msg})
        }
      },
      removeConsul: function (num) {
        var child = document.getElementById("consulTr" + num);
        child.parentNode.removeChild(child);
        var arr = this.consuls
        for (var i = 0; i < arr.length; i++) {
          if (arr[i].id == num) {
            arr.splice(i, 1);
            break;
          }
        }
      },
      addConsul: function () {
        this.consuls.push({
          "ip": "",
          "port": "8500",
          "desc": ""
        })
      },
      newModule: function () {
        var mname = document.getElementById('newModuleName').value
        var x = null
        $.ajax({
          url: this.backend + "mockserverApi/newModule",
          type: "POST",
          async: false,
          data: {"mname": mname, "pid": this.pid, "_xsrf": this.getCookie("_xsrf")},
          success: function (ret) {
            x = ret
          }
        })
        if (x.status == 0) {
          var timestamp = (new Date()).valueOf()
          window.location.href = this.getFrontendUrl() + "project?pid=" + this.pid + "&ln=" + timestamp.toString().slice(0, 10) + '1' + x.data;
        } else {
          this.$message({"type": "error", "text": x.msg})
        }
      },
      doLocate: function (locate, right) {
        if (locate == '1') {
          $('.panel-body').removeClass('active');
          $('.panel-title').removeClass('active');
          $('#mid' + right).addClass('active');
        } else {
          $('.panel-body').removeClass('active');
          $('.panel-title').removeClass('active');
          $('#aid' + right).addClass('active');
        }
        this.$emit("changeLocation", locate, right)
      },
      newApi: function () {
        var aname = document.getElementById('newApiName').value
        var x = null
        $.ajax({
          url: this.getBackendUrl() + "mockserverApi/newApi",
          type: "POST",
          async: false,
          data: {"aname": aname, "mid": '-' + this.pid, "_xsrf": this.getCookie("_xsrf")},
          success: function (ret) {
            x = ret
          }
        })
        if (x.status == 0) {
          var timestamp = (new Date()).valueOf()
          window.location.href = this.getFrontendUrl() + "project?pid=" + this.pid + "&ln=" + timestamp.toString().slice(0, 10) + '3' + x.data;
        } else {
          this.$message({"type": "error", "text": x.msg})
        }
      }
    },
    props: ['locate', 'right', 'curmid'],
    updated() {
      var locate = this.locate
      var right = this.right
      if (locate == '1') {
        $('.panel-body').removeClass('active');
        $('.panel-title').removeClass('active');
        $('#mid' + right).addClass('active');
      } else {
        if (locate == '2') {
          $('#mid' + this.curmid).addClass('open');
        }
        $('.panel-body').removeClass('active');
        $('.panel-title').removeClass('active');
        $('#aid' + right).addClass('active');
      }
    },
    mounted() {
      this.pid = this.getQueryVariable("pid")
      var x = null
      $.ajax({
        url: this.backend + "mockserverApi/getProjectName?pid=" + this.pid,
        async: false,
        success: function (ret) {
          x = ret
        }
      })
      if (x.status == 0) {
        this.projectName = x.data
      } else {
        this.$message({"type": "error", "text": x.msg})
      }
      x = null
      $.ajax({
        url: this.backend + "mockserverApi/listProjectModules?pid=" + this.pid,
        async: false,
        success: function (ret) {
          x = ret
        }
      })
      if (x.status == 0) {
        this.modules = x.data
      } else if (x.status == 1) {
        //模块记录为空
      } else {
        this.$message({"type": "error", "text": x.msg})
      }
      x = null
      $.ajax({
        url: this.backend + "mockserverApi/listProjectApis?pid=" + this.pid,
        async: false,
        success: function (ret) {
          x = ret
        }
      })
      if (x.status == 0) {
        this.apis = x.data
      } else {
        this.$message({"type": "error", "text": x.msg})
      }
      x = null
      $.ajax({
        url: this.backend + "mockserverApi/getConsulEnvInfo",
        async: false,
        success: function (ret) {
          x = ret
        }
      })
      if (x.status == 0) {
        this.consuls = x.data
      } else {
        this.$message({"type": "error", "text": x.msg})
      }
    }
  }
</script>
<style scoped>
  #consulTable input {
    border: none;
  }

  .modal-body {
    max-height: 500px;
    overflow-y: scroll;
  }

  .table-condensed > tbody > tr > td {
    padding: 9px 0px;
  }

  .doc-name {
    line-height: 35px;
    height: 35px;
    cursor: pointer;
    margin-left: 15px;
    display: block;
    text-overflow: ellipsis;
    white-space: nowrap;
    overflow: hidden;
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    font-weight: bold;
    font-size: 14px;
  }

  div, p {
    box-sizing: border-box;
  }

  .dl-docs .dl-project-name {
    margin-top: 7px;
    font-weight: bold;
    font-size: 14px;
  }

  li {
    list-style: none;
  }

  li {
    display: list-item;
    text-align: left;
  }

  .el-tree-expand.is-leaf {
    border-color: transparent;
    cursor: default;
  }

  .el-tree-expand {
    display: inline-block;
    cursor: pointer;
    width: 0;
    height: 0;
    vertical-align: middle;
    border: 6px solid transparent;
    border-right-width: 0;
    border-left-color: #97a8be;
    border-left-width: 7px;
    transform: rotate(0deg);
    transition: transform .3s ease-in-out;
    position: relative;
    z-index: 2;
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
    -webkit-transition-property: color, background-color, border;
    transition-property: color, background-color, border;
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
    border-width: 1px;
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

  .modal {
    text-align: left;
  }

  .doc-left {
    width: 250px;
    border-right: 1px solid rgba(0, 0, 0, .07);
    height: 100%;
    position: fixed;
    top: 0;
    left: 0px;
    bottom: 0;
    background-color: #fafafa;
    z-index: 9999;
    transition: margin-left .5s;
  }

  div, p {
    box-sizing: border-box;
  }

  .dl-menus, .dl-menus .sub {
    width: 130px;
    position: absolute;
    z-index: 3;
    background-color: #fff;
    box-shadow: 3px 3px 10px #ccc;
  }

  .doc-left .doc-search {
    width: 100%;
    height: 50px;
    line-height: 50px;
    background: #fff;
    padding-left: 14px;
    font-size: 14px;
    /*border: none;*/
    box-shadow: 0px 2px 5px #ccc;
  }

  ::-webkit-scrollbar {
    width: 6px;
    background-color: #fff;
  }

  ::-webkit-scrollbar-thumb {
    background-color: #8A8A8A;
    border-radius: 2px;
    -webkit-box-shadow: inset 0 0 6px rgba(0, 0, 0, .3);
  }

  ::-webkit-scrollbar-track {
    -webkit-box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.3);
    background-color: #fff;
  }

  ::selection {
    background: #39f;
    color: #fff;
    text-shadow: none;
  }
</style>
