<template>
  <div class="flex flex-col">
    <div class="py-2 -my-2 sm:-mx-6 sm:px-6 lg:-mx-8 lg:px-8">
      <div class="inline-block min-w-full overflow-hidden align-middle shadow sm:rounded-lg">
        <table class="min-w-full">
          <thead>
            <tr>
              <th class="px-6 py-3 text-xs font-medium leading-4 tracking-wider text-left text-gray-500 uppercase border-b border-gray-200 bg-gray-50">
                Bruker
              </th>
              <th class="px-6 py-3 text-xs font-medium leading-4 tracking-wider text-left text-gray-500 uppercase border-b border-gray-200 bg-gray-50">
                Endring
              </th>
              <th class="px-6 py-3 text-xs font-medium leading-4 tracking-wider text-left text-gray-500 uppercase border-b border-gray-200 bg-gray-50">
                Dato
              </th>
            </tr>
          </thead>
          <tbody>
            <tr class="bg-white" v-for="index in 5" :key="index">
              <td class="px-6 py-4 text-sm leading-5 text-gray-900 whitespace-no-wrap">
                Daniel Kjellid
              </td>
              <td class="px-6 py-4 text-sm leading-5 text-gray-900">
                <span class="px-1 py-1 text-red-800 bg-red-100">first_name</span> endret fra <span class="px-1 py-1 text-red-800 bg-red-100">Test</span> til <span class="px-1 py-1 text-red-800 bg-red-100">Test123</span>
              </td>
              <td class="px-6 py-4 text-sm leading-5 text-gray-900 whitespace-no-wrap">
                28. Desember 2019 21:15
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
export default {

}
</script>

<style>

</style>