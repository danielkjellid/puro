<template>
  <div class="flex items-center w-full">
    <div class="w-full">
      <label :for="label" class="sr-only">{{ label }}</label>
      <div class="relative rounded-md shadow-sm">
        <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
          <svg class="h-5 w-5 text-gray-400" fill="currentColor" viewBox="0 0 20 20">
            <path fill-rule="evenodd" :d="iconPath" clip-rule="evenodd"/>
          </svg>
        </div>
        <input :id="label" class="form-input block w-full pl-10 sm:text-sm sm:leading-5" :placeholder="placeHolder" />
      </div>
    </div>
    <div>
      <span class="ml-3">
        <core-buttons-primary-btn :text="btnText"></core-buttons-primary-btn>
      </span>
    </div>
  </div>
</template>

<script>
import BackendPrimaryBtn from '../../buttons/PrimaryBtn.vue'

export default {
    props: {
        label: {
            type: String,
            required: true,
        },
        iconPath: {
            type: String,
            required: true,
        },
        placeHolder: {
            type: String,
            required: true,
        },
        btnText: {
            type: String,
            required: true,
          },
    },
    components: {
        'core-buttons-primary-btn': BackendPrimaryBtn
    }
}
</script>

<style>

</style>