<template>
  <span class="relative z-0 inline-flex shadow-sm">
    <button
      type="button"
      v-for="(btn, index) in btns"
      :key="index"
      :class="{
        'rounded-l-md': index === 0,
        'rounded-r-md': index === btns.length - 1,
        '-ml-px': index === btns.length - 1,
        '-ml-px': index != 0
      }"
      class="relative inline-flex items-center px-4 py-2 border border-gray-300 bg-white text-sm leading-5 font-medium text-gray-700 hover:text-gray-500 focus:z-10 focus:outline-none focus:border-blue-300 focus:shadow-outline-blue active:bg-gray-100 active:text-gray-800 transition ease-in-out duration-150"
    >
      {{ btn }}
    </button>
  </span>
</template>

<script>
export default {
  props: {
    btns: {
      type: Array,
      required: true
    }
  }
};
</script>

<style></style>
