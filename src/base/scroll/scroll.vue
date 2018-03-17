<template>
  <div class="scroll">
    <slot></slot>
  </div>
</template>

<script type="text/ecmascript-6">

</script>

<style scoped>
  @media screen and (max-width: 830px) {
    .scroll {
      width: 540px;
      height: 230px;
      overflow: auto;
    }
  }
  @media screen and (max-width: 775px) {
    .scroll {
      width: 540px;
      height:500px;
      overflow: auto;
    }
  }
  @media screen and (max-width: 740px) {
    .scroll {
      width: 300px;
      height: 260px;
      overflow: auto;
    }
  }
  @media screen and (max-width: 600px) {
    .scroll {
      width: 540px;
      height:180px;
      overflow: auto;
    }
  }
  @media screen and (max-width: 450px) {
    .scroll {
      width: 300px;
      height: 100%;
      overflow: auto;
    }
  }
  @media screen and (max-width: 330px) {
    .scroll {
      width: 300px;
      height: 350px;
      overflow: auto;
    }
  }
  .scroll {
    padding-top: 5px;
  }
</style>
