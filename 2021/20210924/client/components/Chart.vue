<template>
  <div class="container">
    <h1>Chart 예제</h1>
    <br>
    <div>
      <h3>Line Chart</h3>
      <line-chart></line-chart>
    </div>
    <br>
    <div>
      <h3>Bar Chart</h3>
      <bar-chart></bar-chart>
    </div>
    <br>
    <div>
      <h3>Bubble Chart</h3>
      <bubble-chart></bubble-chart>
    </div>
    <br>
    <div>
      <h3>Reactive Chart</h3>
      <reactive-chart :chart-data="datacollection"></reactive-chart>
      <button class="btn btn-primary" @click="fillData()">Randomize</button>
    </div>
    <br>
    <br>
  </div>
</template>

<script>
import LineChart from './chart/LineChart.vue';
import BarChart from './chart/BarChart.vue';
import BubbleChart from './chart/BubbleChart.vue';
import ReactiveChart from './chart/ReactiveChart.vue';

export default {
  name: 'Chart',
  components: {
    LineChart,
    BarChart,
    BubbleChart,
    ReactiveChart,
  },
  data() {
    return {
      datacollection: null,
    };
  },
  created() {
    this.fillData();
  },
  methods: {
    onClickRedirect() {
      this.$router.replace({ name: 'Home' });
    },
    fillData() {
      this.datacollection = {
        labels: ['1월', '2월', '3월', '4월', '5월', '6월', '7월', '8월', '9월', '10월', '11월', '12월'],
        datasets: [
          {
            label: 'Random',
            backgroundColor: '#ebe8ff',
            data: [this.getRandomInt(), this.getRandomInt(), this.getRandomInt(),
              this.getRandomInt(), this.getRandomInt(), this.getRandomInt(),
              this.getRandomInt(), this.getRandomInt(), this.getRandomInt(),
              this.getRandomInt(), this.getRandomInt(), this.getRandomInt()],
          },
        ],
      };
    },
    getRandomInt() {
      return Math.floor(Math.random() * 10);
    },
  },
};

</script>
