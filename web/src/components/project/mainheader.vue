<template>
  <div class="container xd-header cb">
    <ul class="nav nav-pills">
      <li class="dropdown">
        <a href="#" data-toggle="dropdown" class="dropdown-toggle">全局设置<strong class="caret"></strong></a>
        <ul class="dropdown-menu">
          <li>
            <a id="modal-874431" href="#modal-container-874431" role="button" class="btn"
               data-toggle="modal">consul配置</a>
          </li>
          <!--<li class="divider">-->
          <!--</li>-->
          <!--<li>-->
          <!--<a href="#">分割线</a>-->
          <!--</li>-->
        </ul>
      </li>
      <li class="dropdown">
        <a href="#" data-toggle="dropdown" class="dropdown-toggle">项目设置<strong class="caret"></strong></a>
        <ul class="dropdown-menu">
          <li>
            <a href="#">项目信息</a>
          </li>
          <li>
            <a href="#">项目成员</a>
          </li>
          <li class="divider">
          </li>
          <li>
            <a href="#">导出项目</a>
          </li>
        </ul>
      </li>
      <li class="dropdown">
        <a href="#" class="dropdown-toggle">历史记录</a>
      </li>
      <li class="dropdown">
        <label>|</label>
      </li>
      <li class="dropdown">
        <a href="#" class="dropdown-toggle"><i class="fa fa-eye"/> 项目预览</a>
      </li>
      <li class="dropdown">
        <a class="dropdown-toggle" style="color:#39f;" v-on:click="saveApi()"><i class="fa fa-save"/>
          保存</a>
      </li>
      <div class="user-account fr" aria-expanded="false">
        <a :href="frontend+'dashboard'"><img :src="userico"
                                             class="user-account-logo" alt=""> <span>管理员</span></a>
        <div class="account-menu">
          <a :href="frontend+'dashboard'">控制台</a><br/>
          <a :href="frontend+'logout'">退出登录</a>
        </div>
      </div>
    </ul>
  </div>
