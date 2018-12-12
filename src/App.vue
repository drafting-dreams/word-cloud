<template>
    <div id="app">
        <h1 class="title">华中师范大学学生大数据中心</h1>
        <h2>词云</h2>
        <div class="panelContainer">
            <panel prefix="A"/>
            <panel prefix="B"/>
        </div>
    </div>
</template>

<script>
  import panel from '@/components/panel.vue'

  export default {
    name: 'app',
    components: {
      panel
    }
  }
</script>

<style>
    @keyframes blink {
        0% {
            opacity: .2;
        }
        20% {
            opacity: 1;
        }
        100% {
            opacity: .2;
        }
    }

    #app {
        font-family: 'Avenir', Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
    }

    img {
        display: block;
        max-width: 40vw;
        max-height: 40vh;
        vertical-align: middle;
        margin: auto;
    }

    .loader {
        display: inline-block;
        margin-left: 15px;
    }

    .loader span{
       animation-name: blink;
        animation-duration: 1.4s;
        animation-iteration-count: infinite;
        animation-fill-mode: both;
    }

    .title {
        text-align: left;
        padding-left: 40px;
    }

    .panelContainer {
        display: flex;
        justify-content: space-evenly;
    }

</style>
