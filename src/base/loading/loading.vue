<template>
  <div class="loading">
    <span class="icon-spinner"></span>
  </div>
</template>

<script type="text/ecmascript-6">

</script>

<style scoped>
  .loading {
    position: absolute;
    bottom: 100px;
    color: rgba(0, 0, 0, 0.5);
    font-size: 30px;
    animation: rotate 0.5s linear infinite;
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

