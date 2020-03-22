<template>
    <div>
        <div class="sticky top-0 z-10">
            <core-nav-header></core-nav-header>
        </div>
        <div class="pb-32 bg-gray-800">
            <core-overview-header :title="title">
                <template v-slot:secondary-action>
                    <slot name="overview-header-secondary-action"></slot>
                </template>
                <template v-slot:primary-action>
                    <slot name="overview-header-primary-action"></slot>
                </template>
            </core-overview-header>
        </div>
        <main class="-mt-32">
        <div class="px-8 pb-12 mx-auto max-w-7xl">
            <div class="overflow-hidden bg-white rounded-md shadow">
            <core-overview-table :tableHeads="tableHeads">
                <template v-slot:table-rows>
                    <slot name="overview-table-rows"></slot>
                </template>
            </core-overview-table>
            </div>
        </div>
        </main>
    </div>
</template>

<script>
import Header from '../nav/TheHeader'
import OverviewHeader from '../headers/OverviewHeader'
import OverviewTable from '../tables/OverviewTable'

export default {
    props: {
        title: {
            type: String,
            requires: true,
        },
        tableHeads: {
            type: Array,
            required: true,
        }
    },
    components: {
        'core-nav-header': Header,
        'core-overview-header': OverviewHeader,
        'core-overview-table': OverviewTable,
    }
}
</script>

<style>

</style>