<template>
  <div style="left:250px;position: absolute">
    <mainheader :locate="locate" :right="right"></mainheader>
    <projectIndex v-if="locate=='0'"></projectIndex>
    <chooseModule v-else-if="locate=='1'" :mid="right"></chooseModule>
    <chooseApi v-else :aid="right"></chooseApi>
  </div>

</template>
<script>
  import maincontent from './maincontent.vue'
  import mainheader from './mainheader.vue'
  import projectIndex from './rightPage/index.vue'
  import chooseApi from './rightPage/chooseApi'
  import chooseModule from './rightPage/chooseModule'
  export default{
    name:'rightArea',
    components:{
      mainheader,
      maincontent,
      projectIndex,
      chooseApi,
      chooseModule
    },
    props:['locate','right']
  }
</script>
<style scoped></style>