</template>
<script>
  export default {
    name: 'mainheader',
    data: function () {
      return {
        frontend: this.getFrontendUrl(),
        userico: require('../../assets/userdefault.jpg')
      }
    },
    props: ['locate', 'right'],
    methods: {
      saveApi: function () {
        if (this.locate == 2 || this.locate == 3) {
          var serviceName = document.getElementById('serviceName').value
          var uri = document.getElementById('uri').value
          var requestType = document.getElementById('requestType').value
          var method = document.getElementById('method').value
          var apiName = document.getElementById('apiName').value
          var apiDesc = document.getElementById('apiDesc').value||""
          var requestHeaderList = []
          var requestBodyList = []
          var responseHeaderList = []
          var responseBodyList = []
          if ((!this.checkNone(serviceName)) || (!this.checkNone(uri)) || (!this.checkNone(apiName))) {
            this.$message({"type": "error", "text": "[微服务名称/uri/接口名称]不能为空！"})
            return
          }

          var requestHeaderTable = document.getElementById("requestHeaderTable")
          var requestHeaderRows = requestHeaderTable.getElementsByClassName("requestHeader-item");
          for (var i = 0; i < requestHeaderRows.length; i++) {
            var requestHeaderCells = requestHeaderRows[i].getElementsByTagName('li');
            var name = requestHeaderCells[1].getElementsByTagName('input')[0].value
            if (!this.checkNone(name)) {
              this.$message({"type": "error", "text": "【请求头(HEADER)】中【参数名称】不能为空！"})
              return
            }
            var match = requestHeaderCells[2].getElementsByTagName('select')[0].value
            var value = requestHeaderCells[3].getElementsByTagName('input')[0].value
            var response = requestHeaderCells[4].getElementsByTagName('select')[0].value
            if (!this.checkNone(response)) {
              this.$message({"type": "error", "text": "请在【请求头(HEADER)】中指定【响应内容】！"})
              return
            }
            requestHeaderList.push({"name": name, "match": match, "value": value, "response": response})
          }
          var requestBodyTable = document.getElementById("requestBodyTable")
          var requestBodyRows = requestBodyTable.getElementsByClassName("requestBody-item");
          for (var i = 0; i < requestBodyRows.length; i++) {
            var requestBodyCells = requestBodyRows[i].getElementsByTagName('li');
            var name = requestBodyCells[2].getElementsByTagName('input')[0].value
            if (!this.checkNone(name)) {
              this.$message({"type": "error", "text": "【请求参数(Body)】中【参数名称】不能为空！"})
              return
            }
            var match = requestBodyCells[3].getElementsByTagName('select')[0].value
            var value = requestBodyCells[4].getElementsByTagName('input')[0].value
            var response = requestBodyCells[5].getElementsByTagName('select')[0].value
            if (!this.checkNone(response)) {
              this.$message({"type": "error", "text": "请在【请求参数(Body)】中指定【响应内容】！"})
              return
            }
            requestBodyList.push({"name": name, "match": match, "value": value, "response": response})
          }
          var responseHeaderTable = document.getElementById("responseHeaderTable")
          var responseHeaderRows = responseHeaderTable.getElementsByClassName("responseHeader-item");
          for (var i = 0; i < responseHeaderRows.length; i++) {
            var responseHeaderCells = responseHeaderRows[i].getElementsByTagName('li');
            var key = responseHeaderCells[1].getElementsByTagName('input')[0].value
            if (!this.checkNone(key)) {
              this.$message({"type": "error", "text": "响应头(Header)中[Key]不能为空！"})
              return
            }
            var value = responseHeaderCells[2].getElementsByTagName('input')[0].value
            var desc = responseHeaderCells[3].getElementsByTagName('input')[0].value
            responseHeaderList.push({"key": key, "value": value, "desc": desc})
          }
          var responseBodyTable = document.getElementById('responseBodyTable')
          var responseBodyRows = responseBodyTable.getElementsByClassName("responseBody-item");
          for (var i = 0; i < responseBodyRows.length; i++) {
            var responseBodyCells = responseBodyRows[i].getElementsByTagName('li');
            var name = responseBodyCells[1].getElementsByTagName('input')[0].value
            if (!this.checkNone(name)) {
              this.$message({"type": "error", "text": "响应体(Body)中[响应名称]不能为空！"})
              return
            }
            var type = responseBodyCells[2].getElementsByTagName('select')[0].value
            var status = responseBodyCells[3].getElementsByTagName('input')[0].value
            var response = responseBodyCells[4].getElementsByTagName('input')[0].value
            var desc = responseBodyCells[5].getElementsByTagName('input')[0].value
            responseBodyList.push({"name": name, "type": type, "status": status, "response": response, "desc": desc})
          }
          var x = null
          $.ajax({
            url: this.getBackendUrl() + "mockserverApi/saveApiData",
            type: "POST",
            async: false,
            data: {
              "aid": this.right,
              "serviceName": serviceName,
              "uri": uri,
              "requestType": requestType,
              "method": method,
              "apiName": apiName,
              "apiDesc": apiDesc,
              "requestHeaders": JSON.stringify(requestHeaderList),
              "requestBodys": JSON.stringify(requestBodyList),
              "responseHeaders": JSON.stringify(responseHeaderList),
              "responseBodys": JSON.stringify(responseBodyList),
              "_xsrf": this.getCookie("_xsrf")
            },
            success: function (ret) {
              x = ret
            }
          })
          if (x.status == 0) {
            this.$message({"type": "success", "text": x.msg})
            var labeldiv = document.getElementById('aid'+this.right)
            labeldiv.getElementsByTagName('a')[0].innerText=apiName
          } else {
            this.$message({"type": "error", "text": x.msg})
          }
        }
      }
    }
  }
</script>
<style scoped>
  .fr{
    float: right;
    margin-right: 680px;
  }
.account-menu{
    display:none;
    position: absolute;
    z-index: 1020;
    box-sizing: border-box;
    min-width: 150px;
    padding: 0px;
    background: #fff;
    color: #666;
    box-shadow: 0 5px 12px rgba(0,0,0,.15);
    right: 35%;
  }
  .user-account:hover .account-menu{
    display: block;
  }
  div, p {
    -webkit-box-sizing: border-box;
    box-sizing: border-box;
  }

  div {
    display: block;
  }

  * {
    margin: 0;
    padding: 0;
    -webkit-box-sizing: border-box;
    box-sizing: border-box;
  }

  * {
    margin: 0;
    padding: 0;
    -webkit-box-sizing: border-box;
    box-sizing: border-box;
  }

  * {
    -webkit-box-sizing: border-box;
    box-sizing: border-box;
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

  div {
    display: block;
  }

  .ta-c {
    text-align: center;
  }

  li.dropdown {
    height: 40px;
    line-height: 40px;
    vertical-align: middle;
  }

  li.dropdown > a {
    color: dimgrey;
    height: 40px;
    display: inline;
  }

  .xd-header {
    height: 40px;
    line-height: 40px;
    vertical-align: middle;
    box-shadow: 0px 2px 5px #ccc;
    background-color: #fff;
    z-index: 99;
    width: 100%;
    position: fixed;
  }
</style>
