<template>
  <div class="wrapper" ref="wrapper">
    <div class="inner-wrapper">
      <navbar :location="location" @on="on" @off="off" @menu="menu"></navbar>
      <keep-alive><router-view/></keep-alive>
      <control></control>
      <loading v-show="bgUrl === '' || location === '' "></loading>
      <transition name="fade">
        <div class="weather" v-show="showWeather"  @mouseover="on" @mouseout="off">
          <div class="title">
            <span class="icon-cloud cloud"></span>
            <span class="today">{{todayWeather.date}}</span>
          </div>
          <div class="detail">
            <ul>
              <li class="today-text">{{todayWeather.state}}</li>
              <li class="today-text">{{todayWeather.min}} ℃ ~ {{todayWeather.max}} ℃</li>
              <li class="today-text">{{todayWeather.wind_dir}}</li>
              <li class="today-text">风力：{{todayWeather.wind_sc}}级</li>
            </ul>
          </div>
          <div class="extra">
            <ul>
              <li class="extra-text">
                <span class="extra-list">明天</span>
                <span class="extra-list">{{secondWeather.state}}</span>
                <span class="extra-list">{{secondWeather.min}} ℃ ~ {{secondWeather.max}} ℃</span>
              </li>
              <li class="extra-text">
                <span class="extra-list">后天</span>
                <span class="extra-list">{{secondWeather.state}}</span>
                <span class="extra-list">{{secondWeather.min}} ℃ ~ {{secondWeather.max}} ℃</span>
              </li>
            </ul>
          </div>
        </div>
      </transition>
    </div>
    <transition name="display">
      <div class="outer-wrapper" v-show="showMenu" @click="menu">
        <ul>
          <li class="outerNav-text"><router-link class="navto" to="/home">首页</router-link></li>
          <li class="outerNav-text"><router-link class="navto" to="/state">状态</router-link></li>
          <li class="outerNav-text"><router-link class="navto" to="/blog">博客</router-link></li>
          <li class="outerNav-text"><router-link class="navto" to="/about">关于</router-link></li>
        </ul>
      </div>
    </transition>
  </div>
</template>

<script type="text/ecmascript-6">
  import Navbar from 'components/navbar/navbar'
  import Control from 'base/control/control'
  import Loading from 'base/loading/loading'
  import {getBgImage, getWeather, getIp} from 'api/api'

  export default {
    data() {
      return {
        bgUrl: '',
        location: '',
        todayWeather: {},
        secondWeather: {},
        thirdWeather: {},
        showWeather: false,
        showMenu: false

      }
    },
    created() {
      this._getBgImage()
      this._getWeather()
    },
    methods: {
      _getBgImage() {
        getBgImage().then((res) => {
          if (res.status.code === 200) {
            this.bgUrl = res.data.url
            this.$refs.wrapper.style.backgroundImage = `url(${this.bgUrl})`
          }
        })
      },
      _getWeather() {
        getWeather().then((weather) => {
          this.location = weather.HeWeather6[0].basic.location
          
          let todayData = [
            weather.HeWeather6[0].daily_forecast[0].date,
            weather.HeWeather6[0].daily_forecast[0].cond_txt_d,
            weather.HeWeather6[0].daily_forecast[0].tmp_max,
            weather.HeWeather6[0].daily_forecast[0].tmp_min,
            weather.HeWeather6[0].daily_forecast[0].wind_dir,
            weather.HeWeather6[0].daily_forecast[0].wind_sc
          ]
          let SecondData = [
            weather.HeWeather6[0].daily_forecast[1].cond_txt_d,
            weather.HeWeather6[0].daily_forecast[1].tmp_max,
            weather.HeWeather6[0].daily_forecast[1].tmp_min
          ]
          let thirdData = [
            weather.HeWeather6[0].daily_forecast[2].cond_txt_d,
            weather.HeWeather6[0].daily_forecast[2].tmp_max,
            weather.HeWeather6[0].daily_forecast[2].tmp_min
          ] 

          this.addListener(this.todayWeather, ['date', 'state', 'max', 'min', 'wind_dir', 'wind_sc'], todayData)
          this.addListener(this.secondWeather, ['state', 'max', 'min'], SecondData)
          this.addListener(this.thirdWeather, ['state', 'max', 'min'], thirdData)
        })
      },
      addListener(prop, child, data) {
        for (let i = 0; i < child.length; i++) {
          if (!child[i]) {
            return
          }
          else {
            this.$set(prop, child[i], data[i])
          }
        }
      },
      on() {
        this.showWeather = true
      },
      off() {
        this.showWeather = false
      },
      menu() {
        this.showMenu = !this.showMenu
      }
    },
    components: {
      Navbar,
      Control,
      Loading
    }
  }
</script>

<style scoped>
  .wrapper {
    position: absolute;
    height: 100%;
    width: 100%;
    background-color: black;
    background-image: url(https://bing.ioliu.cn/v1?w=1920&h=1080&d=1);
    background-position: top;
		background-attachment: fixed;
		background-repeat: no-repeat;
		background-size: cover;
  }
  .inner-wrapper {
    display: flex;
    align-items:center;
    justify-content: center;
    position: absolute;
    height: 100%;
    width: 100%;
    background-color: rgba(0, 0, 0, 0.7);
  }
  .weather {
    width: 210px;
    height: 230px;
    background-color: rgba(0, 0, 0, 0.3);
    position: absolute;
    right: 90px;
    top: 44px;
    padding: 20px;
    z-index: 3;
  }
  .title {
    display: inline-block;
    height: 66px;
  }
  .cloud {
    padding-right: 32px;
    vertical-align: middle;
    color: rgba(255, 255, 255, 0.8);
    font-size: 60px;
  }
  .today {
    vertical-align: middle;
    color: rgba(255, 255, 255, 0.8);
    font-size: 14px;
  }
  .today-text {
    padding-top: 4px;
    color: rgba(255, 255, 255, 0.8);
    font-size: 10px;
    vertical-align: middle;
    line-height: 20px;
  }
  .extra-text {
    padding-top: 18px;
    color: rgba(255, 255, 255, 0.8);
    font-size: 14px;
  }
  .extra-list {
    padding-right: 8px;
  }
  .outer-wrapper {
    position: absolute;
    display: flex;
    align-items:center;
    justify-content: center;
    height: 100%;
    width: 100%;
    background-color: rgba(0, 0, 0, 0.8);
  }
  .outerNav-text {
    height: 70px;
    color: rgba(255, 255, 255, 0.7);
    font-size: 14px;
    font-weight: 550;
    line-height: 28px;
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
  .fade-enter-active, .fade-leave-active {
    transition: all 0.7s;
  }
  .fade-enter, .fade-leave-to {
    opacity: 0;
    transform: translateY(40px);
  }
  .display-enter-active, .display-leave-active {
    transition: all 0.5s;
  }
  .display-enter, .display-leave-to {
    opacity: 0;
  }
</style>


