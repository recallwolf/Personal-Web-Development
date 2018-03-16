<template>
  <div class="button">
    <ul>
      <li class="button-icon" @click="play" v-show="!isPlay"><span class="icon-play icon"></span></li>
      <li class="button-icon" @click="pause" v-show="isPlay"><span class="icon-pause icon"></span></li>
      <li class="button-icon" @click="enlarge" v-show="!isEnlarge"><span class="icon-enlarge icon"></span></li>
      <li class="button-icon" @click="shrink" v-show="isEnlarge"><span class="icon-shrink icon"></span></li>

      <a href="https://weibo.com/1634414781/profile?rightmod=1&wvr=6&mod=personinfo">
        <li class="button-setting">
          <span class="icon-sina-weibo icon"></span>
        </li>
      </a>
      <a href="http://steamcommunity.com/id/RecallWolf">
        <li class="button-setting">
          <span class="icon-steam icon"></span>
        </li>
      </a>
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
        src: "http://m10.music.126.net/20180315175502/6bc72b956d08367b52f23798c07a6b26/ymusic/58a4/f4dc/85cf/f8851ca2d1241ca26f4f12f7d976cd66.mp3"
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
  @media screen and (max-width: 1024px) {
    .button-icon {
      display: none;
    }
  }
  .button {
    position: absolute;
    right: 10px;
    bottom: 22px;
  }
  .button-icon {
    float: left;
    margin-right: 18px;
    font-size: 24px;
    color: rgba(255, 255, 255, 0.9);
  }
  .button-setting {
    float: left;
    margin-right: 18px;
    font-size: 24px;
    color: rgba(255, 255, 255, 0.9);
  }
</style>
