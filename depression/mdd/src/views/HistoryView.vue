<!--
 * @Autor: Hongting Yuan
 * @Date: 2022-04-25 19:16:54
 * @LastEditors: Hongting Yuan
 * @LastEditTime: 2022-05-28 09:34:06
 * @Description: file content
 * @FilePath: \mdd\src\views\HistoryView.vue
-->
<template>
  <div class="background">
    <div class="pd">
      <img src="../assets/image/history/right.png" alt="" style="width: 160px;float: right;margin-right: -90px;">
      <img src="../assets/image/history/left.jpeg" alt=""
        style="width: 330px;float: left;margin-left: -90px;margin-top: 120px;">
      <!-- width: 350px;height: 340px; float: right;margin-left: -500px;margin-top: 40px; -->
      <h1 class="title">{{title}}</h1>
      <div style="margin-top: 15px;"></div>
      <p class="description">{{description1}}</p>
      <p class="description">{{description2}}</p>
      <p class="description">{{description3}}</p>
      <div style="margin-top: 150px;"></div>
      <!-- 一周登录详情 -->
      <echarts v-if="ifEcharts==1" :chart-data="Data3" autoresize :style="meStyle3" />
      <div v-if="ifEcharts==0" style="height: 400px;line-height: 400px;align-content: center;font-size: 50px;">暂无数据
      </div>
      <div style="margin-top: 80px;"></div>

      <h3 style="padding-top: 40px;text-align: left;margin: 5px;">{{title1}}</h3>
      <ul v-for="(item,i) in symptoms" style="text-align: left; padding-left: 50px;margin: 3px;">
        <li>{{ item }}</li>
      </ul>
      <h3 style="text-align: left;margin: 5px;">{{title2}}</h3>
      <ul v-for="(item,i) in solves" style="text-align: left; padding-left: 50px;margin: 3px;">
        <li>{{ item }}</li>
      </ul>
      <!-- <div style=" margin-top: 30px;width: 60%;float: left;text-align: left;">{{analyse}}
    </div> -->
      <!-- <img src="../assets/image/introduction/" alt=""> -->
    </div>
  </div>
