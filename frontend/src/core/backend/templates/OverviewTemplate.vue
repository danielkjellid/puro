<template>
    <div>
        <div class="bg-gray-800 pb-32">
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
        <div class="max-w-7xl mx-auto pb-12 px-8">
            <div class="bg-white shadow overflow-hidden rounded-md">
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
        'core-overview-header': OverviewHeader,
        'core-overview-table': OverviewTable,
    }
}
</script>

<style>

</style>