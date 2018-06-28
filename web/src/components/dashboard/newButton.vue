<template>
<div class="container">
			 <div class="new-project-btn-holder btn" title="新增" id="modal-230103" href="#modal-container-230103" role="button" data-toggle="modal"><b>+</b></div>

			<div class="modal fade" id="modal-container-230103" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
				<div class="modal-dialog">
					<div class="modal-content">
						<div class="modal-header">
							 <button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>
							<h3 class="modal-title" id="myModalLabel">
								创建项目
							</h3>
						</div>
						<div class="modal-body">
							<form class="uk-form-stacked">
                <div class="uk-margin">
                  <label for="form-stacked-text" class="uk-form-label">项目名称</label>
                  <div class="uk-form-controls"><input autofocus="autofocus" id="form-stacked-text" type="text" placeholder="请输入项目名称" maxlength="50" class="uk-input">
                  </div>
                </div>
                <div class="uk-margin">
                  <label for="form-stacked-select" class="uk-form-label">项目描述</label>
                  <div class="uk-form-controls"><textarea id="form-stacked-select" rows="5" placeholder="请输入项目描述" maxlength="300" class="uk-textarea"></textarea></div></div>
                <div uk-grid="" class="uk-margin uk-grid-small uk-child-width-auto uk-grid">
                  <label class="uk-first-column">
                    <input type="radio" value="PUBLIC" name="permission" checked="checked" class="uk-radio"> 公开项目
                  </label>
                  <label><input type="radio" value="PRIVATE" name="permission" class="uk-radio" disabled>
                            私有项目</label>
                </div>
              </form>
						</div>
						<div class="modal-footer">
							 <button type="button" class="btn btn-default" data-dismiss="modal">取消</button> <button type="button" class="btn btn-primary" v-on:click="newProject()">创建</button>
						</div>
					</div>
				</div>
			</div>

</div>
</template>
<script>
  export default {
    name:'newButton',
    methods:{
      newProject:function(){
        var pjname = document.getElementById('form-stacked-text').value
        var pjdesc = document.getElementById('form-stacked-select').value
        var ret = null
        var onconnect = false
        $.ajax({
          url: this.getBackendUrl() + "mockserverApi/newProject",
          type: "POST",
          cache: false,
          async: false,
          data: {"pjname": pjname, "pjdesc": pjdesc, "_xsrf": this.getCookie("_xsrf")},
          success: function (x) {
            ret = x
          },
          error: function () {
            onconnect = true
          }
        })
        if (onconnect) {
          this.$message({"type": "error", "text": "新增失败，服务器错误！"})
        } else if (ret.status == 0) {
          this.$message({"type": "success", "text": "新增成功！"})
          var frontendurl = this.getFrontendUrl()
          setTimeout(function(){window.location.href = frontendurl+'project?pid='+ret.data},1500)
        } else {
          this.$message({"type": "error", "text": ret.msg})
        }
      }
    }
  }
</script>
<style scoped>
  .container{
    width:100%;
    left:0px;
    position: absolute;
  }
.new-project-btn-holder {
    text-align: center;
    width: 60px;
    height: 60px;
    line-height: 45px;
    border-radius: 100%;
    color: #fff;
    background-color: #d23f31;
    font-size: 40px;
    display: inline-block;
    cursor: pointer;
}
.new-project-btn-holder:hover{
    background-color: #d25541;
  }
.modal{
  margin-top:120px;
}
.modal-title,.modal-body{
  text-align: left;
}
  .uk-modal-body>:last-child, .uk-modal-footer>:last-child, .uk-modal-header>:last-child {
    margin-bottom: 0;
}
  .uk-margin {
    margin-bottom: 20px;
}
  .uk-form-stacked .uk-form-label {
    display: block;
    margin-bottom: 5px;
}
  .uk-form-label {
    color: #333;
    font-size: .875rem;
}
  a, area, button, input, label, select, summary, textarea {
    touch-action: manipulation;
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
.uk-input, .uk-select:not([multiple]):not([size]) {
    height: 40px;
    vertical-align: middle;
    display: inline-block;
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
</style>
