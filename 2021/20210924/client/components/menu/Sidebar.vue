<template>
    <div class="sidebar">
        <div class="sidebar-backdrop" @click="closeSidebarPanel" v-if="isPanelOpen"></div>
        <transition name="slide">
            <div v-if="isPanelOpen" class="sidebar-panel">
                <!-- ul 대신 <slot></slot>으로 사용한 다음 앞에서 추가해도됨 -->
                <ul class="sidebar-panel-nav">
                    <li><a @click="onClickRedirect('Home')">HOME</a></li>
                    <li><a @click="onClickRedirect('Ping')">PING</a></li>
                    <li><a @click="onClickRedirect('Books')">BOOKS</a></li>
                    <li><a @click="onClickRedirect('Map')">MAP</a></li>
                    <li><a @click="onClickRedirect('Chart')">CHART</a></li>
                </ul>
            </div>
        </transition>
    </div>
</template>

<script>
import { store, mutations } from '@/store';

export default {
  methods: {
    closeSidebarPanel: mutations.toggleNav,

    onClickRedirect(path) {
      this.$router.push({ name: path });
      mutations.toggleNav();
    },
  },
  computed: {
    isPanelOpen() {
      return store.isNavOpen;
    },
  },
};
</script>

<style>
    .slide-enter-active,
    .slide-leave-active
    {
        transition: transform 0.2s ease;
    }

    .slide-enter,
    .slide-leave-to {
        transform: translateX(-100%);
        transition: all 150ms ease-in 0s
    }

    .sidebar-backdrop {
        background-color: rgba(0,0,0,.5);
        width: 100vw;
        height: 100vh;
        position: fixed;
        top: 0;
        left: 0;
        cursor: pointer;
    }

    .sidebar-panel {
        overflow-y: auto;
        background-color: #ebe8ff;
        position: fixed;
        left: 0;
        top: 0;
        height: 100vh;
        z-index: 999;
        padding: 3rem 20px 2rem 20px;
        width: 300px;
    }

     ul.sidebar-panel-nav {
        list-style-type: none;
    }

    ul.sidebar-panel-nav > li > a{
        color: #000;
        text-decoration: none;
        font-size: 1.5rem;
        display: block;
        padding-bottom: 0.5em;
        cursor: pointer;
    }
</style>
