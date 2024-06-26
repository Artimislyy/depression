<!--
 * @Autor: Hongting Yuan
 * @Date: 2022-04-02 14:19:59
 * @LastEditors: Hongting Yuan
 * @LastEditTime: 2022-05-04 18:07:28
 * @Description: file content
 * @FilePath: \mdd\src\views\Family.vue
-->
<template>
  <div class="background">
    <div class="pd">
      <h1 class="title">{{title}}</h1>
      <p class="description">{{description1}}</p>
      <p class="description">{{description2}}</p>
      <p class="description">{{description3}}</p>
      <h2 class="left_title">
        {{left_title}}
      </h2>
      <el-row :gutter="20">
        <el-col :span="12">
          <div style="width: 550px;">
            <p class="left_paragraph">{{left_paragraph1}}</p>
            <p class="left_paragraph">{{left_paragraph2}}</p>
            <p class="left_paragraph">{{left_paragraph3}}</p>
          </div>
        </el-col>
        <el-col :span="8">
          <div><img src="../assets//image/family/cloud.png" alt="cloud"
              style="width: 580px;margin-right: -300px;margin-top: -50px;">
          </div>
        </el-col>
      </el-row>

      <el-row :gutter="20">
        <el-col :span="8">
          <div>
            <img src="../assets/image/family/cake.png" alt="cake"
              style="width: 600px;margin-top: -50px;margin-left: -136px;">
          </div>
        </el-col>
        <el-col :span="12">
          <div style="width: 550px;padding-top: 50px;padding-left: 50px;">
            <p class="right_paragraph">{{right_paragraph1}}</p>
            <p class="right_paragraph">{{right_paragraph2}}</p>
          </div>
        </el-col>
      </el-row>
    </div>
  </div>
</template>
<script>
  export default {
    name: "Family",
    data () {
      return {
        title: '如何与家人朋友谈论抑郁症',
        description1: '当你的工作不顺心时，当你的生活不如意时，当你的心情不舒畅时，',
        description2: '就想想我们之间的感情吧。',
        description3: '你的家人、朋友永远支持你，陪伴你。',
        left_title: '敞开心扉聊一聊',
        left_paragraph1: '抑郁症是一种非常普遍的都市疾病，在如今压力大的生活中，平均每五个人当中，就有一个会在一生中受到不同程度的抑郁症困扰。缺乏家人的谅解会令病情恶化，把内心的感受表达出来可以加深家人对您的了解，而家人和朋友对您的体谅和鼓励，对治疗是十分重要的。',
        left_paragraph2: '告诉家人或朋友自己的病征例如烦躁、失落、忧虑、失眠和头痛等，希望家人能体谅和协助，从而加快康复的过程。',
        left_paragraph3: '告诉家人或朋友自己生病了，原因是脑部化学传递物质失去平衡所引致，并非像一般的误解，如智商低、神经错乱和头脑昏乱等。',
        right_paragraph1: '告诉家人或朋友自己正在接受药物治疗及/或认知行为治疗来改善脑部化学传递物的平衡，康复及预防复发的疗程需要半年至一年左右；而新一代的情绪调节剂是不会令人上瘾的，临床研究显示，七成患者经过治疗后都可以完全康复。',
        right_paragraph2: '告诉家人或朋友自己正在接受药物治疗及/告诉家人不需过份担心，因为经验丰富的医生和临床心理学家会为自己度身制定治疗方法以调节自己的人生价值观及处理抑郁症的病征。可以的话，建议家人一同约见有关的医生和临床心理学家。',
      }
    }
  }
</script>
<style scoped>
  .background {
    background: url("../assets/image/family/bg.jpg");
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
    padding: 0;
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

  .left_title {
    margin-top: 130px;
    margin-bottom: 35px;
    margin-left: 136px;
  }

  .left_paragraph {
    text-indent: 40px;
    margin-bottom: 25px;
    margin-left: 136px;
    margin-right: -136px;
  }

  .right_paragraph {
    text-indent: 40px;
    margin-bottom: 25px;
  }
</style>