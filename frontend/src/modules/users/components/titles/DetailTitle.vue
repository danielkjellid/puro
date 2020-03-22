<template>
  <div class="flex items-center mt-3">
      <span class="inline-flex items-center justify-center w-12 h-12 bg-gray-400 rounded-full">
        <span class="text-lg font-medium leading-none text-white">DK</span>
      </span>
      <div class="ml-3">
        <h1 class="text-xl font-medium leading-6 text-gray-900">
          {{ fullName }}
        </h1>
        <div v-if="verified" class="flex items-center text-sm leading-5 text-gray-500">
          <svg class="flex-shrink-0 w-5 h-5 mr-1 text-green-400" fill="currentColor" viewBox="0 0 20 20">
            <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/>
          </svg>
          Verifisert konto
        </div>
        <div v-else class="flex items-center text-sm leading-5 text-gray-500">
          <svg class="flex-shrink-0 w-5 h-5 mr-1 text-red-400" fill="currentColor" viewBox="0 0 20 20">
            <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clip-rule="evenodd"/>
          </svg>
          Ikke verifisert
        </div>
      </div>
  </div>
</template>

<script>
export default {
    props: {
        initials: {
            type: String,
            required: true,
            default: 'AB',
        },
        fullName: {
            type: String,
            required: true,
            default: 'fullName',
        },
        verified: {
            type: Boolean,
            required: true,
            default: false,
        }
    }
}
</script>