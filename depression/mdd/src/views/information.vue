<template>
  <div class="animated fadeIn" style="background-color: #F3E9DF">
    <div id="main"></div>
  </div>
</template>
<script>
  // import echarts from 'echarts'
  // import 'echarts/map/js/china.js'
  import echarts from 'echarts'
  import 'echarts/map/js/china.js'
  export default {
    name: "information",
    data () {
      return {
        dataList: [
          // { name: '南海诸岛', value: 0 },
          { name: '北京', value: 6.4 },
          { name: '天津', value: 4.3 },
          { name: '上海', value: 11.8 },
          { name: '重庆', value: 4.8 },
          { name: '河北', value: 10.6 },
          { name: '河南', value: 10.7 },
          { name: '云南', value: 5.6 },
          { name: '辽宁', value: 4.9 },
          { name: '黑龙江', value: 4.5 },
          { name: '湖南', value: 5.2 },
          { name: '安徽', value: 9.4 },
          { name: '山东', value: 10.2 },
          { name: '新疆', value: 5.3 },
          { name: '江苏', value: 11.2 },
          { name: '浙江', value: 7.3 },
          { name: '江西', value: 9.0 },
          { name: '湖北', value: 11.0 },
          { name: '广西', value: 6.6 },
          { name: '甘肃', value: 8.5 },
          { name: '山西', value: 10.5 },
          { name: '内蒙古', value: 5.4 },
          { name: '陕西', value: 6.1 },
          { name: '吉林', value: 4.6 },
          { name: '福建', value: 5.5 },
          { name: '贵州', value: 5.6 },
          { name: '广东', value: 4.2 },
          { name: '青海', value: 5.8 },
          { name: '西藏', value: 5.0 },
          { name: '四川', value: 4.2 },
          { name: '宁夏', value: 5.9 },
          { name: '海南', value: 5.1 },
          // { name: '台湾', value: 2369 },
          // { name: '香港', value: 748.25 },
          // { name: '澳门', value: 63.2 }
        ]
      }
    },
    methods: {
      buildMap () {
        let myChart = echarts.init(document.getElementById('main'));
        let option = {
          tooltip: {
            formatter: function (params, ticket, callback) {
              return '发病率' + '<br />' + params.name + '：' + params.value + '%'
            }//数据格式化
          },
          title: {
            text: '中国各省抑郁症发病率（不含港澳台）',
            subtext: 'Fake Data',
            // left: 'center',
            x: 'center',
            y: 'bottom'
          },
          visualMap: {
            min: 4,
            max: 12,
            left: 'left',
            top: 'bottom',
            text: ['高12%', '低4%'],//取值范围的文字
            inRange: {
              color: ['#fff4e6', '#dd2002']//取值范围的颜色
            },
            show: true//图注
          },
          geo: {
            map: 'china',
            roam: false,//不开启缩放和平移
            zoom: 1.23,//视角缩放比例
            label: {
              normal: {
                show: true,
                fontSize: '10',//注意：地图省份名字字体如果过大会导致字体重叠
                color: 'rgba(0,0,0,0.7)'
              }
            },
            itemStyle: {
              normal: {
                borderColor: 'rgba(0, 0, 0, 0.2)'
              },
              emphasis: {
                areaColor: '#F3B329',//鼠标选择区域颜色
                shadowOffsetX: 0,
                shadowOffsetY: 0,
                shadowBlur: 20,
                borderWidth: 0,
                shadowColor: 'rgba(0, 0, 0, 0.5)'
              }
            }
          },
          series: [
            {
              name: '信息量',
              type: 'map',
              geoIndex: 0,
              data: this.dataList
            }
          ]
        };
        myChart.setOption(option);
      }
    },
    mounted () {
      this.buildMap()
    }
  }
</script>

<style scoped>
  * {
    margin: 0;
    padding: 0
  }

  html,
  body {
    width: 100%;
    height: 100%;
  }

  #main {
    /* background-color: #e7b53f; */
    background-color: #F3E9DF;
    width: 700px;
    height: 600px;
    margin: 0px auto;
    /* margin-top: 20px; */
    margin-bottom: 30px;
    border: none;
  }
</style>