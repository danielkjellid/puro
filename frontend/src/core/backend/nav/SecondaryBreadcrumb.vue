<template>
  <nav class="items-center hidden text-sm font-medium leading-5 sm:flex">
    <span
      v-for="(breadcrumb, index) in breadcrumbs"
      :key="breadcrumb"
      class="flex"
    >
      <a
        href="#"
        class="text-gray-500 transition duration-150 ease-in-out hover:text-gray-700 focus:outline-none focus:underline"
      >
        {{ breadcrumb }}
      </a>
      <svg
        v-show="index != breadcrumbs.length - 1"
        class="flex-shrink-0 w-5 h-5 mx-2 text-gray-500"
        fill="currentColor"
        viewBox="0 0 20 20"
      >
        <path
          fill-rule="evenodd"
          d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z"
          clip-rule="evenodd"
        />
      </svg>
    </span>
  </nav>
</template>

<script>
export default {
  props: {
    breadcrumbs: {
      type: Array,
      required: true
    }
  }
};
</script>