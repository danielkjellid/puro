<template>
  <header class="py-10">
    <div class="px-4 px-8 mx-auto max-w-7xl">
      <div>
        <div>
        </div>
        <div class="mt-2 md:flex md:items-center md:justify-between">
          <div class="flex-1 min-w-0">
            <h2 class="text-2xl font-bold leading-7 text-white sm:text-3xl sm:leading-9 sm:truncate">
              {{ title }}
            </h2>
          </div>
          <div class="flex flex-shrink-0 mt-4 md:mt-0 md:ml-4">
            <slot name="secondary-action"></slot>
            <span class="ml-3">
                <slot name="primary-action"></slot>
            </span>
          </div>
        </div>
      </div>
    </div>
  </header>
</template>

<script>

export default {
    props: {
        title: {
            type: String,
            required: true,
        }
    },
    components: {
    }
}
</script>