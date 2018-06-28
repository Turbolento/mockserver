<template>
  <div class="container" style="margin-top:55px;color: #333;">
    <div class="row clearfix">
      <div class="col-md-12 column">
        <div class="tabbable" id="tabs-655829">
          <ul class="nav  my-nav-tabs">
            <li class="active">
              <a href="#panel-144087" data-toggle="tab">基本信息</a>
            </li>
          </ul>
          <div class="tab-content form">
            <div class="tab-pane active" id="panel-144087">

              <div class="item">
                <div class="col-sm-1 label">微服务名</div>
                <div class="col-sm-3">
                  <input id="serviceName" name="serviceName" type="text" placeholder="请输入微服务名称"
                         class="uk-input" v-model="serviceName">
                </div>
                <div class="col-sm-1 label">Uri路径</div>
                <div class="col-sm-3">
                  <input id="uri" name="uri" type="text" placeholder="请输入Uri路径：/api/test"
                         class="uk-input" v-model="uri">
                </div>

              </div>
              <div class="item">
                <div class="col-sm-1 label">请求数据类型</div>
                <div class="col-sm-3">
                  <select class="uk-select" id="requestType" name="requestType" v-model="requestType">
                    <option value="JSON">JSON</option>
                    <option value="X-WWW-FORM-URLENCODED">X-WWW-FORM-URLENCODED</option>
                    <option value="RAW">RAW</option>
                    <option value="XML">XML</option>
                  </select>
                </div>
                <div class="col-sm-1 label">请求方法</div>
                <div class="col-sm-3">
                  <select class="uk-select" id="method" name="method" v-model="method">
                    <option value="GET">GET</option>
                    <option value="POST">POST</option>
                    <option value="PUT">PUT</option>
                    <option value="DELETE">DELETE</option>
                    <option value="PATCH">PATCH</option>
                    <option value="COPY">COPY</option>
                    <option value="OPTIONS">OPTIONS</option>
                  </select>
                </div>
                <div class="col-sm-1 label">接口名称</div>
                <div class="col-sm-3">
                  <input id="apiName" name="apiName" type="text" placeholder="请输入接口名称" class="uk-input" v-model="apiName">
                </div>
              </div>
              <div class="item">
                <div class="col-sm-1 label">接口描述</div>
                <div class="col-sm-11">
                  <input id="apiDesc" name="apiDesc" type="text" class="uk-input" v-model="apiDesc">
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="row clearfix">
      <div class="col-md-12 column">
        <div class="tabbable" id="tabs-655244">
          <ul class="nav  my-nav-tabs">
            <li class="active">
              <a href="#panel-55604" data-toggle="tab">请求头(HEADER)</a>
            </li>
            <li>
              <a href="#panel-863831" data-toggle="tab">请求参数(BODY)</a>
            </li>
          </ul>
          <div class="tab-content">
            <div class="tab-pane active" id="panel-55604">
              <div class="tab-content" style="">
                <div class="div-table">
                  <ul class="div-table-header div-table-line cb">
                    <li class="col-sm-1">操作</li>
                    <li class="col-sm-3">参数名称</li>
                    <li class="col-sm-2">匹配</li>
                    <li class="col-sm-2">默认值</li>
                    <li class="col-sm-4">响应内容</li>
                  </ul>
                </div>
                <requestHeader :requestHeaders="requestHeaders" :responseBodys="responseBodys"></requestHeader>
                <div class="item">
                  <li class="col-sm-1">
                    <button class="btn btn-default btn-sm" v-on:click="addRequestHeader()"><i class="fa fa-plus"></i>
                      添加参数
                    </button>
                  </li>
                </div>
              </div>
            </div>
            <div class="tab-pane" id="panel-863831">
              <div class="tab-content" style="">
                <div class="div-table">
                  <ul class="div-table-header div-table-line cb">
                    <li class="col-sm-1">操作</li>
                    <li class="col-sm-1">参数类型</li>
                    <li class="col-sm-2">参数名称</li>
                    <li class="col-sm-2">匹配</li>
                    <li class="col-sm-3">默认值</li>
                    <li class="col-sm-3">响应内容</li>
                  </ul>
                </div>
                <requestBody :requestBodys="requestBodys" :responseBodys="responseBodys"></requestBody>
                <div class="item">
                  <li class="col-sm-1">
                    <button class="btn btn-default btn-sm" v-on:click="addRequestBody()"><i class="fa fa-plus"></i> 添加参数
                    </button>
                  </li>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="row clearfix">
      <div class="col-md-12 column">
        <div class="tabbable" id="tabs-849910">
          <ul class="nav  my-nav-tabs">
            <li>
              <a href="#panel-31054" data-toggle="tab">公共响应头(HEADER)</a>
            </li>
            <li class="active">
              <a href="#panel-678633" data-toggle="tab">响应数据(BODY)</a>
            </li>
          </ul>
          <div class="tab-content">
            <div class="tab-pane" id="panel-31054">
              <div class="tab-content" style="">
                <div class="div-table">
                  <ul class="div-table-header div-table-line cb">
                    <li class="col-sm-1">操作</li>
                    <li class="col-sm-2">Key</li>
                    <li class="col-sm-4">Value</li>
                    <li class="col-sm-5">描述</li>
                  </ul>
                </div>
                <responseHeader :responseHeaders="responseHeaders"></responseHeader>
                <div class="item">
                  <li class="col-sm-1">
                    <button class="btn btn-default btn-sm" v-on:click="addResponseHeader()"><i class="fa fa-plus"></i>
                      添加响应头
                    </button>
                  </li>
                </div>
              </div>
            </div>
            <div class="tab-pane active" id="panel-678633">
              <div class="tab-content" style="">
                <div class="div-table">
                  <ul class="div-table-header div-table-line cb">
                    <li class="col-sm-1">操作</li>
                    <li class="col-sm-2">响应名称</li>
                    <li class="col-sm-2">响应类型</li>
                    <li class="col-sm-1">状态码</li>
                    <li class="col-sm-3">响应值</li>
                    <li class="col-sm-3">描述</li>
                  </ul>
                </div>
                  <responseBody :responseBodys="responseBodys"></responseBody>
                <div class="item">
                  <li class="col-sm-1">
                    <button class="btn btn-default btn-sm" v-on:click="addResponseBody()"><i class="fa fa-plus"></i>
                      添加响应
                    </button>
                  </li>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
  import requestHeader from './requestHeader'
  import requestBody from './requestBody'
  import responseHeader from './responseHeader'
  import responseBody from './responseBody'
  export default {
    name: 'maincontent',
    data: function () {
      return {
        apiName:'',
        serviceName:"",
        uri:"",
        requestType:"",
        method:"",
        apiDesc:"",
        requsetHeaderCount: 0,
        requsetBodyCount: 0,
        responseHeaderCount: 0,
        responseBodyCount:0,
        requestHeaders:[],
        requestBodys:[],
        responseHeaders:[],
        responseBodys:[],
      }
    },
    props: ['aid'],
    components:{
      requestHeader,
      requestBody,
      responseHeader,
      responseBody
    },
    methods: {
      addRequestHeader: function () {
        this.requestHeaders.push({
          id:this.requsetHeaderCount,
          name:"",
          match:"0",
          value:"",
          response:""
        })
        this.requsetHeaderCount+=1
      },
      addRequestBody: function () {
        this.requestBodys.push({
          id:this.requsetBodyCount,
          name:"",
          match:"0",
          value:"",
          response:""
        })
        this.requsetBodyCount+=1
      },
      addResponseHeader: function () {
        this.responseHeaders.push({
          id:this.responseHeaderCount,
          key:"",
          value:"",
          desc:""
        })
        this.responseHeaderCount+=1
      },
      addResponseBody: function () {
        this.responseBodys.push({
          id:this.responseBodyCount,
          name: "",
          type:"json",
          status:"200",
          response:"",
          desc:""
        })
        this.responseBodyCount+=1
      }
    },
    mounted(){
       var x = null
      $.ajax({
        url:this.getBackendUrl()+"mockserverApi/getApiData?aid="+this.aid,
        async: false,
        success:function(ret){
          x = ret
        }
      })
      if (x.status == 0) {
          this.apiName = x.data.apiName
          this.method = x.data.method||"GET"
          this.requestType = x.data.requestType||"JSON"
          this.apiDesc = x.data.apiDesc
          this.serviceName = x.data.serviceName
          this.uri = x.data.uri
          this.requestHeaders = x.data.requestHeaders||[]
          this.requestBodys = x.data.requestBodys||[]
          this.responseHeaders = x.data.responseHeaders||[]
          this.responseBodys = x.data.responseBodys||[]
          this.requsetHeaderCount =this.requestHeaders.length||0
          this.requsetBodyCount=  this.requestBodys.length||0
          this.responseHeaderCount= this.responseHeaders.length||0
          this.responseBodyCount= this.responseBodys.length||0
        } else {
          this.$message({"type": "error", "text": x.msg})
        }
    },
    watch:{
      aid:function(newValue){
        var x = null
      $.ajax({
        url:this.getBackendUrl()+"mockserverApi/getApiData?aid="+newValue,
        async: false,
        success:function(ret){
          x = ret
        }
      })
      if (x.status == 0) {
          this.apiName = x.data.apiName
          this.method = x.data.method||"GET"
          this.requestType = x.data.requestType||"JSON"
          this.apiDesc = x.data.apiDesc
          this.serviceName = x.data.serviceName
          this.uri = x.data.uri
          this.requestHeaders = x.data.requestHeaders||[]
          this.requestBodys = x.data.requestBodys||[]
          this.responseHeaders = x.data.responseHeaders||[]
          this.responseBodys = x.data.responseBodys||[]
          this.requsetHeaderCount =this.requestHeaders.length||0
          this.requsetBodyCount=  this.requestBodys.length||0
          this.responseHeaderCount= this.responseHeaders.length||0
          this.responseBodyCount= this.responseBodys.length||0
        } else {
          this.$message({"type": "error", "text": x.msg})
        }
      }
    }
  }
