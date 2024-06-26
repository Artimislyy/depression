<!--
 * @Autor: Hongting Yuan
 * @Date: 2022-04-02 15:39:00
 * @LastEditors: Hongting Yuan
 * @LastEditTime: 2022-05-25 10:12:04
 * @Description: file content
 * @FilePath: \mdd\src\views\Other.vue
-->
<template>
  <div class="background">
    <div class="pd">
      <h1 class="title">{{title}}</h1>
      <p class="description">{{description1}}</p>
      <p class="description">{{description2}}</p>
      <p class="summary">{{summary1}}</p>
      <p>{{summary2}}</p>
      <div style="padding: 0 40px 0 260px;">
        <a href="http://localhost:8080/#/test" @click="change(1)">
          <img src="../assets/image/other/zy.jpeg" alt="躁郁症" title="躁郁症"
            style="width: 210px; height: 250px; margin-top: -50px;">
        </a>
        <a href="http://localhost:8080/#/test" @click="change(2)">
          <img src="../assets/image/other/sj.jpeg" title="社交恐惧症" alt="社交恐惧症" style="width: 230px;margin:0 0 0 20px;">
        </a>
      </div>
      <div style="margin-top: -30px;">
        <a href="http://localhost:8080/#/test" @click="change(3)">
          <img src="../assets/image/other/jl.jpeg" title="焦虑症" alt="焦虑症" style="width: 220px;margin-left: -200px;"></a>
        <a href="http://localhost:8080/#/test" @click="change(4)">
          <img src="../assets/image/other/cs.jpeg" title="创伤后应激障碍" alt="创伤后应激障碍"
            style="width: 280px;margin-left: 20px;">
        </a>
      </div>
      <div style="margin-top: 10px;margin-left: 20px;">
        <a href="http://localhost:8080/#/test" @click="change(5)">
          <img src="../assets/image/other/qp.jpeg" title="强迫症" alt="强迫症" style="width: 210px;">
        </a>
        <a href="http://localhost:8080/#/test" @click="change(6)">
          <img src="../assets/image/other/jk.jpeg" title="惊恐症" alt="惊恐症" style="width: 290px; margin-left: 20px;">
        </a>
      </div>
      <h2 class="what_title">{{what_title}}</h2>
      <p class="what_paragraph">{{what_paragraph}}</p>
    </div>
  </div>
</template>
<script>
  export default {
    name: "other",
    data () {
      return {
        title: '其他情绪病',
        description1: '生活一定会把压轴的好运留到最后',
        description2: '才会让你经历那么糟糕的日子',
        summary1: '情绪病是一种情绪障碍，包括许多种不同的情绪不适感。',
        summary2: '其中抑郁症便是最常见的一种。',
        what_title: '什么是情绪病',
        what_paragraph: '情绪病是由于过度或短暂兴奋、抑郁、焦躁等情绪引起的情绪波动及精神状态不佳，是一种非常普遍的都市心理疾病。根据调查，许多情绪病患者并不知道自己患病或患哪一种情绪病，故未有及早寻求有效的专业协助。一个原因是，他们根本不明白如何辨识情绪病。另一原因是，情绪病可能引起身体上的不适，例如头痛、疲劳、心悸。因此，患者及其家人，往往以为只是身体出现毛病，可是身体检查的结果，大多是正常。这会延误患者接受有效治疗，令病况加剧，甚至出现并发症。'
      }
    },
    methods: {
      change (num) {
        this.GLOBAL.id = 2
        if (num == 1) {
          this.GLOBAL.OTHER = '躁郁症'
        } else if (num == 2) {
          this.GLOBAL.OTHER = '社交恐惧症'
        } else if (num == 3) {
          this.GLOBAL.OTHER = '焦虑症'
        } else if (num == 4) {
          this.GLOBAL.OTHER = '创伤后应激障碍'
        } else if (num == 5) {
          this.GLOBAL.OTHER = '强迫症'
        } else if (num == 6) {
          this.GLOBAL.OTHER = '惊恐症'
        }
      }
    }
  }
</script>
<style scoped>
  .background {
    background: url("../assets/image/other/bg.jpg");
    background-size: 100%;
    height: auto;
    /* height: 100%; */
    /* position: fixed; */
    width: 100%;
    overflow: hidden;
  }

  .title {
    padding: 190px 0 30px 0;
  }

  .pd {
    padding: 0 136px;
  }

  p {
    font-size: 18px;
    line-height: 22px;
  }

  .description {
    font-size: 18px;
    font-family: 'SimHei';
    line-height: 25px;
    padding: 5px 0;
    text-align: center;
  }

  .summary {
    margin-top: 250px;
    width: 280px;
  }

  .what_title {
    padding-top: 60px;
  }

  .what_paragraph {
    padding-top: 30px;
    text-indent: 40px;
    padding-bottom: 20px;
  }

  a {
    text-decoration: none;
    color: #ffffff;
  }

  .router-link-active {
    text-decoration: none;
  }
</style>