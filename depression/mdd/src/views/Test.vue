<!--
 * @Autor: Hongting Yuan
 * @Date: 2022-04-02 14:59:09
 * @LastEditors: Hongting Yuan
 * @LastEditTime: 2022-05-27 15:38:32
 * @Description: file content
 * @FilePath: \mdd\src\views\Test.vue
-->
<!-- 改change函数位置 -->
<template>
  <div>
    <audio id="audio1" src="../static/audio/1.mp3" hidden></audio>
    <audio id="audio2" src="../static/audio/2.mp3" hidden></audio>
    <audio id="audio3" src="../static/audio/3.mp3" hidden></audio>
    <audio id="audio4" src="../static/audio/4.mp3" hidden></audio>
    <audio id="audio5" src="../static/audio/5.mp3" hidden></audio>
    <audio id="audio6" src="../static/audio/6.mp3" hidden></audio>
    <audio id="audio7" src="../static/audio/7.mp3" hidden></audio>
    <audio id="audio8" src="../static/audio/8.mp3" hidden></audio>
    <audio id="audio9" src="../static/audio/9.mp3" hidden></audio>
    <audio id="audio10" src="../static/audio/10.mp3" hidden></audio>
    <audio id="audio11" src="../static/audio/ans1.mp3" hidden></audio>
    <audio id="audio12" src="../static/audio/ans2.mp3" hidden></audio>
    <audio id="audio13" src="../static/audio/ans3.mp3" hidden></audio>
    <audio id="audio14" src="../static/audio/ans4.mp3" hidden></audio>
    <audio id="audio15" src="../static/audio/ans5.mp3" hidden></audio>
    <audio id="audio16" src="../static/audio/ans6.mp3" hidden></audio>
    <!-- 测试问卷 -->
    <div class="background1" v-if="num==0">
      <div>
        <img src="../assets/image/test/question/frozen.png" alt=""
          style="width: 350px;height: 340px; float: right;margin-left: -500px;margin-top: 40px;">
        <h1 class="title">{{title_test}}</h1>
        <p class="description">{{description_test1}}</p>
        <p class="description">{{description_test2}}</p>
        <p class="description" style="margin-bottom: 200px;">{{description_test3}}</p>
        <!-- <div v-for="(item,index) in questions" :key="index" style="width: 700px;margin-left: 286px;" v-if="id==3">
          <p style="margin: 12px 0;">{{item}}</p>
          <div>
            <el-radio-group v-model="radio[index]" style="text-align: left;margin: 0;padding: 0;">
              <el-radio :label="3">一点也不</el-radio>
              <el-radio :label="6">偶尔</el-radio>
              <el-radio :label="9">经常</el-radio>
              <el-radio :label="12">几乎每天</el-radio>
            </el-radio-group>
          </div>
        </div> -->
        <!-- 抑郁症 -->
        <div v-if="id==3">
          <h2 style="margin-left: 286px;margin-bottom: 20px;">{{test_title}}</h2>
          <div v-for="(item,index) in questionnaire_one" :key="index" style="width: 700px;margin-left: 286px;">
            <p style="margin: 12px 0;">{{item}}</p>
            <div>
              <el-radio-group v-model="radio[index]" style="text-align: left;margin: 0;padding: 0;">
                <el-radio :label="0">一点也不</el-radio>
                <el-radio :label="1">偶尔</el-radio>
                <el-radio :label="2">经常</el-radio>
                <el-radio :label="3">几乎每天</el-radio>
              </el-radio-group>
            </div>
          </div>
          <img src="../assets/image/test/question/button.png" alt=""
            style="width: 300px;margin-top: -50px;margin-right:-600px;" @click="goChatRoom">
          <h3 style="width: 300px;margin-left: 780px;margin-top: -170px;text-align: center;color: #692422;"
            v-if="this_question_num==0">去聊天室</h3>

          <div style="padding-bottom: 180px;"></div>
        </div>

        <!-- 其他情绪病 -->
        <div v-if="id==2">
          <h2 style="margin-left: 286px;margin-bottom: 20px;">{{test_title}}</h2>
          <div v-for="(item,index) in questionnaire_two" :key="index" style="width: 700px;margin-left: 286px;">
            <p style="margin: 12px 0;">{{item}}</p>
            <div>
              <el-radio-group v-model="radio[index]" style="text-align: left;margin: 0;padding: 0;">
                <el-radio :label="0">一点也不</el-radio>
                <el-radio :label="1">偶尔</el-radio>
                <el-radio :label="2">经常</el-radio>
                <el-radio :label="3">几乎每天</el-radio>
              </el-radio-group>
            </div>
          </div>
          <img src="../assets/image/test/question/button.png" alt=""
            style="width: 300px;margin-top: -50px;margin-right:-600px;" @click="getOtherResult">
          <h3 style="width: 300px;margin-left: 780px;margin-top: -170px;text-align: center;color: #692422;"
            v-if="this_question_num==0">分析结果</h3>
          <div style="padding-bottom: 150px;"></div>
          <div v-if="other_result_num==2">
            <div style="margin-top: 200px;"></div>
            <p style="padding-left: 500px;width: 400px;">{{other_result_analysis}}</p>
            <p style="height: 130px;margin-top: 20px; padding-left: 550px;width: 400px; font-size: 16px;">
              {{other_result_tips}}</p>
          </div>
        </div>


      </div>
    </div>
    <!-- 聊天室 -->
    <div class="background2" v-if="num>=1">
      <div class="pd">
        <h1 class="title">{{title}}</h1>
        <p class="description">{{description1}}</p>
        <p class="description">{{description2}}</p>
        <p style="margin-top: 200px;">{{content1}}</p>
        <p>{{content2}}</p>
        <div
          style="float: left; width: 200px; height: 120px; margin-top: 220px;margin-bottom: -100px;margin-right: -250px;">
          <video v-if="this_question_num>=1 && this.this_question_num<8" id="video" autoplay ref="videos"
            style="width: 100%;height: 100%;" muted></video>
          <video style="position:absolute;" :style="recordtype=='END'?'z-index:3':'z-index:1'" id="videosreplay"
            class="local-video" src="" ref="videosreplay" hidden></video>
          <!-- <video :style="recordtype=='END'?'z-index:3':'z-index:1'" id="videosreplay" src="" ref="videosreplay"
            style="width: 100%;height: 100%;"></video> -->
        </div>
        <img src="../assets/image/test/chatroom/xyf.png" alt=""
          style="width: 300px;height: auto;float: left;margin-left: -100px;margin-top: 360px;">
        <img src="../assets/image/test/chatroom/dialogbox_one.png" alt=""
          style="width: 300px;margin-top: 100px;margin-left: -500px;">
        <p style="width: 160px;margin-right: -180px;margin-left: 280px;margin-top: -240px;">注意：谈话过程中请确保您的脸部正对摄像头!!!</p>
        <img src="../assets/image/test/chatroom/dialogbox_two.png" alt=""
          style="width: 350px;margin-left: 300px;margin-bottom: -100px;">

        <img src="../assets/image/test/chatroom/button.png" alt=""
          style="width: 300px;margin-left: 520px;margin-top: -200px;" @click="next">
        <!-- <img src="../assets/image/test/chatroom/button.png" alt=""
          style="width: 300px;margin-left: 720px;margin-top: 50px;" @click="next" v-if="this_question_num > 8"
          v-preventReClick="3000"> -->
        <h3 style="width: 300px;margin-left: 606px;margin-top: -170px;text-align: center;color: #692422;"
          v-if="this_question_num==0">开始</h3>
        <!-- <audio src="../assets/audio/1.mp4" controls="controls"></audio> -->


        <h3 style="width: 300px;margin-left: 606px;margin-top: -170px;text-align: center;color: #692422;"
          v-if="this_question_num>0 && this_question_num<8">下一问</h3>

        <h3 style="width: 300px;margin-left: 606px;margin-top: -170px;text-align: center;color: #692422;"
          v-if="this_question_num>=8">分析结果</h3>
        <!-- <p>下一问</p>
          <p>分析结果</p> -->
        <div style="padding-bottom: 160px;"></div>
        <p style="width: 240px;margin-left: 630px;margin-top: -450px;height: 150px;">{{questions[this_question_num]}}
        </p>
        <div style="padding-bottom: 310px;" v-if="num==2"></div>
        <div v-if="result_num==2">
          <div style="padding-bottom: 50px;" v-if="num==2"></div>
          <!-- <p style="padding-left: 500px;width: 400px;">{{other_result_analysis}}</p> -->

          <p style="width: 460px;color: #893218;" v-if="num==2">{{yy_result_analysis}}{{yy_score}}</p>
          <section>
            <div class="box">
              <div class="mo" :style="{'--progress':-progress+100+'%'}"></div>
              <i></i>
            </div>
            <!-- <el-input-number v-model="progress" :step="10"></el-input-number> -->
          </section>
          <p style="margin-top: 20px; padding-left: 50px;width: 400px; font-size: 16px;margin-bottom: 100px;">
            {{yy_result_tips}}</p>
          <el-button type="primary" round @click="getHistory"
            style="float: right; margin-right: -80px; margin-bottom: 10px;text-align: right;background-color: #56551D;border: none;">
            历史信息</el-button>
          <!-- <div style="margin-top: 200px;"></div> -->
        </div>

        <!-- <div v-if="num==1"> -->
      </div>
    </div>
    <!-- <input style="width: 74px;" type="file" id="uFile" name="uFile" @change="upload($event)" /> -->
  </div>

