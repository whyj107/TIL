<template>
  <div class="container">
    <button type="button" class="btn btn-primary" @click="onClickRedirect">{{ msg }}</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Ping',
  data() {
    return {
      msg: '',
    };
  },
  methods: {
    getMessage() {
      const path = 'http://192.168.0.64:5000/ping';
      axios
        .get(path)
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    onClickRedirect() {
      this.$router.replace({ name: 'Home' });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>
