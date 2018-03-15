<template>
  <transition name="fade">
    <div class="home">
      <p class="text">或者有人笑我故意向未练的孩子们的空想界中找求荒唐的乌托邦，以为逃避现实之所，但我也可笑他们的屈服于现实，忘却人类的本性。</p>
    </div>
  </transition>
</template>

<script type="text/ecmascript-6">

</script>

<style scoped>
  .home {
    display: flex;
    align-items:center;
    justify-content: center;
    width: 80%;
  }
  .text {
    font-family: 'Microsoft YaHei';
    font-size: 18px;
    line-height: 24px;
    color: rgba(255, 255, 255, 0.9);
  }
  .fade-enter-active, .fade-leave-active {
    transition: all 1s;
  }
  .fade-enter, .fade-leave-to {
    opacity: 0;
    transform: translateY(30px);
  }
</style>