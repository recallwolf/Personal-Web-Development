<template>
  <transition name="fade">
    <div class="state">
      <scroll>
        <timeline v-bind:timedata="timedata"></timeline>
        <div class="img-pos">
          <img class="pic" src="~common/image/city.png">
        </div>
      </scroll>
    </div>
  </transition>
</template>

<script  type="text/ecmascript-6">
  import Timeline from 'base/timeline/timeline'
  import Scroll from 'base/scroll/scroll'
  
  export default {
    data() {
      return {
        timedata: [{
          year: 1997,
          text: '这一年我出生了'
        },
        {
          year: 2002,
          text: '我离开了姥姥家 来到了长沙'
        },
        {
          year: 2012,
          text: '我重新认识了人与人之间的关系 思考了很久'
        },
        {
          year: 2015,
          text: '我去了郑州'
        },
        {
          year: 2018,
          text: "Now ? I don't know"
        }]
      }
    },
    components: {
      Timeline,
      Scroll
    }
  }
</script>

<style scoped>
  @media screen and (max-width: 1280px) {
    .img-pos {
      display: none;
    }
  }
  @media screen and (max-width: 450px) {  
    .state {
      top: 60px!important;
    }
  }
  .state {
    position: absolute;
    display: flex;
    top: 68px;    
    left: 5%;
  }
  .img-pos {
    float: left;
    position: absolute;
    top: 80px;
    left: 500px;
  }
  .pic {
    width: 593px; 
    height: 331px;
    opacity: 0.7;
  }
  .fade-enter-active, .fade-leave-active {
    transition: all 1s;
  }
  .fade-enter, .fade-leave-to {
    opacity: 0;
    transform: translateY(10px);
  }
</style>
