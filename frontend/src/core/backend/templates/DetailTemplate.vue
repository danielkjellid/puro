<template>
  <div>
    <div class="sticky top-0 z-10">
      <core-nav-header></core-nav-header>
      <div class="sticky top-0 z-10 bg-white shadow">
        <div class="container px-8 mx-auto">
          <div class="flex items-center justify-between py-5">
            <div>
              <div>
                <!-- page breadcrumbs -->
                <!-- takes an array of objects, containing properties title and to -->
                <core-nav-breadcrumb :breadcrumbs="breadcrumbs"></core-nav-breadcrumb>
              </div>
              <div>
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
            <slot name="detail-content"></slot>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// CORE IMPORTS
// - nav imports
import Header from "../nav/TheHeader"
import Breadcrumb from '../nav/Breadcrumb'

export default {
  props: {
    breadcrumbs: {
      type: Array,
      required: true,
    }
  },
  components: {
    "core-nav-header": Header,
    'core-nav-breadcrumb': Breadcrumb,
  }
};
</script>

<style></style>
