<template>
  <div class="flex flex-col">
    <div class="py-2 -my-2 sm:-mx-6 sm:px-6 lg:-mx-8 lg:px-8">
        <div class="inline-block min-w-full overflow-hidden align-middle shadow sm:rounded-lg">
        <table class="min-w-full">
            <thead>
            <tr>
                <th class="px-6 py-3 text-xs font-medium leading-4 tracking-wider text-left text-gray-500 uppercase border-b border-gray-200 bg-gray-50" v-for="tableHead in tableHeads" :key="tableHead">
                {{ tableHead }}
                </th>
                <th class="px-6 py-3 border-b border-gray-200 bg-gray-50"></th>
            </tr>
            </thead>
            <tbody class="bg-white">
                <slot name="panel-table-rows"></slot>
            </tbody>
        </table>
        </div>
    </div>
  </div>
</template>

<script>
export default {
    props: {
        tableHeads: {
            type: Array,
            required: true,
        }
    }
}
</script>

<style>

</style>