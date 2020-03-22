<template>
  <div class="flex items-center w-full">
    <div class="w-full">
      <label :for="label" class="sr-only">{{ label }}</label>
      <div class="relative rounded-md shadow-sm">
        <div class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
          <svg class="w-5 h-5 text-gray-400" fill="currentColor" viewBox="0 0 20 20">
            <path fill-rule="evenodd" :d="iconPath" clip-rule="evenodd"/>
          </svg>
        </div>
        <input :id="label" class="block w-full pl-10 form-input sm:text-sm sm:leading-5" :placeholder="placeHolder" />
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
import PrimaryBtn from '../buttons/PrimaryBtn'

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
        'core-buttons-primary-btn': PrimaryBtn
    }
}
</script>

<style>

</style>