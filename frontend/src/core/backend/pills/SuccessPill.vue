<template>
  <span class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800">
    {{ text }}
  </span>
</template>

<script>
export default {
    props: {
        text: {
            type: String,
            required: true,
        }
    }
}
</script>