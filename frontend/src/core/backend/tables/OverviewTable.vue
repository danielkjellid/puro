<template>
  <div class="overflow-hidden bg-white rounded-md shadow">
    <div class="px-4 py-5 bg-white border-b border-gray-200 sm:px-6">
      <core-forms-input-icon-btn :label="'search'" :iconPath="'M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z'" :placeHolder="'Søk...'" :btnText="'Søk'"></core-forms-input-icon-btn>
    </div>
    <div class="flex flex-col">
      <div class="py-2 -my-2 overflow-x-auto sm:-mx-6 sm:px-6 lg:-mx-8 lg:px-8">
        <div class="inline-block min-w-full overflow-hidden align-middle border-b border-gray-200 shadow sm:rounded-lg">
          <table class="min-w-full">
            <thead>
              <tr>
                <th class="px-6 py-3 text-xs font-medium leading-4 tracking-wider text-left text-gray-500 uppercase bg-gray-100 border-b border-gray-200" v-for="tableHead in tableHeads" :key="tableHead">
                  {{ tableHead }}
                </th>
                <th class="px-6 py-3 bg-gray-100 border-b border-gray-200"></th>
              </tr>
            </thead>
            <tbody class="bg-white">
              <slot name="table-rows"></slot>
            </tbody>
          </table>
          <div class="px-6 py-4">
            <core-pagination></core-pagination>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import InputGroupIconAndBtn from '../inputs/IconAndBtn.vue'
import Pagination from '../pagination/Pagination.vue'

export default {
  props: {
    tableHeads: {
      type: Array,
      required: true,
    }
  },
  components: {
    'core-forms-input-icon-btn': InputGroupIconAndBtn,
    'core-pagination': Pagination,
  }
}
</script>

<style>

</style>