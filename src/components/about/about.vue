<template>
  <transition name="fade">
    <div class="container">
      <scroll v-bind:data="data">
        <div class="row">
          <div class="about">
            <h1 class="title">欢迎来到recallwolf的小站</h1>
            <p class="text">这是我的私人据点</p>
            <p class="text">这个网站是为了展示我的兴趣爱好，同时也是我多年来的愿望</p>
          </div>
          <div class="about-part">
            <h1 class="title">我喜欢编程</h1>
            <p class="text">写代码是一件很好玩的事</p>
            <p class="text">我现在在学习很多前端方面的内容，同时我也很想了解嵌入式和后端方面</p>
          </div>
          <div class="about-part">
            <h1 class="title">我希望</h1>
            <p class="text">丰子恺先生是我这一生最敬佩的人， 我想成为他那样的人， 我一直在努力</p>
            <p class="text">不乱于心，不困于情，不畏将来，不念过往。如此。安好</p>
            <p class="text">无愧于天，无愧于地，无怍于人，无惧于鬼。这样，人生</p>
          </div>
        </div>
        <div class="img-pos">
          <img width="416px" height="528px" src="~common/image/pic.jpg">
        </div>
      </scroll>
    </div>
  </transition>
</template>

<script type="text/ecmascript-6">
  import Scroll from 'base/scroll/scroll'

  export default {
    data() {
      return {
        data: 'about'
      }
    },
    components: {
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
    .title {
      font-size: 18px!important;
      line-height: 28px!important;
    }
    .text {
      font-size: 14px!important;
      line-height: 21px!important;
    }
  }
  .container {
    position: absolute;
    display: flex;
    top: 80px;    
    left: 5%;
  }
  .row {
    float: left;
  }
  .about {
    display: flex;
    flex-direction: column;
    padding-bottom: 32px;
  }
  .title {
    font-size: 23px;
    color: rgba(255, 255, 255, 0.9);
    line-height: 40px;
  }
  .text {
    font-size: 18px;
    color: rgba(255, 255, 255, 0.9);
    line-height: 26px;
  }
  .about-part {
    display: flex;
    flex-direction: column;
    padding-bottom: 32px;
  }
  .img-pos {
    float: left;
    position: absolute;
    left: 680px;
  }
  .fade-enter-active, .fade-leave-active {
    transition: all 1s;
  }
  .fade-enter, .fade-leave-to {
    opacity: 0;
    transform: translateY(10px);
  }
</style>