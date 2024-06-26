<!--
 * @Autor: Hongting Yuan
 * @Date: 2022-04-02 14:19:59
 * @LastEditors: Hongting Yuan
 * @LastEditTime: 2022-05-28 09:01:27
 * @Description: file content
 * @FilePath: \mdd\src\views\Introduction.vue
-->
<template>
  <div class="background">

    <div class="pd">
      <h1 class="title">{{title}}</h1>
      <p class="description">{{description1}}</p>
      <p class="description">{{description2}}</p>
      <el-row :gutter="20" style="margin-top: 200px;">
        <el-col :span="10">
          <div>
            <img src="../assets/image/introduction/sleep.jpeg" alt="sleep" style="width: 300px;margin-top: 53px;">
          </div>
        </el-col>
        <el-col :span="10">
          <div>
            <h2 class="what_title">
              {{what_title}}
            </h2>
            <p class="what_paragraph">{{what_passage_one}}</p>
            <p class="what_paragraph">{{what_passage_two}}</p>
            <p class="what_paragraph">{{what_passage_three}}</p>
          </div>
        </el-col>
      </el-row>
      <h2 class="why_title">
        {{why_title}}
      </h2>
      <p class="why_passage">{{why_passage}}</p>
      <img src="../assets/image/introduction/accuse.jpeg" alt="accuse"
        style="width: 400px;margin-left: 470px;margin-bottom: 20px;">

      <!-- <img src="../assets/image/introduction/" alt=""> -->
    </div>
  </div>
</template>
<script>
  export default {
    name: "Introduction",
    data () {
      return {
        title: '抑郁症简介',
        description1: '这世上除了糟糕的事情',
        description2: '还有许多美好在等着你',
        what_title: '什么是抑郁症',
        what_passage_one: '抑郁症是现在最常见的一种心理疾病，以连续且长期的心情低落为主要的临床特征，是现代人心理疾病最重要的类型。',
        what_passage_two: '临床可见，心情低落和现实过得不开心，情绪长时间地低落消沉，从一开始的闷闷不乐到最后的悲痛欲绝，自卑、痛苦、悲观、厌世，感觉活着每一天都是在绝望地折磨自己，消极逃避，最后甚至更有自杀倾向和行为。',
        what_passage_three: '患者患有躯体化症状,胸闷,气短。每天只想躺在床上,什么都不想动。有明显的焦虑感。更严重者会出现幻听、被害妄想症、多重人格等精神分裂症状。抑郁症每次发作,持续至少2周以上、一年,甚至数年,大多数病例有复发的倾向。',
        why_title: '抑郁症的原因',
        why_passage: '迄今，抑郁症的病因并不非常清楚，但可以肯定的是，生物、心理与社会环境诸多方面因素参与了抑郁症的发病过程。生物学因素主要涉及遗传、神经生化、神经内分泌、神经再生等方面；与抑郁症关系密切的心理学易患素质是病前性格特征，如抑郁气质。成年期遭遇应激性的生活事件，是导致出现具有临床意义的抑郁发作的重要触发条件。然而，以上这些因素并不是单独起作用的，强调遗传与环境或应激因素之间的交互作用、以及这种交互作用的出现时点在抑郁症发生过程中具有重要的影响。',
      }
    }
  }
</script>
<style scoped>
  .background {
    background: url("../assets/image/introduction/bg.jpg");
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

  .what_title {
    margin-left: 90px;
    margin-bottom: 35px;
  }

  .what_paragraph {
    margin: 0px 0 25px 90px;
    width: 400px;
    text-indent: 40px;
  }

  .why_title {
    margin-left: 50px;
    margin-top: 50px;
  }

  .why_passage {
    margin: 30px 50px;
    text-indent: 40px;
  }
</style>