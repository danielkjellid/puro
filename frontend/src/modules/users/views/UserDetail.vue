<template>
    <core-detail-template>
        <template v-slot:detail-breadcrumb>
            <p>Test</p>
        </template>
    </core-detail-template>
</template>

<script>
// core imports
import DetailTemplate from '../../../core/backend/templates/DetailTemplate'


export default {
    components: { 
        'core-detail-template': DetailTemplate,
    }
}
</script>

<style>

</style>