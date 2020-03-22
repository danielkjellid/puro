<template>
  <nav>
    <a v-for="link in  links" :key="link" :href="link.to" class="flex items-center px-3 py-2 text-sm font-medium leading-5 text-gray-600 transition duration-150 ease-in-out rounded-md group hover:text-gray-900 hover:bg-gray-100 focus:outline-none focus:text-gray-900 focus:bg-gray-200">
      <svg class="flex-shrink-0 w-6 h-6 mr-3 -ml-1 text-gray-400 transition duration-150 ease-in-out group-hover:text-gray-500 group-focus:text-gray-600" stroke="currentColor" fill="none" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" :d="link.icon"/>
      </svg>
      <span class="truncate">
        {{ link.title }}
      </span>
    </a>
  </nav>
</template>

<script>
export default {
    props: {
        links: {
            type: Array,
            required: true,
        }
    }

}
</script>

<style>

</style>