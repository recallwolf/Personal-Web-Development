<template>
  <div class="button">
    <ul>
      <li class="button-setting" @click="play" v-show="!isPlay"><span class="icon-play icon"></span></li>
      <li class="button-setting" @click="pause" v-show="isPlay"><span class="icon-pause icon"></span></li>
      <li class="button-setting" @click="enlarge" v-show="!isEnlarge"><span class="icon-enlarge icon"></span></li>
      <li class="button-setting" @click="shrink" v-show="isEnlarge"><span class="icon-shrink icon"></span></li>
    </ul>
    <audio ref="audio" :src="src"></audio>
  </div>
</template>

<script type="text/ecmascript-6">
  export default {
    data() {
      return {
        isEnlarge: false,
        isPlay: false,
        src: "http://m10.music.126.net/20180310152454/c1ab6aa3793cd26d23d48cd1ab3c4aa7/ymusic/7288/be3a/8b70/803f8908a232833b84ff8f854e6b5eca.mp3"
      }
    },
    methods: {
      enlarge() {
       this.requestFullScreen()
       this.isEnlarge = true
      },
      requestFullScreen(element) {
        if (!this.isEnlarge) {
          let el = document.querySelector(element) || document.documentElement
          if (el.requestFullscreen) {
            el.requestFullscreen()
          }
          else if (el.mozRequestFullScreen) {
            el.mozRequestFullScreen()
          }
          else if (el.webkitRequestFullScreen) {
            el.webkitRequestFullScreen()
          }
        }
      },
      shrink() {
        this.exitFullscreen()
        this.isEnlarge = false
      },
      exitFullscreen() {
        if (this.isEnlarge) {
          if (document.exitFullscreen) {
            document.exitFullscreen();
          }
          else if (document.mozCancelFullScreen) {
            document.mozCancelFullScreen();
          }
          else if (document.webkitCancelFullScreen) {
            document.webkitCancelFullScreen();
          }
        }
      },
      play() {
        this.isPlay = true
        if (this.isPlay) {
          this.$refs.audio.play()
        }
      },
      pause() {
        this.isPlay = false
        if (!this.isPlay) {
          this.$refs.audio.pause()
        }
      }
    }
  }
</script>

<style scoped>
  @media screen and (max-width: 796px) {
    .button-setting {
      display: none
    }
  }
  .button {
    position: absolute;
    right: 10px;
    bottom: 22px;
  }
  .button-setting {
    float: left;
    padding-right: 18px;
    font-size: 24px;
    color: rgba(255, 255, 255, 0.9);
  }
</style>
