<template>
  <form class="px-4 py-5 bg-gray-50">
    <div>
      <label for="add-note" class="block text-sm font-medium leading-5 text-gray-700">Add a note</label>
      <div class="relative mt-1 rounded-md shadow-sm">
        <textarea id="add-note" class="block w-full form-input sm:text-sm sm:leading-5" rows="3"/>
      </div>
      <div class="flex justify-end mt-4">
        <primary-btn :text="'Legg til notat'"></primary-btn>
      </div>
    </div>
  </form>
</template>

<script>
import PrimaryBtn from '../buttons/PrimaryBtn';

export default {
    components: {
        'primary-btn': PrimaryBtn,
    }
}
</script>

<style>

</style>