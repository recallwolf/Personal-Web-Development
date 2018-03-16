<template>
  <div>
    <ul>
      <li v-for="(day, index) in timedata"  v-bind:key="index" class="setting">
        <h1 class="box">
          <h2 class="head">{{day.year}}</h2>
          <p class="text">{{day.text}}</p>
        </h1>
        <div class="line"></div>
      </li>
    </ul>
  </div>
</template>

<script type="text/ecmascript-6">
  export default {
    props: {
      timedata: {
        type: Array,
        default: []
      }
    }
  }
</script>

<style scoped>
  .setting {
    height: 100px;
  }
  .box {
    width: 18px;
    height: 18px;
    border-radius: 50%;
    background-color: rgba(0, 0, 0, 0.7);
    border: 2px solid rgba(149, 165, 166, 0.5);
    float: left;
  }
  .head {
    color: rgba(255, 255, 255, 0.8);
    font-size: 30px;
    padding-left: 32px;
    position: relative;
    bottom: 5px;
    float: left;
  }
  .text {
    color: rgba(255, 255, 255, 0.8);
    font-size: 16px;
    line-height: 20px;
    padding-left: 32px;
    width: 300px;
    position: relative;
    top: 30px;
    left: -62px;
  }
  .line {
    position: relative;
    top: 22px;
    left: 10px;
    width: 100px;
    height: 78px;
    border-left: 2px solid rgba(255, 255, 255, 0.5);
  }
  ul li:last-child div{
    display: none
  }
</style>
