<template>
  <div class="bg-white shadow overflow-hidden sm:rounded-lg ">
    <div class="bg-white px-4 py-5 sm:px-6 border-b border-gray-200">
      <div class="-ml-4 -mt-4">
        <div class="ml-4 mt-4">
          <h3 class="text-lg leading-6 font-medium text-gray-900">
            {{ panelTitle }}
          </h3>
          <p class="mt-1 text-sm leading-5 text-gray-500">
            {{ panelSubtitle }}
          </p>
        </div>
      </div>
    </div>
    <div>
      <!-- panel content -->
      <slot name="panel-content"></slot>
    </div>
  </div>
</template>

<script>
export default {
    props: {
        panelTitle: {
            type: String,
            required: true,
        },
        panelSubtitle: {
            type: String,
            required: true,
        }
    }
}
</script>

<style>

</style>