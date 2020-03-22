<template>
  <nav class="bg-gray-800">
    <div class="container px-8 mx-auto max-w-7xl">
      <div class="border-b border-gray-700">
        <div class="flex items-center justify-between h-16 px-0">
          <div class="flex items-center">
            <div class="flex-shrink-0">
              <img class="w-8 h-8" src="https://tailwindui.com/img/logos/workflow-mark-on-dark.svg" alt="" />
            </div>
            <div class="block">
              <div class="flex items-baseline ml-10">
                <router-link to="/users" active-class="bg-gray-900" class="px-3 py-2 text-sm font-medium text-white rounded-md focus:outline-none focus:text-white focus:bg-gray-700">
                  <a>Brukere</a>
                </router-link>
                <a href="#" class="px-3 py-2 ml-4 text-sm font-medium text-gray-300 rounded-md hover:text-white hover:bg-gray-700 focus:outline-none focus:text-white focus:bg-gray-700">Inventar</a>
                <a href="#" class="px-3 py-2 ml-4 text-sm font-medium text-gray-300 rounded-md hover:text-white hover:bg-gray-700 focus:outline-none focus:text-white focus:bg-gray-700">Markedsføring</a>
                <a href="#" class="px-3 py-2 ml-4 text-sm font-medium text-gray-300 rounded-md hover:text-white hover:bg-gray-700 focus:outline-none focus:text-white focus:bg-gray-700">Forespørsler</a>
                <a href="#" class="px-3 py-2 ml-4 text-sm font-medium text-gray-300 rounded-md hover:text-white hover:bg-gray-700 focus:outline-none focus:text-white focus:bg-gray-700">Rapporter</a>
              </div>
            </div>
          </div>
          <div class="flex items-center ml-4">
            <div class="relative ml-3">
              <div>
                <button @click="dropdownOpen = !dropdownOpen" class="flex items-center max-w-xs text-sm text-white rounded-full focus:outline-none focus:shadow-solid">
                  <span class="inline-flex items-center justify-center w-10 h-10 bg-gray-900 rounded-full">
                    <span class="font-medium leading-none text-white text-md">DK</span>
                  </span>
                </button>
              </div>
              <div v-show="dropdownOpen" class="absolute right-0 z-20 w-48 mt-2 origin-top-right rounded-md shadow-lg">
                <div class="py-1 bg-white rounded-md shadow-xs">
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