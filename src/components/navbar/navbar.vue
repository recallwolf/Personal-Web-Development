<template>
  <div class="nav">
    <div class="nav-display">
      <ul>
        <li class="nav-img">
          <img class="pic" src="~common/image/avatar.jpg">
        </li>
        <li class="nav-text"><router-link class="navto" to="/home">首页</router-link></li>
        <li class="nav-text"><router-link class="navto" to="/state">状态</router-link></li>
        <li class="nav-text"><a class="navto" href="/blog">博客</a></li>
        <li class="nav-text"><router-link class="navto" to="/about">关于</router-link></li>
      </ul>
    </div>
    <div class="btn-display">
      <span class="icon-menu iconM" @click="showMenu"></span>
    </div>
    <div class="nav-right">
      <ul>
        <li class="nav-text" @mouseover="mouseover" @mouseout="mouseout">{{location}}</li>
        <a href="https://github.com/recallwolf">
          <li class="icon-setting">
            <span class="icon-github"></span>
          </li>
        </a>
      </ul>
    </div>
  </div>
</template>

<script type="text/ecmascript-6">
  export default {
    props: {
      location: {
        type: String,
        default: ''
      }
    },
    methods: {
      mouseover() {
        this.$emit('on')
      },
      mouseout() {
        this.$emit('off')
      },
      showMenu() {
        this.$emit('menu')
      }
    }
  }
</script>

<style scoped>
  @media screen and (max-width: 796px) {
    .nav-display {
      display: none;
    }
    .btn-display {
      display: block!important;
      padding-top: 12px;
      padding-right: 25px;
      padding-left: 20px;
    }
  }
  .nav {
    display: flex;
    position: fixed;
    width: 100%;
    height: 44px;
    top: 0;
    left: 0;
    background-color: rgba(0, 0, 0, 0.5);
  }
  .btn-display {
    display: none;
    padding-top: 12px;
    padding-right: 25px;
    padding-left: 20px;
  }
  .pic {
    width: 36px;
    height: 36px;
    border-radius: 50%;
  }
  .pic:hover {
    animation: rotate 4s infinite;
  }
  .iconM {
    color: rgba(255, 255, 255, 0.7);
    font-size: 22px;
  }
  .nav-img {
    float: left;
    padding-right: 25px;
    padding-left: 20px;
    padding-top: 4px;
  }
  .nav-text {
    float: left;
    padding-right: 32px;
    padding-top: 8px;
    color: rgba(255, 255, 255, 0.7);
    font-size: 14px;
    font-weight: 550;
    line-height: 28px;
  }
  .nav-right {
    position: absolute;
    right: 32px;
  }
  .icon-setting {
    float: left;
    color: rgb(255, 255, 255);
    font-size: 24px;
    padding-top: 10px;
  }
  .navto {
    color: rgba(255, 255, 255, 0.7);
    text-decoration: none;
  }
  .active{
    padding-bottom: 7px;
    color: rgb(255, 255, 255);
    border-bottom-style: solid;
    border-bottom-width: 1px;
    border-bottom-color: rgb(240,20,20);
  }
  @keyframes rotate {
    0% {
      transform: rotate(0);
    }
    100% {
      transform: rotate(360deg);
    }
  }
</style>

