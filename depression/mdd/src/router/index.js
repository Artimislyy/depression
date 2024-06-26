/*
 * @Autor: Hongting Yuan
 * @Date: 2022-04-02 14:37:50
 * @LastEditors: Hongting Yuan
 * @LastEditTime: 2022-04-29 12:29:50
 * @Description: file content
 * @FilePath: \mdd\src\router\index.js
 */
import Vue from 'vue'
import Router from 'vue-router'
import Introduction from '@/views/Introduction'
import Other from '@/views/Other'
import TreatMent from '@/views/TreatMent'
import Home from '@/views/Home'
import Test from '@/views/Test'
import Family from '@/views/Family'
import Pressure from '@/views/Pressure'
import HistoryView from '@/views/HistoryView'
import Login from '@/views/Login'
import Register from '@/views/Register'
import information from '@/views/information'
import '../assets/css/global.css'


Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      redirect: 'Home'
    },
    {
      path: '/Home',
      name: 'Home',
      component: Home,
      children: [
        {
          path: '/information',
          name: 'information',
          component: information
        },
        {
          path: '/Introduction',
          name: 'Introduction',
          component: Introduction
        },
        {
          path: '/Other',
          name: 'Other',
          component: Other
        },
        {
          path: '/TreatMent',
          name: 'TreatMent',
          component: TreatMent
        },
        {
          path: '/Family',
          name: 'Family',
          component: Family
        },
        {
          path: '/Pressure',
          name: 'Pressure',
          component: Pressure
        },
        {
          path: '/Test',
          name: 'Test',
          component: Test
        },
        {
          path: '/HistoryView',
          name: 'HistoryView',
          component: HistoryView
        },
      ]
    },
    {
      path: '/Login',
      name: 'Login',
      component: Login
    },
    {
      path: '/Register',
      name: 'Register',
      component: Register
    },
    // {
    //   path: '/tt',
    //   name: 'tt',
    //   component: tt
    // }
  ]
})

