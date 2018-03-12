import Vue from 'vue'
import Router from 'vue-router'
import Home from 'components/home/home'
import State from 'components/state/state'
import Blog from 'components/blog/blog'
import About from 'components/about/about'

Vue.use(Router)

export default new Router({
  linkActiveClass: 'active',
  routes: [
    {
      path: '/',
      redirect: '/home',
    },
    {
      path: '/home',
    	name: 'home',
    	component: Home
    },
    {
      path: '/state',
    	name: 'state',
    	component: State
    },
    {
      path: '/blog',
    	name: 'blog',
    	component: Blog
    },
    {
      path: '/about',
    	name: 'about',
    	component: About
    }
  ]
})
