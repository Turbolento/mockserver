<script>
  export default {
    data: function () {
      return {
        responseTypes: []
      }
    },
    props: ['responseBodys'],
    methods: {
      removeResponseBody: function (num) {
        var child = document.getElementById("responseBody" + num);
        child.parentNode.removeChild(child);
        var arr = this.responseBodys
        for (var i = 0; i < arr.length; i++) {
          if (arr[i].id == num) {
            arr.splice(i, 1);
            break;
          }
        }
      },
      openJsonEdit: function (content,x) {
        $("#jsonEdit" + x).css("display", "block");
        $('#jsonEdit' + x + ' textarea').val(content)
      },
      formatJson: function (x) {
        var content = $("#jsonEdit"+x+" textarea").val()
        try{
          var t = JSON.stringify(JSON.parse(content), null, 4)
          $('#jsonEdit' + x + ' textarea').val(t)
          this.$message({"type": "success", "text": "json格式正确！"})
        }
        catch(err){
          this.$message({"type": "error", "text": "json格式有误！"})
          $('#jsonEdit' + x + ' textarea').val(content)
        }
      },
      saveJson:function(x){
        var content = $('#jsonEdit' + x + ' textarea').val()
        var t = this.format(content,true)
        for(var p in this.responseBodys ){
          if(this.responseBodys[p].id ==x){
            this.responseBodys[p].response = t
            break
          }
        }
      },
      format:function(txt,compress){
        var indentChar = '    ';
        try{var data=eval('('+txt+')');}
        catch(e){
          return txt
        };
        var draw=[],last=false,This=this,line=compress?'':'\n',nodeCount=0,maxDepth=0;

        var notify=function(name,value,isLast,indent/*缩进*/,formObj){
            nodeCount++;/*节点计数*/
            for (var i=0,tab='';i<indent;i++ )tab+=indentChar;/* 缩进HTML */
            tab=compress?'':tab;/*压缩模式忽略缩进*/
            maxDepth=++indent;/*缩进递增并记录*/
            if(value&&value.constructor==Array){/*处理数组*/
                draw.push(tab+(formObj?('"'+name+'":'):'')+'['+line);/*缩进'[' 然后换行*/
                for (var i=0;i<value.length;i++)
                    notify(i,value[i],i==value.length-1,indent,false);
                draw.push(tab+']'+(isLast?line:(','+line)));/*缩进']'换行,若非尾元素则添加逗号*/
            }else   if(value&&typeof value=='object'){/*处理对象*/
                    draw.push(tab+(formObj?('"'+name+'":'):'')+'{'+line);/*缩进'{' 然后换行*/
                    var len=0,i=0;
                    for(var key in value)len++;
                    for(var key in value)notify(key,value[key],++i==len,indent,true);
                    draw.push(tab+'}'+(isLast?line:(','+line)));/*缩进'}'换行,若非尾元素则添加逗号*/
                }else{
                        if(typeof value=='string')value='"'+value+'"';
                        draw.push(tab+(formObj?('"'+name+'":'):'')+value+(isLast?'':',')+line);
                };
        };
        var isLast=true,indent=0;
        notify('',data,isLast,indent,false);
        return draw.join('');
      }
    },
    mounted() {
      document.addEventListener("click", function (e) {
        if (e.target.className != "fa fa-edit" && e.target.className != "json-edit" && e.target.className != "btn btn-default btn-sm json-btn" &&e.target.className != "json-textarea") {
          $(".json-edit").each(function () {
            $(this).css("display", "none")
          })
        }
      })
      var x = null
      $.ajax({
        url: this.getBackendUrl() + "mockserverApi/listAllResponseTypes",
        async: false,
        success: function (ret) {
          x = ret
        }
      })
      if (x.status == 0) {
        this.responseTypes = x.data
      } else {
        this.$message({"type": "error", "text": x.msg})
      }
    }
  }
</script>

