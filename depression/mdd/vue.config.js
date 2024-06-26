/*
 * @Autor: Hongting Yuan
 * @Date: 2022-04-05 11:46:49
 * @LastEditors: Hongting Yuan
 * @LastEditTime: 2022-04-25 15:45:54
 * @Description: file content
 * @FilePath: \mdd\vue.config.js
 */
// 跨域配置 
module.exports = { 
  devServer: { //记住，别写错了devServer//设置本地默认端口 选填 
    host: 'localhost', 
    port: 8080, 
    proxy: { //设置代理，必须填 
      '/api': { //设置拦截器 拦截器格式 斜杠+拦截器名字，名字可以 自己定 
        // target: 'http://127.0.0.1:5000', //代理的目标地址 
        // target: 'http://depression.free.idcfengye.com', //代理的目标地址 
        target: 'http://depression.vipgz6.91tunnel.com', //代理的目标地址 
        changeOrigin: true, //是否设置同源，输入是的 
        pathRewrite: { //路径重写 
          '/api': '' 
          //选择忽略拦截器里面的单词 
        } 
      } 
    } 
  } 
}
