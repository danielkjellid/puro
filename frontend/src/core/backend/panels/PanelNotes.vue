<template>
    <div>
        <div class="flex px-4 py-5">
          <div>
            <span class="inline-flex items-center justify-center w-10 h-10 bg-gray-400 rounded-full">
              <span class="font-medium leading-none text-white text-md">TW</span>
            </span>
          </div>
          <div class="ml-4">
            <h2 class="text-sm font-medium text-gray-900">Emilia Gates</h2>
            <p class="mt-2 text-sm text-gray-600">Tailwind includes a generous palette of great-looking, well-balanced colors that are perfect for prototyping or for kicking off a brand new project.</p>
            <span class="block mt-2 text-xs text-gray-600">4 days ago &#8226; Rediger &#8226; Slett</span>
          </div>
        </div>
        <add-note-form></add-note-form>
    </div>
</template>

<script>
import AddNoteForm from '../forms/AddNoteForm'; 

export default {
    components: {
        'add-note-form': AddNoteForm,
    }
}
</script>

<style>

</style>