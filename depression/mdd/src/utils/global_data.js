/*
 * @Autor: Hongting Yuan
 * @Date: 2022-04-04 23:58:57
 * @LastEditors: Hongting Yuan
 * @LastEditTime: 2022-04-05 00:00:48
 * @Description: file content
 * @FilePath: \mdd\src\global_data.js
 */
var g_data = {
  id:1
}
import Vue from 'vue'

Vue.prototype.g_data_watch = (objItem, callback) => {

Object.defineProperty(g_data,objItem, {

get:function(){

returnthis.value

},

set:function(newValue){

this.value=newValue

callback(this.value)

}

})

}

export default g_data
