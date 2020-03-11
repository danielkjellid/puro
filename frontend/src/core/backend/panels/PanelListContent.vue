<template>
    <dl>
        <div class="bg-white px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6" v-for="(d, index) in data" :key="d.fieldName" :class="{'bg-gray-50' : index % 2 === 0}">
            <dt class="text-sm leading-5 font-medium text-gray-500">
                {{ d.fieldName }}
            </dt>
            <dd class="mt-1 text-sm leading-5 text-gray-900 sm:mt-0 sm:col-span-2" v-if="typeof d.fieldValue != 'boolean'">
                {{ d.fieldValue }}
            </dd>
            <dd class="mt-1 flex items-center text-sm leading-5 text-gray-900 sm:mt-0 sm:col-span-2" v-else>
                <svg class="flex-shrink-0 mr-2 h-5 w-5" fill="currentColor" viewBox="0 0 20 20" :class="[d.fieldValue ? 'text-green-400' : 'text-red-400']">
                  <path v-if="d.fieldValue" fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/>
                  <path v-else fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clip-rule="evenodd"/>
                </svg>
                <span v-if="d.fieldValue">Aksepterer {{ d.fieldName.toLowerCase() }}</span>
                <span v-else>Aksepterer ikke {{ d.fieldName.toLowerCase() }}</span>
            </dd>
        </div>
    </dl>
</template>

<script>
export default {
    props: {
        data: {
            type: Array,
            required: true,
        }
    }
}
</script>

<style scoped>
.bg-gray-50 {
  background-color: #f9fafb;
}
</style>