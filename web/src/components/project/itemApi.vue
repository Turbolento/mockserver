<template>
  <div>
    <div class="panel-body" :id="'aid'+aid">
      <a v-on:click="changeLocate()">{{aname}}</a>
    </div>
  </div>
</template>
<script>
  export default {
    name:'itemApi',
    props:['aid','aname'],
    methods:{
      changeLocate:function(){
        this.$emit("changeLocation",3,this.aid)
      }
    }
  }
</script>
<style scoped>
    .panel-body{
    text-align: left;
    padding:8px 8px 8px 30px;
    margin-left: -15px;
  }
  .panel-body:hover{
  background-color: #d1dbe5;
}
  .panel-body.active{
    background-color: #d1dbe5;
  }
</style>
