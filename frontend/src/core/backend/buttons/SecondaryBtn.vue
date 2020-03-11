<template>
  <span class="shadow-sm rounded-md">
    <button type="button" class="inline-flex items-center px-4 py-2 border border-transparent text-sm leading-5 font-medium rounded-md text-white bg-gray-600 hover:bg-gray-500 focus:outline-none focus:shadow-outline-gray focus:border-gray-700 active:bg-gray-700 transition duration-150 ease-in-out">
      {{ text }}
    </button>
  </span>
</template>

<script>
export default {
    props: {
        text: {
            type: String,
            required: true,
        },
    }
}
</script>