</template>
<script>
  import axios from 'axios'
  import fixWebmDuration from 'webm-duration-fix'

  export default {
    name: "Test",
    data () {
      return {
        progress: 0,
        replayVideo: false,
        recordtype: "BEGIN",
        showReplay: true,
        timer: 0,
        recordtime: 0,
        second: 0,
        minute: 0,
        hour: 0,
        playtime: 0,
        playtimer: 0,
        yy_score: 0,
        id: this.GLOBAL.id,
        test_title: '请根据自身最近两周情况回答下列问题',
        title: '聊天室',
        description1: '来这儿坐坐，敞开心扉',
        description2: '忘记过去的痛楚，一切都会好的',
        content1: '没有人会一直顺利，愿你更加强大',
        content2: '然后有一天，你可以笑着讲述那些曾让你哭的瞬间',
        result: '加油加油加油加油加油加油加油加油加油加油加油加油加油加油加油加油加油加油加油加油加油加油加油加油',
        questionnaire_one:
          ["1、对做事没有兴趣或乐趣？",
            "2、感到沮丧、沮丧或绝望？",
            "3、入睡或保持睡眠困难，或睡眠过多？",
            "4、感到疲倦或精力不足？",
            "5、食欲不振或暴饮暴食？",
            "6、自我感觉不好，感觉自己是个失败者，让家人或自己失望了？",
            "7、注意力不能集中在一些事情上，比如读书或看电视？",
            "8、移动或说话的速度很慢，以至于其他人可能会注意到？或者是相反的情况--焦躁不安或坐立不安，以至于你比平时多四处走动？",
            "9、认为你最好死了或者以某种方式伤害自己？",
          ],
        questionnaire_two:
          ["1、过去数月，你是否多次突然感到很害怕或惊恐，而每次通常持续数分钟至数小时？",
            "2、经常检查灯和水龙头关好没有？",
            "3、有时担心会给自己或所爱的人带来伤害？",
            "4、经常想到亲人会有不幸？",
            "5、你是否总是尽量想提前离开有可能使你遭遇尴尬的境地？",
            "6、惊恐的时候，会感觉呼吸困难、担心不能自控？",
            "7、经常觉得身上衣服有些不对劲？",
            "8、是否老是对自己和自己所干的事不满意，尽管已经努力想干好？",
            "9、经历惊恐后，你是否持续一个月或以上，担忧以后再出现惊恐？",
          ],
        questions:
          ["你好呀，为了更好的进行测试，接下来我将问你几个问题，谈话内容完全保密，让我们开始吧！",
            "你最近心情怎么样",
            "是因为什么事情让你拥有这样的心情呢",
            "你最近做的最开心的一件事情是什么呢",
            "你最近有去旅行吗，如果有可以和我讲讲旅行中发生的事情吗",
            "你做过最后悔的一件事情是什么，可以和我分享一下吗",
            "你曾经被诊断出患有抑郁症吗",
            "你想改变自己现在的生活吗？如果想，你希望怎么改变",
            "好吧，我想我已经问了所有需要问的问题，谢谢你和我分享你的想法",
            "请耐心等待分析结果",
            "请耐心等待分析结果",
            "请耐心等待分析结果",
            "请耐心等待分析结果",
            "请耐心等待分析结果",
            "请耐心等待分析结果",
          ],
        // questions:
        //   ["你好呀，为了更好的进行测试，接下来我将问你几个问题，谈话内容完全保密，让我们开始吧！",
        //     "你最近感觉怎么样",
        //     "告诉我你最近做的一些你非常喜欢的事情",
        //     "你最好的朋友会如何形容你",
        //     "我很想听听你的一次旅行",
        //     "有什么让你后悔的事情吗",
        //     "你曾经被诊断出患有抑郁症吗",
        //     "你希望改变自己的哪些方面",
        //     "你一生中最自豪的是什么",
        //     "好吧，我想我已经问了所有需要问的问题，谢谢你和我分享你的想法"
        //   ],
        title_test: '抑郁症测试',
        this_question_num: 0,
        description_test1: '伤心、难过、失眠……你真的是抑郁症吗',
        description_test2: '如果不是，大胆放下顾虑，向阳而生',
        description_test3: '如果是，请努力走向出口，我们永远在你身后',
        num: 0,
        radio: [0, 0, 0, 0, 0, 0, 0, 0, 0,],
        result_num: 0,
        other_result_num: this.GLOBAL.other_result_num,
        yy_result_analysis: 'PHQ-9评估得分范围在0-23，分数越高越可能抑郁。您的得分为:',
        // yy_result_analysis: '根据已综合的诊断标准，初步显示你可能已经患上抑郁症，建议你尽快向专业人士寻求评估。',
        yy_result_tips: '请注意，抑郁症自我测试绝对不能代替专业临床评估。如果你对抑郁症有任何疑问，请向临床心理学家或有关医生寻求专业协助。',
        other_result_analysis: "根据已综合的诊断标准，初步显示你可能已经患上" + this.GLOBAL.OTHER + "，建议你尽快向专业人士寻求评估。",
        other_result_analysis: "根据已综合的诊断标准，初步显示你没有患上" + this.GLOBAL.OTHER + "。",
        // other_result_analysis: '根据已综合的诊断标准，初步显示你可能已经患上，建议你尽快向专业人士寻求评估。',
        other_result_tips: "请注意，" + this.GLOBAL.OTHER + "自我测试绝对不能代替专业临床评估。如果你对" + this.GLOBAL.OTHER + "有任何疑问，请向临床心理学家或有关医生寻求专业协助。",
        audio: ['audio1', 'audio2', 'audio3', 'audio4', 'audio5', 'audio6', 'audio7', 'audio8', 'audio9', 'audio10', 'audio11', 'audio12', 'audio13', 'audio14', 'audio15', 'audio16'],
        cnt_sum: 0,
        ansMaxTime: 0,
        ansBeginTime: 0,
        ansMaxBeginTime: 0,

      }
    },
    created () {
      if (this.GLOBAL.IS_LOGIN == 0) {
        // this.$router.replace({ path: '/Login' });
        this.$router.push({ path: '/Login' })
      }
      // console.log(parseInt('2.345'))
      this.id = this.GLOBAL.id
      if (this.GLOBAL.id == 2) {
        this.title_test = "情绪病测试"
      }
      this.other_result_num = 0
      console.log(this.GLOBAL.id)
    },
    methods: {
      getHistory () {
        // this.$router.replace({ path: '/HistoryView' });
        this.$router.push({ path: '/HistoryView' })
      },
      // 调用摄像头
      callCamera () {
        let _this = this;
        MediaUtils.getUserMedia(true, true, function (err, stream) {
          if (err) {
            throw err;
          } else {
            // 通过 MediaRecorder 记录获取到的媒体流
            const mimeType = 'video/webm;codecs=vp8,opus';
            mediaRecorder = new MediaRecorder(stream, {
              // mimeType: "video/webm;codecs=vp9",
              mimeType: mimeType,
            });
            mediaStream = stream;
            var chunks = []
            // startTime = 0;
            var video = _this.$refs.videos;
            video["srcObject"] = stream;
            video.play();// 播放实时画面
            mediaRecorder.ondataavailable = function (e) {
              mediaRecorder.blobs.push(e.data);
              chunks.push(e.data);
            };
            mediaRecorder.blobs = [];

            mediaRecorder.onstop = async () => {
              // var duration = Date.now() - startTime;
              // console.log(duration)
              // c
              recorderFile = await fixWebmDuration(new Blob(chunks, { type: mimeType }));
              // ysFixWebmDuration(recorderFile, duration, function (fixedBlob) {
              //   recorderFile = fixedBlob
              //   console.log(recorderFile)
              // });
              console.log(recorderFile);
              var url = URL.createObjectURL(recorderFile)
              // var b = URL.readAsDataURL(recorderFile)
              var videosreplay = _this.$refs.videosreplay;
              videosreplay.setAttribute("src", url);
              console.log('url', url)
              // console.log('base64', b)
              chunks = [];
              if (null != stopRecordCallback) {
                stopRecordCallback();
              }
            };
            _this.record()
          }
        });
      },
      record () {
        if (this.recordtype == "ING") {
          this.stopRecord(() => {
            console.log("结束录制");
          });
        }
        else if (this.recordtype == "BEGIN") {
          console.log("开始录制");
          this.startAudio();
          mediaRecorder.start();
          startTime = Date.now();
          this.recordtype = "ING";
        }
      },

      // 对录像时长进行记录
      startAudio () {
        this.timer = setInterval(() => {
          this.recordtime += 1000;
          if (this.recordtime == 1000000) {
            this.stopRecord();
          }
          this.second++;
          if (this.second >= 60) {
            this.second = 0;
            this.minute = this.minute + 1;
          }

          if (this.minute >= 60) {
            this.minute = 0;
            this.hour = this.hour + 1;
          }
          console.log(this.recordtime)
        }, 1000);
      },

      // 停止录像时终止录制器，关闭媒体流并清除时长记录定时器
      stopRecord (callback) {
        this.recordtype = "END";
        this.showReplay = true;

        stopRecordCallback = callback;
        clearInterval(this.timer);
        // 终止录制器
        mediaRecorder.stop();
        // 关闭媒体流
        MediaUtils.closeStream(mediaStream);
        var videosreplay = this.$refs.videosreplay;
        videosreplay.onended = () => {
          this.playtime = 0;
          this.replayVideo = false;
          clearInterval(this.playtimer);
        };
        videosreplay.onclick = () => {
          this.showReplay = !this.showReplay;
        };
      },
      // 回放
      toggleReplayVideo () {
        console.log('播放中...')
        this.replayVideo = !this.replayVideo;
        this.showReplay = false;
        var videosreplay = this.$refs.videosreplay;
        if (this.replayVideo) {
          videosreplay.play().catch(err => {
            this.$message.error(err.message);
            console.log(err);
          });
          this.playtimer = setInterval(() => {
            this.playtime += 1000;
          }, 1000);
        } else {
          videosreplay.pause();
          clearInterval(this.playtimer);
        }
      },
      submit () {

        let that = this;
        console.log('cnt_sum111111111111', that.cnt_sum)
        console.log(recorderFile)
        var url = URL.createObjectURL(recorderFile)
        // var b = URL.readAsDataURL(recorderFile)
        console.log('url', url)
        // console.log('base64', b)
        let file = new File(
          [recorderFile],
          "msr-" + new Date().toISOString().replace(/:|\./g, "-") + ".mp4",
          {
            type: "video/mp4",
          }
        );
        let config = {
          headers: { "Content-Type": "multipart/form-data" }
        }
        console.log('file', file)
        const formdata = new FormData()
        formdata.append("file", file);
        console.log("video")
        console.log(formdata.get('file'))
        // axios.get('/video', { params: { vedio: formdata } }).then(function (result) {
        //   console.log(result)
        // }).catch(error => (console.log(error)))
        alert('分析需要一点时间，听首歌等等吧~~')
        document.getElementById(that.audio[8]).pause()
        document.getElementById(that.audio[9]).play()
        axios.post('/video', formdata, { headers: { 'Content-Type': 'application/x-www-form-urlencoded' } },) //请求头要为表单
          .then(response => {
            console.log('video', response.data);
            this.yy_score = parseInt(response.data.data + 0.5)
            that.progress = response.data.data * 1.0 / 23 * 100
            that.result_num = 2
            document.getElementById(that.audio[9]).pause()
            if (response.data.data <= 3.0) {
              document.getElementById(that.audio[10]).play()
              console.log(10)
            } else if (response.data.data > 3.0 && response.data.data <= 6.0) {
              document.getElementById(that.audio[11]).play()
              console.log(11)
            } else if (response.data.data > 6.0 && response.data.data <= 10.0) {
              document.getElementById(that.audio[12]).play()
              console.log(12)
            } else if (response.data.data > 10.0 && response.data.data <= 14.0) {
              document.getElementById(that.audio[13]).play()
              console.log(13)
            } else if (response.data.data > 14.0 && response.data.data <= 19.0) {
              document.getElementById(that.audio[14]).play()
              console.log(14)
            } else {
              document.getElementById(that.audio[15]).play()
              console.log(15)
            }
            that.$message({
              message: '分析完成，请查看结果~~',
              type: 'success'
            });
          })
          .catch(function (error) {
            document.getElementById(that.audio[9]).pause()
            // document.getElementById(that.audio[10]).play()
            that.$message({
              message: error,
              type: 'error'
            });
            console.log(error);
          })
        // axios.post('/video', formdata, {
        //   'Content-type': 'multipart/form-data'
        // }).then(function (result) {
        //   console.log(result)
        // }).catch(error => (console.log(error)))
      },
      next () {
        console.log(this.this_question_num)
        this.this_question_num = this.this_question_num + 1
        if (this.this_question_num == 1) {
          this.callCamera()
        }
        if (this.this_question_num == 8) {
          this.record()
        }
        if (this.this_question_num > 1 && this.this_question_num <= 8) {
          if (this.recordtime - this.ansBeginTime > this.ansMaxTime) {
            this.ansMaxTime = this.recordtime - this.ansBeginTime
            this.ansMaxBeginTime = this.ansBeginTime
          }
          this.ansBeginTime = this.recordtime
          console.log(this.ansMaxBeginTime, this.ansMaxTime)
        }

        if (this.this_question_num == 9) {

          axios.get('/Time', { params: { timeBegin: this.ansMaxBeginTime, timeEnd: this.ansMaxBeginTime + this.ansMaxTime } }).
            then(result => {
              console.log(result)
              if (this.this_question_num == 9) {
                this.submit()
              }
            }).catch(error => (console.log(error)))
        }
        if (this.this_question_num > 9) {
          this.$message({
            message: '请耐心等等分析结果',
            type: 'warning'
          });
        }
        // if (this.this_question_num > 0) {
        if (this.this_question_num < 9) {
          console.log('audio', this.audio[this.this_question_num])
          document.getElementById(this.audio[this.this_question_num - 1]).pause()
          document.getElementById(this.audio[this.this_question_num]).play()
          // document.getElementById(this.audio[11]).play()
        }

        // }


      },
      goChatRoom () {
        this.num = 2
        document.getElementById(this.audio[0]).play()
        console.log(this.num)
        this.cnt_sum = 0
        for (var i = 0; i <= 8; i++) {
          console.log(this.radio[i])
          console.log(this.cnt_sum)
          this.cnt_sum = this.cnt_sum + this.radio[i]
        }
        if (this.cnt_sum >= 13) {
          // this.yy_result_analysis = "根据已综合的诊断标准，初步显示你可能已经患上抑郁症，建议你尽快向专业人士寻求评估。"
          this.other_result_analysis = "根据已综合的诊断标准，初步显示你可能已经患上" + this.GLOBAL.OTHER + "，建议你尽快向专业人士寻求评估。"
        } else {
          // this.yy_result_analysis = "根据已综合的诊断标准，初步显示你没有患上抑郁症。"
          this.other_result_analysis = "根据已综合的诊断标准，初步显示你没有患上" + this.GLOBAL.OTHER + "。"
        }
        console.log('cnt', this.cnt_sum)
        // var message = JSON.stringify({ Score: this.cnt_sum });
        // var message = {  }
        axios.get('/Score', { params: { Score: this.cnt_sum } }).then(result => {
          console.log(result)
        }).catch(error => (console.log(error)))
      },
      getOtherResult () {
        this.cnt_sum = 0
        this.other_result_num = 2
        for (var i = 0; i <= 8; i++) {
          console.log(this.radio[i])
          console.log(this.cnt_sum)
          this.cnt_sum = this.cnt_sum + this.radio[i]
        }
        if (this.cnt_sum >= 15) {
          // this.yy_result_analysis = "根据已综合的诊断标准，初步显示你可能已经患上抑郁症，建议你尽快向专业人士寻求评估。"
          this.other_result_analysis = "根据已综合的诊断标准，初步显示你可能已经患上" + this.GLOBAL.OTHER + "，建议你尽快向专业人士寻求评估。"
        } else {
          // this.yy_result_analysis = "根据已综合的诊断标准，初步显示你没有患上抑郁症。"
          this.other_result_analysis = "根据已综合的诊断标准，初步显示你没有患上" + this.GLOBAL.OTHER + "。"
        }
        console.log('cnt', this.cnt_sum)
      }
    }
  }
  var MediaUtils = {
    /**
     * 获取用户媒体设备(处理兼容的问题)
     * @param videoEnable {boolean} - 是否启用摄像头
     * @param audioEnable {boolean} - 是否启用麦克风
     * @param callback {Function} - 处理回调
     */
    getUserMedia: function (videoEnable, audioEnable, callback) {
      navigator.getUserMedia =
        navigator.getUserMedia ||
        navigator.webkitGetUserMedia ||
        navigator.mozGetUserMedia ||
        navigator.msGetUserMedia ||
        window.getUserMedia;
      var constraints = { video: videoEnable, audio: audioEnable };
      if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
        navigator.mediaDevices
          .getUserMedia(constraints)
          .then(function (stream) {
            callback(false, stream);
          })
        ["catch"](function (err) {
          callback(err);
        });
      } else if (navigator.getUserMedia) {
        navigator.getUserMedia(
          constraints,
          function (stream) {
            callback(false, stream);
          },
          function (err) {
            callback(err);
          }
        );
      } else {
        callback(new Error("Not support userMedia"));
      }
    },

    /**
     * 关闭媒体流
     * @param stream {MediaStream} - 需要关闭的流
     */
    closeStream: function (stream) {
      if (typeof stream.stop === "function") {
        stream.stop();
      } else {
        let trackList = [stream.getAudioTracks(), stream.getVideoTracks()];

        for (let i = 0; i < trackList.length; i++) {
          let tracks = trackList[i];
          if (tracks && tracks.length > 0) {
            for (let j = 0; j < tracks.length; j++) {
              let track = tracks[j];
              if (typeof track.stop === "function") {
                track.stop();
              }
            }
          }
        }
      }
    },
  };
  var startTime, mediaRecorder, mediaStream, stopRecordCallback, recorderFile;
</script>
<style scoped>
  .box {
    position: relative;
    width: 500px;
    height: 20px;
    overflow: hidden;
    background: linear-gradient(270deg, #ff0000 10%, #ffc801 70%, #00ffa2 100%);
  }

  .mo {
    position: absolute;
    z-index: 1;
    right: 0;
    height: 100%;
    width: var(--progress, 0%);
    background-color: #ccc;
  }

  .background2 {
    background: url("../assets/image/test/chatroom/bg.jpg");
    background-size: 100%;
    height: auto;
    /* height: 100%; */
    /* position: fixed; */
    width: 100%;
    overflow: hidden;
  }

  .background1 {
    background: url("../assets/image/test/question/bg.jpg");
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
</style>