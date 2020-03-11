<template>
  <header class="py-10">
    <div class="max-w-7xl mx-auto px-4 px-8">
      <div>
        <div>
          <nav class="hidden sm:flex items-center text-sm leading-5 font-medium">
            <a href="#" class="text-gray-400 hover:text-gray-200 focus:outline-none focus:underline transition duration-150 ease-in-out">Brukere</a>
            <svg class="flex-shrink-0 mx-2 h-5 w-5 text-gray-500" fill="currentColor" viewBox="0 0 20 20">
              <path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clip-rule="evenodd"/>
            </svg>
            <a href="#" class="text-gray-400 hover:text-gray-200 focus:outline-none focus:underline transition duration-150 ease-in-out">Oversikt</a>
          </nav>
        </div>
        <div class="mt-2 md:flex md:items-center md:justify-between">
          <div class="flex-1 min-w-0">
            <h2 class="text-2xl font-bold leading-7 text-white sm:text-3xl sm:leading-9 sm:truncate">
              {{ title }}
            </h2>
          </div>
          <div class="mt-4 flex-shrink-0 flex md:mt-0 md:ml-4">
            <slot name="secondary-action"></slot>
            <span class="ml-3">
                <slot name="primary-action"></slot>
            </span>
          </div>
        </div>
      </div>
    </div>
  </header>
</template>

<script>
export default {
    props: {
        title: {
            type: String,
            required: true,
        }
    }
}
</script>