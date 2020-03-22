<template>
    <core-detail-template>
        <!-- detail page breadcrumbs -->
        <template v-slot:detail-breadcrumb>
            <!-- page breadcrumbs -->
            <!-- takes an array of objects, containing properties title and to -->
            <core-nav-secondary-breadcrumb :breadcrumbs="['Brukere', 'Daniel Kjellid']"></core-nav-secondary-breadcrumb>
        </template>

        <!-- detail page title -->
        <template v-slot:detail-title>
            <!-- user detail title -->
            <!-- takes strings 'initials' and 'fullName', and a boolean 'verified' as props -->
            <users-detail-title :initials="'DK'" :fullName="'Daniel Kjellid'" :verified="true" ></users-detail-title>
        </template>

        <!-- detail page action buttons -->
        <template v-slot:detail-actions>
            <core-buttons-tertiary-btn-group
              :btns="['Send e-post', 'Notat', 'Rediger', 'Eksporter']"
            ></core-buttons-tertiary-btn-group>
            <span class="ml-3">
              <core-buttons-primary-btn :text="'Logg inn som'"></core-buttons-primary-btn>
            </span>
        </template>

        <!-- detail page navigation -->
        <template v-slot:detail-page-navigation>
            <!-- displays navigation on the left -->
            <!-- Takes an array of objects, containing properties title, to (link to #) and icon (path of svg -->
            <core-nav-pagenav :links="pageNav"></core-nav-pagenav>
        </template>

        <!-- detail page content -->
        <template v-slot:detail-content>
            <!-- user overview -->
            <!-- default panel -->
            <!-- takes strings as props panelTitle and panelSubtitle -->
            <!-- adds a slot to insert content -->
            <core-panels-panel :panelTitle="'Oversikt'" :panelSubtitle="'Personlig informasjon om bruker'">
              <template v-slot:panel-content>
                <!-- panel-list content type which shows a list of data -->
                <!-- takes an array of objects, containing properties fieldName and fieldValue -->
                <core-panels-panel-list :data="userData"></core-panels-panel-list>
              </template>
            </core-panels-panel>
            
            <!-- orders overview -->
            <core-panels-panel :panelTitle="'Forespørsler'" :panelSubtitle="'Forespørsler brukeren har gjort'" class="mt-12">
              <template v-slot:panel-content>
                <!-- panel-table sets up a table and takes strings as props tableHeads -->
                <core-panels-panel-table :tableHeads="['Produkt', 'Antall', 'Sum', 'Status']">
                  <!-- slot for inserting module specific tabledata -->
                  <template v-slot:panel-table-rows>
                    <users-order-rows v-for="index in 5" :key="index"></users-order-rows>
                  </template>
                </core-panels-panel-table>
              </template>
            </core-panels-panel>

            <!-- user notes -->
            <core-panels-panel :panelTitle="'Notater'" :panelSubtitle="'Notater om bruker'" class="mt-12">
              <template v-slot:panel-content>
                <!-- panel-notes lists notes and adds a form to submit new notes -->
                <core-panels-panel-notes></core-panels-panel-notes>
              </template>
            </core-panels-panel>

            <!-- changelog -->
            <core-panels-panel :panelTitle="'Endringslogg'" :panelSubtitle="'Endringer gjort på brukeren'" class="mt-12">
              <template v-slot:panel-content>
                
                <core-panels-panel-changelog></core-panels-panel-changelog>
              </template>
            </core-panels-panel>
        </template>
    </core-detail-template>
</template>

<script>
// CORE IMPORTS
// - template import
import DetailTemplate from '../../../core/backend/templates/DetailTemplate'

// - nav import
import PageNav from '../../../core/backend/nav/PageNav'
import SecondaryBreadcrumb from '../../../core/backend/nav/SecondaryBreadcrumb'

// - panels imports
import Panel from '../../../core/backend/panels/Panel'
import PanelListContent from '../../../core/backend/panels/PanelListContent'
import PanelTableContent from '../../../core/backend/panels/PanelTableContent'
import PanelChangelog from '../../../core/backend/panels/PanelChangelog'
import PanelNotes from '../../../core/backend/panels/PanelNotes'

// - button imports
import PrimaryBtn from '../../../core/backend/buttons/PrimaryBtn'
import TertiaryBtnGroup from '../../../core/backend/buttons/groups/TertiaryBtnGroup'

// MODULE IMPORTS
//- tables import
import DetailOrderRows from '../components/tables/DetailOrderTableRows'

// - titles import
import DetailTitle from '../components/titles/DetailTitle'

export default {
    data () {
        return {
            // dummy data for the time being
            userData: [
              { fieldName: 'Navn', fieldValue: 'Daniel Kjellid' },
              { fieldName: 'E-post', fieldValue: 'daniel@kjellid.no' },
              { fieldName: 'Mobil', fieldValue: '+47 452 76 890' },
              { fieldName: 'Adresse', fieldValue: 'Gunnar Schjelderupsvei 11R, 0485 Oslo' },
              { fieldName: 'Kilde', fieldValue: '/referal/newsletter/1' },
              { fieldName: 'Registrert', fieldValue: '10.08.2019 15:40' },
              { fieldName: 'Sist login', fieldValue: '10.08.2019 15:40' },
              { fieldName: 'Markedsføring', fieldValue: true },
              { fieldName: 'Personalisering', fieldValue: true },
              { fieldName: 'Tredjepartspersonalisering', fieldValue: false }
            ],
            // array for listing page navigation
            pageNav: [
              { title: 'Oversikt', to: '#overview', icon: 'M5.121 17.804A13.937 13.937 0 0112 16c2.5 0 4.847.655 6.879 1.804M15 10a3 3 0 11-6 0 3 3 0 016 0zm6 2a9 9 0 11-18 0 9 9 0 0118 0z' },
              { title: 'Notater', to: '#notes', icon: 'M7 8h10M7 12h4m1 8l-4-4H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-3l-4 4z'  },
              { title: 'Forespørsler', to: '#orders', icon: 'M20 13V6a2 2 0 00-2-2H6a2 2 0 00-2 2v7m16 0v5a2 2 0 01-2 2H6a2 2 0 01-2-2v-5m16 0h-2.586a1 1 0 00-.707.293l-2.414 2.414a1 1 0 01-.707.293h-3.172a1 1 0 01-.707-.293l-2.414-2.414A1 1 0 006.586 13H4' },
              { title: 'Endringslogg', to: '#orders', icon: 'M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z' }
            ]
        }
    },
    components: { 
        // core imports
        'core-detail-template': DetailTemplate,
        'core-nav-pagenav': PageNav,
        'core-nav-secondary-breadcrumb': SecondaryBreadcrumb,
        'core-panels-panel': Panel,
        'core-panels-panel-list': PanelListContent,
        'core-panels-panel-table': PanelTableContent,
        'core-panels-panel-changelog': PanelChangelog,
        'core-panels-panel-notes': PanelNotes,
        'core-buttons-primary-btn': PrimaryBtn,
        'core-buttons-tertiary-btn-group': TertiaryBtnGroup,

        // module imports
        'users-order-rows': DetailOrderRows,
        'users-detail-title': DetailTitle,
    }
}
</script>

<style>

</style>