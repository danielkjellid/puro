<template>
  <div>
    <core-overview-template :title="'Brukere'" :tableHeads="['Navn', 'Kontakt', 'Adresse', 'Status']">
        <template v-slot:overview-header-secondary-action>
            <core-buttons-secondary-btn :text="'Eksporter'"></core-buttons-secondary-btn>
        </template>
        <template v-slot:overview-header-primary-action>
            <core-buttons-primary-btn :text="'Ny bruker'"></core-buttons-primary-btn>
        </template>
        <template v-slot:overview-table-rows>
            <users-users-rows v-for="index in 5" :key="index"></users-users-rows>
        </template>
    </core-overview-template>   
  </div>
</template>

<script>
// core imports
import OverviewTemplate from '../../../core/backend/templates/OverviewTemplate'
import PrimaryBtn from '../../../core/backend/buttons/PrimaryBtn'
import SecondaryBtn from '../../../core/backend/buttons/SecondaryBtn'

// module imports
import UsersRows from '../components/OverviewTableRow'

export default {
    components: {
        'core-overview-template': OverviewTemplate,
        'core-buttons-primary-btn': PrimaryBtn,
        'core-buttons-secondary-btn': SecondaryBtn,
        'users-users-rows': UsersRows,
    }
}
</script>

<style>

</style>