</template>
<script>
  import axios from 'axios'

  import echarts from '../components/MEcharts/echarts.vue'
  export default {
    components: {
      echarts
    },
    name: "HistoryView",
    data () {
      return {
        ifEcharts: 0,
        analyse: '抑郁症是一种非常普遍的都市疾病，在如今压力大的生活中，平均每五个人当中，就有一个会在一生中受到不同程度的抑郁症困扰。缺乏家人的谅解会令病情恶化，把内心的感受表达出来可以加深家人对您的了解，而家人和朋友对您的体谅和鼓励，对治疗是十分重要的。抑郁症是一种非常普遍的都市疾病，在如今压力大的生活中，平均每五个人当中，就有一个会在一生中受到不同程度的抑郁症困扰。缺乏家人的谅解会令病情恶化，把内心的感受表达出来可以加深家人对您的了解，而家人和朋友对您的体谅和鼓励，对治疗是十分重要的。抑郁症是一种非常普遍的都市疾病，在如今压力大的生活中，平均每五个人当中，就有一个会在一生中受到不同程度的抑郁症困扰。缺乏家人的谅解会令病情恶化，把内心的感受表达出来可以加深家人对您的了解，而家人和朋友对您的体谅和鼓励，对治疗是十分重要的。抑郁症是一种非常普遍的都市疾病，在如今压力大的生活中，平均每五个人当中，就有一个会在一生中受到不同程度的抑郁症困扰。缺乏家人的谅解会令病情恶化，把内心的感受表达出来可以加深家人对您的了解，而家人和朋友对您的体谅和鼓励，对治疗是十分重要的。抑郁症是一种非常普遍的都市疾病，在如今压力大的生活中，平均每五个人当中，就有一个会在一生中受到不同程度的抑郁症困扰。缺乏家人的谅解会令病情恶化，把内心的感受表达出来可以加深家人对您的了解，而家人和朋友对您的体谅和鼓励.',
        title1: '抑郁症的主要症状',
        symptoms: ["三低症状: 情绪低落，思维迟缓，活动减少。",
          "三无症状: 无助，无望，无价值。",
          "三自症状: 自责，自罪，自杀。"
        ],
        title2: '针对抑郁症主要症状的10点建议',
        solves: [
          "正确对待疾病，保持乐观心态。",
          "及时求助医生，服药缓解抑郁症状。",
          "求助于心理专家，接受心理治疗。",
          "改善家庭环境，优化家庭氛围。",
          "坚持每天完成一件任务，转移注意力。",
          "家人可以鼓励患者多参加社交活动。",
          "听听轻音乐，听听歌，唱唱歌。",
          "积极进行认知调整。",
          "多活动，多锻炼。",
          "进行积极的自我暗示。",
        ],

        // <!-- 一周登录详情 -->
        meStyle3: {
          width: '100%',
          height: '350px',
          // float: 'left'
        },
        Data3: {
          title: {
            text: '研判分析',
            subtext: 'Fake Data',
            // left: 'center',
            x: 'center',
            y: 'bottom'
          },
          tooltip: {
            trigger: 'item'
          },
          xAxis: {
            type: 'category',
            data: []
            // data: ['2022-04-23', '2022-04-25', '2022-04-26', '2022-04-27', '2022-04-28', '2022-04-29', '2022-05-04']
          },
          yAxis: {
            type: 'value'
          },
          series: [
            {
              name: '测试值',
              data: [],
              // data: [8.0, 7.0, 8.0, 6.0, 9.0, 7.0, 6.0],
              type: 'line'
            }
          ]
        },
        title: '研判分析',
        description1: '经历风雨，迎来彩虹；走过艰难，踏上坦途；',
        description2: '洒下泪水，洗去烦忧；飘落白雪，阳光自来；',
        description3: '看到自己慢慢好起来，彻底跟所有的忧伤说拜拜。'
      }
    },
    created () {
      if (this.GLOBAL.IS_LOGIN == 0) {
        // this.$router.replace({ path: '/Login' });
        this.$router.push({ path: '/Login' })
      }
      this.init()
    },
    methods: {
      change () {
        this.GLOBAL.id = 2
      },
      init () {
        let that = this
        var i = 1
        axios.get('/history', { params: { id: this.GLOBAL.USERID } }).
          then(result => {
            console.log('history', result)
            // console.log(result.data.data.time[0])
            // console.log(result.data.data.score[0])
            // var time = "time" + i
            // var score = "score" + i
            // if (result.data.data.time)
            // that.Data3.series[0].data = result.data.data.score
            // that.Data3.xAxis.data = result.data.data.time

            // that.Data3.series.data = result.data.data.score
            // console.log(that.Data3.xAxis.data)
            // console.log(that.Data3.series.data)
            if (result.data.data.score.length) {
              console.log(result.data.data.score.length)
              that.ifEcharts = 1
              for (var i = Math.max(0, result.data.data.score.length - 7), j = 0; i < result.data.data.score.length; i++, j++) {
                that.Data3.series[0].data[j] = parseInt(result.data.data.score[i] + 0.5)
                that.Data3.xAxis.data[j] = result.data.data.time[i]
              }
            } else {
              that.ifEcharts = 0
            }
            console.log(that.Data3.series[0].data)
            console.log(that.Data3.xAxis.data)

            // console.log(that.Data3.xAxis.data)
            // console.log(that.Data3.series.data)
            // console.log(that.Data3.series.data[1])
            // console.log(result.data.data.time0)
            // console.log(result.data.data.time[0])
            // console.log(result.data.data.score[0])
          }).catch(error => (
            this.$message({
              message: error,
              type: 'warning'
            })
            // console.log(error)
          ))
      }
    }
  }
</script>
<style scoped>
  .background {
    background: url("../assets/image/history/bg.jpg");
    background-size: 100%;
    height: auto;
    /* height: 100%; */
    /* position: fixed; */
    width: 100%;
    overflow: hidden;
  }

  .title {
    margin-left: 270px;
    padding: 150px 0 30px 0;
  }

  .pd {
    padding: 0 136px;
  }

  p {
    font-size: 18px;
    line-height: 22px;
  }

  .description {
    margin-right: 50px;
    font-size: 18px;
    font-family: 'SimHei';
    line-height: 25px;
    padding: 5px 0;
    text-align: center;
  }
</style>