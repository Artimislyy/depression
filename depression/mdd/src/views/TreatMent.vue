<!--
 * @Autor: Hongting Yuan
 * @Date: 2022-04-02 15:39:19
 * @LastEditors: Hongting Yuan
 * @LastEditTime: 2022-05-04 18:06:32
 * @Description: file content
 * @FilePath: \mdd\src\views\TreatMent.vue
-->
<template>
  <div class="background">
    <div class="pd">
      <h1 class="title">{{title}}</h1>
      <p class="description">{{description1}}</p>
      <p class="description">{{description2}}</p>
      <h2 class="improtant_title">
        {{improtant_title}}
      </h2>
      <p class="improtant_paragraph">
        {{improtant_paragraph}}
      </p>
      <el-row :gutter="20">
        <el-col :span="12">
          <div>
            <h2 class="method_title">
              {{method_title}}
            </h2>
            <h3 class="method_paragraph_title">
              {{method_paragraph_title1}}
            </h3>
            <p class="method_paragraph_content">
              {{method_paragraph_content1}}
            </p>
            <h3 class="method_paragraph_title">
              {{method_paragraph_title2}}
            </h3>
            <p class="method_paragraph_content">
              {{method_paragraph_content2}}
            </p>
            <h3 class="method_paragraph_title">
              {{method_paragraph_title3}}
            </h3>
            <p class="method_paragraph_content">
              {{method_paragraph_content3}}
            </p>
          </div>
        </el-col>
        <el-col :span="8">
          <div style="margin: 140px 0 0 40px;"><img src="../assets/image/restroom/umbrella.jpeg" alt="umbrella"></div>
        </el-col>
      </el-row>
      <el-row :gutter="20">
        <el-col :span="10">
          <div style="margin: 70px 0 0 36px;">
            <img src="../assets/image/restroom/man.jpeg" alt="man" style="width: 450px;">
          </div>
        </el-col>
        <el-col :span="10">
          <div>
            <h2 class="method_right_title">
              {{method_right_title}}
            </h2>
            <h3 class="method_paragraph_right_title">
              {{method_paragraph_right_title1}}
            </h3>
            <p class="method_paragraph_right_content">
              {{method_paragraph_right_content1}}
            </p>
            <h3 class="method_paragraph_right_title">
              {{method_paragraph_right_title2}}
            </h3>
            <p class="method_paragraph_right_content" style="margin-bottom: 20px;">
              {{method_paragraph_right_content2}}
            </p>
          </div>
        </el-col>
      </el-row>
    </div>
  </div>
</template>
<script>
  export default {
    name: "restRoom",
    data () {
      return {
        title: '抑郁症的治疗方法',
        description1: '认识各种抑郁症',
        description2: '及早寻求专业诊治',
        improtant_title: '抑郁症治疗的重要性',
        improtant_paragraph: '医学研究证明，抑郁症不单只是心理及环境因素所形成，而患者生理的变化，即脑部化学传递物质（包括血清素、脑肾上线素、谷氨酸、氨基丁酸及多巴胺等）失调也扮演着重要的角色，所以患者单靠意志力并不足以控制抑郁症。若没有适当的治疗，长期的情绪问题会对身体造成严重影响，例如引致高血压或令患有心脏病人士的病情恶化，亦会影响患者的工作及社交生活。假若你患上抑郁症，不必过份担忧，尽早请教你的临床心理学家或医生，从而得到适当的治疗。抑郁症是可以好转或康复的。',
        method_title: '抑郁症治疗的方法',
        method_paragraph_title1: '心理治疗：',
        method_paragraph_content1: '透过临床心理学家的治疗而作出一些情绪改善方法，其中包括有认知行为治疗、认知治疗、行为治疗、动眼治疗、支援性心理治疗、压力管理及家庭治疗等。',
        method_paragraph_title2: '药物治疗：',
        method_paragraph_content2: '可独立或结合心理治疗使用；新一代的情绪调节剂能令脑部血清素及其他化学传递物质回复平衡，不属于镇静剂药物，经过一段疗程后，大部份患者的病情会有进步。',
        method_paragraph_title3: '合并治疗：',
        method_paragraph_content3: '心理治疗与药物治疗有相辅相成的作用，因此你的临床心理学家或医生会根据你的病况采用不同的治疗组合。病人应该遵照及配合专业人士的建议，令治疗发挥到最大的效用。',
        method_right_title: '认知行为治疗',
        method_paragraph_right_title1: '什么是认知行为治疗(CBT)：',
        method_paragraph_right_content1: '认知行为治疗是一种有大量科学研究证明有效的心理治疗方法，临床心理学家会先与病人建立互信的关系，然后透过改变病人的思想谬误以及不能自控的问题行为，纾缓患者的困扰。',
        method_paragraph_right_title2: '认知行为治疗的原理：',
        method_paragraph_right_content2: '一个人的情绪和行为主要受其主观想法而非客观事实所影响。情绪抑郁症患者常常不能自控地以过度负面或钻牛角尖的想法和态度去临床心理学家会有系统地协助他们纠正自己的思想谬误，以改善负面的情绪、行为和生活模式。面对事情，以致其日常生活出了乱子。',
      }
    }
  }
</script>
<style scoped>
  .background {
    background: url("../assets/image/restroom/bg.jpg");
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

  .description {
    font-size: 18px;
    font-family: 'SimHei';
    line-height: 25px;
    padding: 5px 0;
    text-align: center;
  }

  .improtant_title {
    padding: 145px 0 35px 36px;
  }

  .improtant_paragraph {
    text-align: left;
    padding-left: 36px;
  }

  .method_title {
    padding: 80px 0 0 36px;
  }

  .method_paragraph_title {
    text-align: left;
    margin: 20px 0 10px 36px;
  }

  .method_paragraph_content {
    text-align: left;
    margin-left: 36px;
    width: 450px;
  }

  .method_right_title {
    margin-top: 30px;
    text-align: left;
    width: 450px;
    margin-left: 110px;

  }

  .method_paragraph_right_title {
    text-align: left;
    margin: 20px 0 10px 36px;
    width: 450px;
    margin-left: 110px;
  }

  .method_paragraph_right_content {
    text-align: left;
    width: 450px;
    margin-left: 110px;
  }
</style>