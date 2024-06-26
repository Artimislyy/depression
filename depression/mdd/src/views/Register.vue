<!--
 * @Autor: Hongting Yuan
 * @Date: 2022-04-25 22:53:16
 * @LastEditors: Hongting Yuan
 * @LastEditTime: 2022-04-29 18:17:05
 * @Description: file content
 * @FilePath: \mdd\src\views\Register.vue
-->
<template>
  <div class="background">
    <div style="height: 58px;"></div>
    <div class="login">
      <p style="text-align: center;margin: 20px 0;">Register</p>
      <div style="height: 10px;"></div>
      <el-input type="text" v-model="username" placeholder="用户名"></el-input>
      <el-input type="password" v-model="password1" placeholder="密码"></el-input>
      <el-input type="password" v-model="password2" placeholder="确认密码"></el-input>
      <el-input type="email" v-model="email" placeholder="邮箱"></el-input>
      <div>
        <el-radio v-model="radio" label="1">男</el-radio>
        <el-radio v-model="radio" label="2">女</el-radio>
      </div>

      <el-button type="primary" @click="Register" v-preventReClick="3000"
        style="background-color: #59C2C5;color: white;font-size: 24px;border: none;margin-top: 30px;">注册</el-button>
      <a @click="goLogin"
        style="margin-left: 10px;border-bottom: 1px solid rgb(15, 151, 225);color: rgb(15, 151, 225);">去登录</a>
    </div>
  </div>
</template>
<script>
  import axios from 'axios'
  export default {
    name: "Register",
    data () {
      return {
        title: '注册',
        username: '',
        password1: '',
        password2: '',
        email: '',
        radio: '1'
      }
    },
    methods: {
      goLogin () {
        this.$router.replace({ path: '/Login' });
      },

      Register () {
        var reg = /^[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$/;
        if (this.username == '' || this.password1 == '' || this.password2 == '') {
          this.$message({
            message: '用户名和密码不能为空',
            type: 'warning'
          });
        } else if (this.password1 != this.password2) {
          this.$message({
            message: '两次密码不一致',
            type: 'warning'
          });
        } else if (!reg.test(this.email)) {
          this.$message({
            message: '请输入有效的邮箱',
            type: 'warning'
          });
        } else {
          console.log(this.username)
          var formData = new FormData();
          formData.append('username', this.username);
          formData.append('password', this.password1);
          formData.append('repassword', this.password2);
          formData.append('email', this.email);
          axios.post('/register', formData, { headers: { 'Content-Type': 'multipart/form-data' } },) //请求头要为表单
            .then(res => {
              if (res.data.code == 200) {
                this.$message({
                  message: '注册成功，快去登录吧',
                  type: 'success'
                });
                console.log(res.data);
                this.username = ''
                this.password1 = ''
                this.password2 = ''
                this.email = ''
                this.$router.replace({ path: '/Login' });
              } else {
                this.$message({
                  message: res.data.msg,
                  type: 'warning'
                });
              }
            })
            .catch(function (error) {
              this.$message.error(error);
            })
        }
      }
    }
  }
</script>
<style scoped>
  * {
    user-select: none;
    /* 无法选中，整体感更强 */
  }

  .background {
    background: url("../assets/image/home/bg.jpg");
    background-size: 100%;
    /* height: auto; */
    height: 600px;
    /* position: fixed; */
    width: 100%;
    overflow: hidden;
    margin-top: -85px;
  }

  /* .background {
    background: url("../assets/image/home/bg.jpg") no-repeat;
    background-size: cover;
    background-attachment: fixed;
  } */

  .login {
    position: absolute;
    top: 50%;
    margin-top: -200px;
    left: 50%;
    margin-left: -200px;
    /* absolute居中的一种方法 */
    /* background-color: whitesmoke; */
    background-color: rgba(255, 255, 255, 0.6);
    width: 400px;
    height: 450px;
    border-radius: 25px;
    text-align: center;
    padding: 5px 40px;
    box-sizing: border-box;
    /* 这样padding就不会影响大小 */
  }

  p {
    font-size: 42px;
    font-weight: 600;
  }

  .el-input {
    /* background-color: rgba(255, 255, 255, 0.6); */

    /* background-color: rgba(255, 255, 255, 0.6); */
    /* color: rgba(255, 255, 255, 0.6); */
    /* border-bottom: 2px solid rgba(255, 255, 255, 0.6); */
    /* 下面的会覆盖上面的步伐 */

  }

  /deep/.el-input__inner {
    border-radius: 0;
    width: 100%;
    margin: 10px 0;
    border: none;
    background-color: transparent !important;
    border-bottom: 2px solid rgb(180, 180, 180);
    outline: none;
    font-size: 22px;
  }

  /* .el-input__inner {
    background-color: rgba(255, 255, 255, 0.6);
    color: rgba(255, 255, 255, 0.6);
  } */

  .btn {
    background-color: #59c2c5;
    width: 38%;
    height: 48px;
    border-radius: 8px;
    margin-top: 40px;
    font-size: 28px;
    font-weight: 600;
    color: white;
  }

  .btn:hover {
    background-color: #59c2a0;
  }
</style>