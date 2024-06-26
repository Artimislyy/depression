<!--
 * @Autor: Hongting Yuan
 * @Date: 2022-04-02 14:19:59
 * @LastEditors: Hongting Yuan
 * @LastEditTime: 2022-05-25 16:10:11
 * @Description: file content
 * @FilePath: \mdd\src\views\Home.vue
-->

<!--
 * @Autor: Hongting Yuan
 * @Date: 2022-04-25 19:39:43
 * @LastEditors: Hongting Yuan
 * @LastEditTime: 2022-04-25 20:26:23
 * @Description: file content
 * @FilePath: \mdd\src\components\Login.vue
-->
<template>
  <div>
    <el-container>
      <el-header>
        <img src="../../src/assets/image/logo.png" alt="logo"
          style=" width: 100px; float: left;margin-left: 20px;margin-top: 5px;" />
        <el-menu active-text-color="#7B8E69" :default-active="activeIndex" class="el-menu-demo" mode="horizontal"
          @select="handleSelect" router style="float: right;padding-right: 20px;">
          <el-submenu index="/mdd">
            <template slot="title" @click="init">抑郁症</template>
            <el-menu-item index="/Introduction" @click="init">抑郁症简介</el-menu-item>
            <el-menu-item index="/information" @click="init">抑郁症发病率</el-menu-item>
            <el-menu-item index="/Test" @click="change">抑郁症测试</el-menu-item>
            <el-menu-item index="/HistoryView">研判分析</el-menu-item>
          </el-submenu>
          <!-- <el-menu-item index="/Test" @click="change">抑郁症测试</el-menu-item> -->
          <el-menu-item index="/Other">其他情绪病</el-menu-item>
          <el-submenu index="/">
            <template slot="title" @click="init">休息室</template>
            <el-menu-item index="TreatMent" @click="init">抑郁症的治疗方法</el-menu-item>
            <el-menu-item index="Family" @click="init">如何与家人和朋友谈论抑郁症</el-menu-item>
            <el-menu-item index="Pressure" @click="init">压力与抑郁症的关系</el-menu-item>
          </el-submenu>
          <!-- <el-menu-item index="/RestRoom">休息室</el-menu-item> -->
        </el-menu>
      </el-header>
      <el-main style="background-color: #F3E9DF;">
        <router-view />
      </el-main>
      <el-footer style="text-align: center;vertical-align: middle;line-height: 60px;font-size: 13px;">
        Copyright@2022 袁红婷 张樱子 罗杨阳 <span style="font-size: 10px;">注：web端部分图片来自于百度网页公开图片</span>
      </el-footer>
    </el-container>
  </div>
</template>
<script>
  import axios from 'axios'
  export default {
    name: 'Home',
    data () {
      return {
        activeIndex: '1',
        id: this.GLOBAL.id
      };
    },
    created () {
      let router_path = this.$route.path
      // console.log(router_path)
      if (router_path != '/Introduction') {
        this.$router.replace({ path: '/Introduction' });
      }

    },
    methods: {
      handleSelect (key, keyPath) {
        this.activeIndex = keyPath[0]
      },
      change () {
        console.log(this.id)
        this.GLOBAL.id = 3
        this.GLOBAL.other_result_num = 0
        // var message = { 'username': 'lyy' }
        // axios.post('/name', message).then(function (result) {
        //   console.log(result)
        // }).catch(error => (console.log(error)))
        // console.log(this.GLOBAL.id)
      },
      init () {
        this.GLOBAL.id = 2
        this.GLOBAL.other_result_num = 0
      }
    }
  }
</script>

<style scoped>
  a {
    text-decoration: none;
  }

  .router-link-active {
    text-decoration: none;
  }
</style>