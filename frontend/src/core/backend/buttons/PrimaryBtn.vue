<template>
  <span class="shadow-sm rounded-md">
    <button type="button" class="inline-flex items-center px-4 py-2 border border-transparent text-sm leading-5 font-medium rounded-md text-white bg-indigo-500 hover:bg-indigo-400 focus:outline-none focus:shadow-outline-indigo focus:border-indigo-600 active:bg-indigo-600 transition duration-150 ease-in-out">
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