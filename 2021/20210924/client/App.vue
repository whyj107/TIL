<template>
  <div>
    <nav class="main-nav">
      <div class="logo">Vue Project</div>
      <burger></burger>
    </nav>
    <div id="app">
      <router-view/>
    </div>
    <sidebar></sidebar>
  </div>
</template>

<script>
import Burger from './components/menu/Burger.vue';
import Sidebar from './components/menu/Sidebar.vue';

export default {
  name: 'App',
  components: {
    Burger,
    Sidebar,
  },
};
</script>

<style>
html {
   height: 100%;
   overflow:scroll;
 }

body {
  border: 0; margin: 0; padding: 0;
  font-family: 'Lato';
  height: 100%;
  background: #fff;
}

.logo {
  align-self: center;
  color: #fff;
  font-weight: bold;
  font-family: 'Lato';
  text-shadow: -1px 0 black, 0 1px black, 1px 0 black, 0 -1px black;
}

.main-nav {
  display: flex;
  justify-content: space-between;
  padding: 0.5rem 0.8rem;
  background: #ebe8ff;
}
</style>
