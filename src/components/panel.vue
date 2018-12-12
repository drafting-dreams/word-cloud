<template>
    <div class="panel">
        <label for="file">Select file: </label>
        <select @change="getFile" id="file">
            <option :value="fileSource" selected disabled hidden>Choose here</option>
            <option value="a.txt">a-student</option>
            <option value="b.txt">b-student</option>
            <option value="c.txt">c-student</option>
        </select>
        <div v-show="loading" class="loader">
            <span>generating...</span>
        </div>
        <img :src="'/'+fileSource" alt="image lost">
    </div>
</template>

<script>
  import $ from 'jquery'

  export default {
    name: 'panel',
    data: function () {
      return {
        fileSource: '_test.jpg',
        loading: false,
      }
    },
    props: {
      prefix: String
    },
    methods: {
      getFile: function (e) {
        console.log(e.target.value)
        console.log(this.prefix)
        this.loading = true
        $.get('/api/wordCloud', {
          fileName: this.prefix + e.target.value,
        }).then(res => {
          this.fileSource = res
          console.log(res)
          console.log(Date.now())
          this.loading = false
        }).catch(err => {
          console.log(err)
          this.loading = false
        })
      },
    },
  }
</script>

<style>
    .panel {
        display: inline-block;
    }
</style>

