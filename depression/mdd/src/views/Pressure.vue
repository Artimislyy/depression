<!--
 * @Autor: Hongting Yuan
 * @Date: 2022-04-02 14:19:59
 * @LastEditors: Hongting Yuan
 * @LastEditTime: 2022-05-04 18:07:55
 * @Description: file content
 * @FilePath: \mdd\src\views\Pressure.vue
-->
<template>
  <div class="background">
    <div class="pd">
      <h1 class="title">{{title}}</h1>
      <p class="description">{{description1}}</p>
      <p class="description">{{description2}}</p>
      <h2 class="middle_title">{{middle_title}}</h2>
      <p class="middle_paragraph">{{middle_paragraph1}}</p>
      <p class="middle_paragraph">{{middle_paragraph2}}</p>
      <p class="middle_paragraph">{{middle_paragraph3}}</p>
      <el-row :gutter="20">
        <el-col :span="8">
          <div>
            <img src="../assets/image/pressure/girl.jpg" alt="girl" style="width: 380px;margin-top: 150px;">
          </div>
        </el-col>
        <el-col :span="12">
          <div style="margin-top: 150px;margin-left: 100px;width: 510px;margin-bottom: 20px;">
            <h2 class="right_title">{{right_title}}</h2>
            <p style="margin-top: 30px;">{{right_paragraph1}}</p>
            <p class="right_paragraph">{{right_paragraph2}}</p>
            <p class="right_paragraph">{{right_paragraph3}}</p>
            <p class="right_paragraph">{{right_paragraph4}}</p>
            <p class="right_paragraph">{{right_paragraph5}}</p>
          </div>
        </el-col>
      </el-row>
    </div>
  </div>
</template>
<script>
  export default {
    name: "Pressure",
    data () {
      return {
        title: '压力与抑郁症的关系',
        description1: '过好每一天，并且把每一天都当成一辈子过',
        description2: '那么，你就找到了幸福生活的金钥匙',
        middle_title: '压力抑郁症三重奏',
        middle_paragraph1: '持续而不能应付的压力可能诱发抑郁症',
        middle_paragraph2: '没有遇上客观压力事件的人也会患上抑郁症',
        middle_paragraph3: '受抑郁症困扰的人会在主观上觉得自己无法应付一般外来压力',
        right_title: '是压力太大还是抑郁',
        right_paragraph1: '其实，压力反应跟抑郁症的症状很相似。那应到底该怎样分辨，是属于压力反应，还是已经患上了抑郁症呢？ 简单来说，请留意三方面：',
        right_paragraph2: '征状的持续性一般而言，压力反应持续的时间较短，一般不超过四个星期。若征状已持续四星期或以上，便要多加注意了。',
        right_paragraph3: '征状造成的困扰如果曾用有效的减压方法，但征状依然持续出现，并令你感到困扰，这情况可能属于抑郁症的症状。',
        right_paragraph4: '严重影响日常生活中的重要范畴如工作 / 学业、社交、家庭关系或处理家务的能力等。',
        right_paragraph5: '总而言之，如果征状长时间持续，并影响到了生活，便可能患上抑郁症。需要尽快咨询专业人士，进行调整和治疗。',
      }
    }
  }
</script>
<style scoped>
  .background {
    background: url("../assets/image/pressure/bg.jpg");
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

  .middle_title {
    margin-top: 260px;
  }

  .middle_paragraph {
    margin-top: 30px;
  }

  .right_paragraph {
    margin-top: 30px;
    text-indent: 40px;
  }
</style>