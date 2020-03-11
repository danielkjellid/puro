<template>
  <nav class="bg-gray-800">
    <div class="max-w-7xl mx-auto px-8">
      <div class="border-b border-gray-700">
        <div class="flex items-center justify-between h-16 px-0">
          <div class="flex items-center">
            <div class="flex-shrink-0">
              <img class="h-8 w-8" src="https://tailwindui.com/img/logos/workflow-mark-on-dark.svg" alt="" />
            </div>
            <div class="block">
              <div class="ml-10 flex items-baseline">
                <a href="#" class="px-3 py-2 rounded-md text-sm font-medium text-white bg-gray-900 focus:outline-none focus:text-white focus:bg-gray-700">Brukere</a>
                <a href="#" class="ml-4 px-3 py-2 rounded-md text-sm font-medium text-gray-300 hover:text-white hover:bg-gray-700 focus:outline-none focus:text-white focus:bg-gray-700">Inventar</a>
                <a href="#" class="ml-4 px-3 py-2 rounded-md text-sm font-medium text-gray-300 hover:text-white hover:bg-gray-700 focus:outline-none focus:text-white focus:bg-gray-700">Markedsføring</a>
                <a href="#" class="ml-4 px-3 py-2 rounded-md text-sm font-medium text-gray-300 hover:text-white hover:bg-gray-700 focus:outline-none focus:text-white focus:bg-gray-700">Forespørsler</a>
                <a href="#" class="ml-4 px-3 py-2 rounded-md text-sm font-medium text-gray-300 hover:text-white hover:bg-gray-700 focus:outline-none focus:text-white focus:bg-gray-700">Rapporter</a>
              </div>
            </div>
          </div>
          <div class="ml-4 flex items-center">
            <div class="ml-3 relative">
              <div>
                <button @click="dropdownOpen = !dropdownOpen" class="max-w-xs flex items-center text-sm rounded-full text-white focus:outline-none focus:shadow-solid">
                  <span class="inline-flex items-center justify-center h-10 w-10 rounded-full bg-gray-900">
                    <span class="text-md font-medium leading-none text-white">DK</span>
                  </span>
                </button>
              </div>
              <div v-show="dropdownOpen" class="origin-top-right absolute right-0 mt-2 w-48 rounded-md shadow-lg z-10">
                <div class="py-1 rounded-md bg-white shadow-xs">
                  <a href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100">Min konto</a>
                  <a href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100">Gå til front</a>
                  <a href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100">Logg ut</a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  data() {
    return {
      dropdownOpen: false,
    }
  }
}
</script>