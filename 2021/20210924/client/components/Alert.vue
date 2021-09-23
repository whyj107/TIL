<template>
<div>
    <b-alert variant="성공" show>{{ message }}</b-alert>
    <br>
</div>
</template>

<script>
export default {
  props: ['message'],
};
</script>