</script>
<style scoped>
  .div-table {
    width: 100%;
  }

  div, p {
    box-sizing: border-box;
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

  .div-table-line li:first-child {
    border-left: 1px solid #ccc;
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

  .div-table-header li {
    background-color: #fff;
    padding: 8px 10px;
    border-top: 1px solid #ccc !important;
  }

  .col-sm-1 {
    width: 8.33333333%;
  }

  .col-sm-1, .col-sm-10, .col-sm-11, .col-sm-12, .col-sm-2, .col-sm-3, .col-sm-4, .col-sm-5, .col-sm-6, .col-sm-7, .col-sm-8, .col-sm-9 {
    float: left;
    padding-left: 15px;
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

  .div-table.editing .input {
    overflow: hidden;
    padding: 0;
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

  .col-sm-3 {
    width: 25%;
  }

  .div-table.editing .input .text {
    border-color: transparent;
  }

  .div-table-line .name {
    padding-left: 10px;
    overflow: visible;
    position: relative;
  }

  .text {
    width: 100%;
    padding: 10px 12px;
    font-size: 14px;
    border: 1px solid #C3C3C3;
    box-sizing: border-box;
    font-family: consolas, 'Microsoft Yahei', tahoma, sans-serif;
  }

  input, textarea {
    outline: none;
  }

  a, area, button, input, label, select, summary, textarea {
    touch-action: manipulation;
  }

  a, area, button, input, label, select, summary, textarea {
    touch-action: manipulation;
  }

  .container {
    font: 13px/1.5 consolas, 'Microsoft Yahei', tahoma, sans-serif;
  }

  .label {
    color: #333;
  }

  .form .item {
    border-bottom: 1px solid #efefef;
    margin: 0;
    padding: 10px 0;
    height: 61px;
  }

  div, p {
    box-sizing: border-box;
  }

  .form .label {
    text-align: right;
    display: inline-block;
    padding-top: 10px;
  }

  .col-sm-1 {
    width: 8.33333333%;
  }

  .col-sm-1, .col-sm-10, .col-sm-11, .col-sm-12, .col-sm-2, .col-sm-3, .col-sm-4, .col-sm-5, .col-sm-6, .col-sm-7, .col-sm-8, .col-sm-9 {
    float: left;
    padding-left: 15px;
  }
  .my-nav-tabs>li {
    float: left;
    margin-bottom: -1px;
    position: relative;
}

  .my-nav-tabs>li>a {
      position: relative;
      display: block;
      padding: 10px 15px;
  }
  .my-nav-tabs > li > a {
    margin-right: 2px;
    border: 1px solid transparent;
    border-radius: 4px 4px 0 0;
    color: lightgrey;
  }

  .my-nav-tabs > li.active > a {
    margin-right: 2px;
    line-height: 1.42857143;
    border: 1px solid transparent;
    border-radius: 4px 4px 0 0;
    border-bottom-color: #1e87f0;
    color: black;
  }

  .uk-select:not([multiple]):not([size]) {
    -webkit-appearance: none;
    -moz-appearance: none;
    padding-right: 20px;
    background-image: url(data:image/svg+xml;charset=UTF-8,%3Csvg%20width%3D%2224%22%20height%3D%2216…ints%3D%2212%2013%209%208%2015%208%22%3E%3C%2Fpolygon%3E%0A%3C%2Fsvg%3E%0A);
    background-repeat: no-repeat;
    background-position: 100% 50%;
  }

  .uk-input, .uk-select:not([multiple]):not([size]) {
    height: 40px;
    vertical-align: middle;
    display: inline-block;
  }

  .uk-select:not([multiple]):not([size]) {
    -webkit-appearance: none;
    -moz-appearance: none;
    padding-left: 20px;
    background-image: url(data:image/svg+xml;charset=UTF-8,%3Csvg%20width%3D%2224%22%20height%3D%2216…ints%3D%2212%2013%209%208%2015%208%22%3E%3C%2Fpolygon%3E%0A%3C%2Fsvg%3E%0A);
    background-repeat: no-repeat;
    background-position: 0 50%;
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

  .uk-select {
    text-transform: none;
  }

  .uk-checkbox, .uk-input, .uk-radio, .uk-select, .uk-textarea {
    box-sizing: border-box;
    margin: 0;
    border-radius: 0;
    font: inherit;
  }

  a, area, button, input, label, select, summary, textarea {
    touch-action: manipulation;
  }

  a, area, button, input, label, select, summary, textarea {
    touch-action: manipulation;
  }

  select {
    border-radius: 0px;
    border-color: rgb(169, 169, 169);
  }

  select {
    -webkit-appearance: menulist;
    box-sizing: border-box;
    align-items: center;
    white-space: pre;
    -webkit-rtl-ordering: logical;
    color: black;
    background-color: white;
    cursor: default;
    border-width: 1px;
    border-style: solid;
    border-color: initial;
    border-image: initial;
  }

  select {
    border-radius: 5px;
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
