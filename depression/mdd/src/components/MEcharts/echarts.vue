<!--
 * @Autor: Hongting Yuan
 * @Date: 2022-04-26 00:26:52
 * @LastEditors: Hongting Yuan
 * @LastEditTime: 2022-05-26 22:25:06
 * @Description: file content
 * @FilePath: \mdd\src\components\MEcharts\echarts.vue
-->
<template>
  <!-- <div class="charttest"> -->
  <div :id="echarts" ref="echarts" class="echarts" :style="{width:meStyle.width,height:meStyle.height}" />
  <!-- </div> -->
</template>

<script>
  // import * as echarts from 'echarts'
  import echarts from 'echarts'
  export default {
    name: 'Echarts',
    components: {},
    props: {
      chartData: {
        type: Object,
        default: () => { }
      },
      meStyle: {
        type: Object,
        default: () => {
          return {
            width: '400px',
            height: '400px'
          }
        }
      }
    },
    data () {
      return {
      }
    },
    computed: {
      echarts () {
        return 'echarts' + Math.random() * 100000
      }
    },
    watch: {
      chartData: {
        /**
         * @description: 渲染echarts数据
         * @param {*} newVal
         * @param {*} oldVal
         * @return {*}
         * @author: Hongting Yuan
         */
        handler (newVal, oldVal) {
          if (this.myChart) {
            if (newVal) {
              this.myChart.setOption(newVal)
            } else {
              this.myChart.setOption(oldVal)
            }
          } else {
            // setTimeout(() => { // 延时加载echarts初始化函数
              this.drawCharts()
              // }, 1000)
            }
        },
          // handler() {
          //   this.drawCharts()
          // },
          immediate: true,
            deep: true
        }
      },
      mounted () {
        // setTimeout(() => { // 延时加载echarts初始化函数
          this.drawCharts()
        // }, 500)
      },
      methods: {
        drawCharts () {
          var myChart = echarts.init(document.getElementById(this.echarts))
          myChart.setOption(this.chartData, true)
        }
      }
    }
</script>

<style>
  .echarts {
    padding: 2%;
  }
</style>