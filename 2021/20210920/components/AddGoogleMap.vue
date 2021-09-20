<template>
  <div>
    <gmap-map
        :zoom="14"    
        :center="center"
        style="width:100%;  height: 600px;"
      >
      <gmap-polygon
      :paths="paths"
      :options="{
        strokeWeight: 0.5
      }">
      </gmap-polygon>
    </gmap-map>
  </div>
</template>
 
<script>
import imgpath from '@/assets/logo.png';
import seoulOutline from '@/Seoul.json';

const outlineSeoul = [];
const wholeWorld = [
    { "lat": -85.1054596961173,   "lng": -180 },
    { "lat": 85.1054596961173,    "lng": -180 },
    { "lat": 85.1054596961173,    "lng": 180 },
    { "lat": -85.1054596961173,   "lng": 180 },
    { "lat": -85.1054596961173,   "lng": 0 }
  ];

var seoul = { lat: 37.5642135 ,lng: 127.0016985 };
export default {
  name: "AddGoogleMap",
  data() {
    return {
      img: {
        url: imgpath,
        scaledSize: { width: 20, height: 20 },
      },
      ani: 4,
      center: seoul,
      locationMarkers:[
          {
              position: seoul
          }
      ],
      paths: [wholeWorld, outlineSeoul],
    };
  },
  created(){
    (seoulOutline.seoul).forEach(element => {
      print(element)
      outlineSeoul.push(element);
    });
  },
};
</script>