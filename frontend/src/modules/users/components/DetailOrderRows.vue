<template>
<!-- <tr v-for="(d, index) in data" :key="d.name" :class="{'bg-gray-50 : index % 2 === 0}"> -->
  <tr>
      <td class="px-6 py-4 whitespace-no-wrap">
      <div class="flex items-center">
          <div class="flex-shrink-0 w-10 h-10">
          <img class="w-10 h-10 rounded-full" src="https://images.unsplash.com/photo-1532910404247-7ee9488d7292?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="" />
          </div>
          <div class="ml-4">
          <div class="text-sm font-medium leading-5 text-gray-900">Ikon</div>
          <div class="text-sm leading-5 text-gray-500">Sky gray</div>
          </div>
      </div>
      </td>
      <td class="px-6 py-4 whitespace-no-wrap">
      <div class="text-sm leading-5 text-gray-900">20x1m2</div>
      <div class="text-sm leading-5 text-gray-500">120x100cm</div>
      </td>
      <td class="px-6 py-4 text-sm leading-5 text-gray-900 whitespace-no-wrap">
      9980,00kr
      </td>
      <td class="px-6 py-4 whitespace-no-wrap">
      <span class="inline-flex px-2 text-xs font-semibold leading-5 text-green-800 bg-green-100 rounded-full">
          Tilbud sendt
      </span>
      </td>
      <td class="px-6 py-4 text-sm font-medium leading-5 text-right whitespace-no-wrap">
      <a href="#" class="text-indigo-600 hover:text-indigo-900 focus:outline-none focus:underline">Behandle</a>
      </td>
  </tr>
</template>

<script>
export default {

}
</script>

<style>

</style>