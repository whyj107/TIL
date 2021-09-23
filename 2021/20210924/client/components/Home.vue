<template>
  <div class="container">
    <br>
    <div class="btn-group" role="group">
        <button type="button" class="btn btn-primary"
        @click="onClickRedirect(locationPing)">1. Ping</button>
        <br>
        <button type="button" class="btn btn-secondary"
        @click="onClickRedirect(locationBooks)">2. Books</button>
        <br>
        <button type="button" class="btn btn-success"
        @click="onClickRedirect(locationMap)">3. Map</button>
        <br>
        <button type="button" class="btn btn-light"
        @click="onClickRedirect(locationChart)">4. Chart</button>
    </div>
    <br>
  </div>
</template>

<script>
export default {
  data() {
    return {
      locationBooks: 'Books',
      locationMap: 'Map',
      locationPing: 'Ping',
      locationChart: 'Chart',
    };
  },
  methods: {
    onClickRedirect(btnPath) {
      this.$router.push({ name: btnPath });
    },
  },
};
</script>
