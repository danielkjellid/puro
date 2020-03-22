<template>
  <div>
    <div class="sticky top-0 z-10">
      <core-header></core-header>
      <div class="sticky top-0 z-10 bg-white shadow">
        <div class="container px-8 mx-auto">
          <div class="flex items-center justify-between py-5">
            <div>
              <div>
                <!-- breadcrumb -->
                <slot name="detail-breadcrumb"></slot>
              </div>
              <div class="flex items-center mt-3">
                <!-- title of page, usually paired with image and metadata -->
                <slot name="detail-title"></slot>
              </div>
            </div>
            <div>
              <!-- action buttons -->
              <slot name="detail-actions"></slot>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- Main content -->
    <div class="container px-6 py-6 mx-auto">
      <div class="grid grid-cols-4 gap-5">
        <div class="col-span-1">
          <!-- page navigation -->
          <slot name="detail-page-navigation"></slot>
        </div>
        <div class="col-span-3">
          <div>
            <!-- content of page, usually in the shape of panels -->
            <slot name="detail content"></slot>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Header from "../nav/TheHeader";

export default {
  components: {
    "core-header": Header
  }
};
</script>

<style></style>
