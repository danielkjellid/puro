<template>
  <tr>
    <td class="px-6 py-4 whitespace-no-wrap border-b border-gray-200">
      <div class="flex items-center">
        <div class="flex-shrink-0 h-10 w-10">
          <span class="inline-flex items-center justify-center h-10 w-10 rounded-full bg-gray-400">
            <span class="text-md font-medium leading-none text-white">TW</span>
          </span>
        </div>
        <div class="ml-4">
          <div class="text-sm leading-5 font-medium text-gray-900">Bernard Lane</div>
          <div class="text-sm leading-5 text-gray-500">Utvikler</div>
        </div>
      </div>
    </td>
    <td class="px-6 py-4 whitespace-no-wrap border-b border-gray-200">
      <div class="text-sm leading-5 text-gray-900">ted.woods@example.com</div>
      <div class="text-sm leading-5 text-gray-500">+47 123 45 678</div>
    </td>
    <td class="px-6 py-4 whitespace-no-wrap border-b border-gray-200">
      <div class="text-sm leading-5 text-gray-900">Adressegate 1</div>
      <div class="text-sm leading-5 text-gray-500">0485 Oslo</div>
    </td>
    <td class="px-6 py-4 whitespace-no-wrap border-b border-gray-200">
      <core-pills-success-pill :text="'Aktiv'"></core-pills-success-pill>
    </td>
    <td class="px-6 py-4 whitespace-no-wrap text-right border-b border-gray-200 text-sm leading-5 font-medium">
      <a href="#" class="text-indigo-600 hover:text-indigo-900 focus:outline-none focus:underline">Rediger</a>
    </td>
  </tr>
</template>

<script>
import SuccessPill from '../../../core/backend/pills/SuccessPill'

export default {
  components: {
    'core-pills-success-pill': SuccessPill,
  }
}
</script>

<style>

</style>