<template>
  <div>
    <gmap-map
        id="gmap"
        :zoom="zoom"
        :center="center"
        :options="{
          disableDefaultUI: true,
          maxZoom: 15,
          minZoom: 11,
        }"
        style="width:100vw;  height: 100vh;"
      >

      <gmap-polygon
        :paths="paths"
        :options="{
          strokeWeight: 0.5
        }"
        ></gmap-polygon>

      <gmap-marker
        :icon=img
        v-for="(m, index) in markers"
        :key="index"
        :position="m.position"
        @click="doMouseClick(m)"
        :description="m.description"
        @mouseover="doMouseOver(m, index)"
        @mouseout="stopMouseOver(m)"
      >
      </gmap-marker>

      <gmap-info-window
            @closeclick="window_open=false"
            :opened="window_open"
            :position="infoPosition"
            :options="infoOptions">
      </gmap-info-window>
    </gmap-map>
  </div>
</template>

<script>
/* eslint no-param-reassign: "error" */
import { gmapApi } from 'vue2-google-maps';
import imgpath from '@/assets/logo.png';
import outlinepath from '@/outline.json';
// Mark
// var company = { lat: 35.21488, lng: 128.83616 };
// var seoul = { lat: 37.5642135, lng: 127.0016985 };
const changwon = { lat: 35.228047926028935, lng: 128.68180774290053 };
const sample = [
  { position: changwon, description: '창원시청' },
  { position: { lat: 35.22979214251197, lng: 128.68253313076977 }, description: '창원문화예술회관' },
];
// --------------------------------------------------------------------------

// OutLine
const wholeWorld = [];
const changwonOutline = [];

// --------------------------------------------------------------------------

export default {
  name: 'AddGoogleMap',
  computed: {
    google: gmapApi,
  },
  data() {
    return {
      zoom: 15,
      center: changwon,
      markers: sample,
      paths: [wholeWorld, changwonOutline],
      img: {
        url: imgpath,
        scaledSize: { width: 20, height: 20 },
      },
      info_marker: null,
      infowindow: changwon,
      infoPosition: null,
      infoContent: null,
      infoOptions: {
        pixelOffset: {
          width: 0,
          height: -35,
        },
        maxWidth: 200,
        content: null,
      },
      window_open: false,
      currentMidx: null,
      auto_reload_delay: 1 * 1000, // 인터벌 시간
      auto_reload_func: null, // 인터벌 함수 담을 곳
    };
  },
  mounted() {
  },
  created() {
    (outlinepath.wholeWorld).forEach((element) => {
      wholeWorld.push(element);
    });

    (outlinepath.changwonOutline).forEach((element) => {
      changwonOutline.push(element);
    });

    // setInterval 시작
    this.auto_reload_func = setInterval(() => {
      const now = new Date();
      // eslint-disable-next-line
      console.log(now);
    }, this.auto_reload_delay);
  },
  destroyed() {
    // setInterval 종료
    clearInterval(this.auto_reload_func);
  },
  methods: {
    onClickRedirect() {
      this.$router.replace({ name: 'Home' });
    },
    getPosition(marker) {
      return {
        lat: parseFloat(marker.position.lat),
        lng: parseFloat(marker.position.lng),
      };
    },
    doMouseOver(marker, idx) {
      // Bounce
      // marker.anima="1"

      this.infoPosition = this.getPosition(marker);
      this.infoOptions.content = `<div><div>${marker.description}</div><div><p>위도: ${marker.position.lat}</p><p>경도: ${marker.position.lng}</p></div></div>`;
      if (this.currentMidx === idx) {
        this.window_open = !this.window_open;
      } else {
        this.window_open = true;
        this.currentMidx = idx;
      }
    },
    stopMouseOver(marker) {
      // Stop
      // this.animation=""
      this.window_open = false;
      // eslint-disable-next-line
      console.log(marker);
    },
    doMouseClick(marker) {
      this.center = marker.position;
    },
  },
};
</script>
