<script>
  export default {
    props: ['requestBodys','responseBodys'],
    methods: {
      removeRequestBody: function (num) {
        var child = document.getElementById("requestBody" + num);
        child.parentNode.removeChild(child);
        var arr = this.requestBodys
        for (var i = 0; i < arr.length; i++) {
          if (arr[i].id == num) {
            arr.splice(i, 1);
            break;
          }
        }
      }
    }
  }
</script>

<template>
  <div class="requestBody-list" id="requestBodyTable">
    <div
      class="requestBody-item"
      v-for="requestBody in requestBodys"
      v-dragging="{ item: requestBody, list: requestBodys, group: 'requestBody' }"
      :key="requestBody.id" :id="'requestBody'+requestBody.id">
                  <div data-pid="0" data-module-name="requestBodys"
                       class="placeholder-request-bodys div-editing-table request-bodys" data-sortable-id="19"
                       aria-dropeffect="move">
                    <div data-id="6gk969" class="div-table-line  div-editing-line" role="option" aria-grabbed="false">
                      <div>
                        <ul class="cb">
                          <li class="col-sm-1"><i class="fa fa-remove" style="margin: 0 4px;cursor:pointer;"
                                                  v-on:click="removeRequestBody(requestBody.id)"></i>
                            <i class="fa fa-reorder" draggable="true" style="margin: 0 4px;cursor:move;"></i></li>
                          <li class="col-sm-1">
                            <select class="uk-select"
                                    style="position: absolute;top:0px;left:0px;height:38px;display: inline-block">
                              <option value="json" selected>json</option>
                            </select>
                          </li>
                          <li class="col-sm-2 input">
                            <input type="text" class="text name" v-model="requestBody.name"></li>
                          <li class="col-sm-2">
                            <select class="uk-select"
                                    style="position: absolute;top:0px;left:0px;height:38px;display: inline-block" v-model="requestBody.match">
                              <option value="0">等于</option>
                              <option value="1">包含</option>
                              <option value="2">大于</option>
                              <option value="3">小于</option>
                              <option value="4">开始于</option>
                              <option value="5">结束于</option>
                              <option value="6">任意值</option>
                            </select>
                          </li>
                          <li class="col-sm-3 input"><input type="text" class="text" v-model="requestBody.value"></li>
                          <li class="col-sm-3 input">
                            <select class="uk-select" :style="{'color':requestBody.response?'':'red'}"
                                    style="position: absolute;top:0px;left:0px;height:38px;display: inline-block" v-model="requestBody.response">
                              <option value="">请选择(响应数据为空则先添加)</option>
                              <option v-for="responseBody in responseBodys" :value="responseBody.name">{{responseBody.name}}</option>
                            </select>
                          </li>
                        </ul>
                      </div>
                    </div
                    >
                  </div>
    </div>
  </div>
</template>
<style scoped>
  option{
    color:#666;
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
