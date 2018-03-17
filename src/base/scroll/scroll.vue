<template>
  <div class="scroll" ref="wrapper">
    <slot></slot>
  </div>
</template>

<script type="text/ecmascript-6">
  import BScroll from 'better-scroll'

  export default {
    props: {
      data: {
        type: String
      }
    },
    mounted() {
      this.changeWidth()
      this.$nextTick(() => {
        this._initScroll()
      })
    },
    methods: {
      _initScroll() {
        this.scroll = new BScroll(this.$refs.wrapper, {
          probeType: this.probeType,
          click: this.click,
          observeDOM: true,
          resizePolling: 60,
          scrollbar: true
        })
      },
      changeWidth() {
        if (this.data === 'state') {
          this.$refs.wrapper.style.width = 400 + 'px'
        }
        if (this.data === 'about') {
          let clientWidth = document.body.clientWidth
          console.log(clientWidth)
          if (clientWidth > 830) {
            this.$refs.wrapper.style.width = 620 + 'px'
          }
        }
      }
    }
  }
</script>

<style scoped>
  @media screen and (max-width: 830px) {
    .scroll {
      width: 540px;
      height: 230px;
      overflow: hidden;
    }
  }
  @media screen and (max-width: 775px) {
    .scroll {
      width: 540px;
      height:500px;
      overflow: hidden;
    }
  }
  @media screen and (max-width: 740px) {
    .scroll {
      width: 300px;
      height: 260px;
      overflow: hidden;
    }
  }
  @media screen and (max-width: 600px) {
    .scroll {
      width: 540px;
      height:180px;
      overflow: hidden;
    }
  }
  @media screen and (max-width: 450px) {
    .scroll {
      width: 300px;
      height: 100%;
      overflow: hidden;
    }
  }
  @media screen and (max-width: 330px) {
    .scroll {
      width: 300px;
      height: 350px;
      overflow: hidden;
    }
  }
  .scroll {
    padding-top: 5px;
  }
</style>
