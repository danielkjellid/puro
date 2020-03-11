<template>
  <div class="bg-white shadow overflow-hidden rounded-md">
    <div class="bg-white px-4 py-5 border-b border-gray-200 sm:px-6">
      <core-forms-input-icon-btn :label="'search'" :iconPath="'M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z'" :placeHolder="'Søk...'" :btnText="'Søk'"></core-forms-input-icon-btn>
    </div>
    <div class="flex flex-col">
      <div class="-my-2 py-2 overflow-x-auto sm:-mx-6 sm:px-6 lg:-mx-8 lg:px-8">
        <div class="align-middle inline-block min-w-full shadow overflow-hidden sm:rounded-lg border-b border-gray-200">
          <table class="min-w-full">
            <thead>
              <tr>
                <th class="px-6 py-3 border-b border-gray-200 bg-gray-100 text-left text-xs leading-4 font-medium text-gray-500 uppercase tracking-wider" v-for="tableHead in tableHeads" :key="tableHead">
                  {{ tableHead }}
                </th>
                <th class="px-6 py-3 border-b border-gray-200 bg-gray-100"></th>
              </tr>
            </thead>
            <tbody class="bg-white">
              <slot name="table-rows"></slot>
            </tbody>
          </table>
          <div class="py-4 px-6">
            <core-pagination></core-pagination>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import InputGroupIconAndBtn from '../forms/input-groups/IconAndBtn.vue'
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