<template>
  <div class="responseBody-list" id="responseBodyTable">
    <div
      class="responseBody-item"
      v-for="responseBody in responseBodys"
      v-dragging="{ item: responseBody, list: responseBodys, group: 'responseBody' }"
      :key="responseBody.id" :id="'responseBody'+responseBody.id">
      <div data-pid="0" data-module-name="requestHeaders"
           class="placeholder-request-headers div-editing-table request-headers" data-sortable-id="19"
           aria-dropeffect="move">
        <div data-id="6gk969" class="div-table-line  div-editing-line" role="option" aria-grabbed="false">
          <div>
            <ul class="cb">
              <li class="col-sm-1"><i class="fa fa-remove" style="margin: 0 4px;cursor:pointer;"
                                      v-on:click="removeResponseBody(responseBody.id)"></i>
                <i class="fa fa-reorder" draggable="true" style="margin: 0 4px;cursor:move;"></i></li>
              <li class="col-sm-2 input">
                <input type="text" class="text name" v-model="responseBody.name" v-on:click.stop></li>
              <li class="col-sm-2">
                <select v-model="responseBody.type" class="uk-select"
                        style="position: absolute;top:0px;left:0px;height:38px;display: inline-block">
                  <option v-for="rt in responseTypes" :value="rt">{{rt}}</option>
                </select>
              </li>
              <li class="col-sm-1 input">
                <input type="text" class="text" v-model="responseBody.status">
              </li>
              <li class="col-sm-3 input response-content">
                <input :id="'respText'+responseBody.id" type="text" class="text" v-model="responseBody.response">
                <i class="fa fa-edit" v-on:click="openJsonEdit(responseBody.response,responseBody.id)"></i>
                <div class="json-edit" :id="'jsonEdit'+responseBody.id">
                  <textarea class="json-textarea" spellcheck="false">{{responseBody.response}}</textarea>
                  <br/>
                  <button class="btn btn-default btn-sm json-btn"
                          v-on:click="formatJson(responseBody.id)">格式化
                  </button>
                  <button class="btn btn-default btn-sm" v-on:click="saveJson(responseBody.id)">保&emsp;存</button>
                </div>
              </li>
              <li class="col-sm-3 input">
                <input type="text" class="text" v-model="responseBody.desc">
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<style scoped>
  .json-edit {
    width: 100%;
    padding: 10px;
    box-sizing: border-box;
    border: 1px solid rgba(0, 0, 0, .15);
    -webkit-box-shadow: 0 6px 12px rgba(0, 0, 0, .175);
    box-shadow: 0 6px 12px rgba(0, 0, 0, .175);
    background-color: #fff;
    top: 0px;
    position: absolute;
    z-index: 10;
    display: none;
  }

  .json-edit > textarea {
    word-break: break-all;
    resize: none;
    width: 100%;
    min-height: 150px;
    overflow-y: auto;
    border: none;
  }

  .response-content > i {
    font-style: normal;
    font-weight: normal;
    font-size: 18px;
    margin-right: 15px;
    top: 10px;
    right: -10px;
    position: absolute;
    z-index: 3;
    color: #b44421;

  }

  .response-content > i:hover {
    color: #3f56fa;
    cursor: pointer;
  }

  .response-content > input {
    padding-right: 30px;
  }

  li.input {
    padding: 0px !important;
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

  .div-table-header li {
    background-color: #fff;
    padding: 8px 10px;
    border-top: 1px solid #ccc !important;
  }

  li {
    list-style: none;
  }

  li {
    display: list-item;
    text-align: -webkit-match-parent;
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
    outline: none;
    position: relative;
    height: 38px;
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
    border: none;
    border-bottom: 1px solid #ccc;
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

  .nav-tabs > li > a {
    margin-right: 2px;
    line-height: 1.42857143;
    border: 1px solid transparent;
    border-radius: 4px 4px 0 0;
    color: lightgrey;
  }

  .nav-tabs > li.active > a {
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
    padding: 0 10px;
    background: #fff;
    color: #666;
    border: 1px solid #e5e5e5;
    border-right: none;
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
