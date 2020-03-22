<template>
  <div>
    <div class="sticky top-0 z-10">
      <core-header></core-header>
        <!--
      <users-user-overview></users-user-overview>
      -->
        <div class="sticky top-0 z-10 bg-white shadow">
          <div class="container px-8 mx-auto">
            <div class="flex items-center justify-between py-5">
              <div>
                <div>
                  <nav class="flex items-center text-sm font-medium leading-5">
                    <a
                      href="#"
                      class="text-gray-500 transition duration-150 ease-in-out hover:text-gray-700 focus:outline-none focus:underline"
                      >Brukere</a
                    >
                    <svg
                      class="flex-shrink-0 w-5 h-5 mx-2 text-gray-400"
                      fill="currentColor"
                      viewBox="0 0 20 20"
                    >
                      <path
                        fill-rule="evenodd"
                        d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z"
                        clip-rule="evenodd"
                      />
                    </svg>
                    <a
                      href="#"
                      class="text-gray-500 transition duration-150 ease-in-out hover:text-gray-700 focus:outline-none focus:underline"
                      >Daniel Kjellid</a
                    >
                  </nav>
                </div>
                <div class="flex items-center mt-3">
                  <span
                    class="inline-flex items-center justify-center w-12 h-12 bg-gray-400 rounded-full"
                  >
                    <span class="text-lg font-medium leading-none text-white"
                      >DK</span
                    >
                  </span>
                  <div class="ml-3">
                    <h1 class="text-xl font-medium leading-6 text-gray-900">
                      Daniel Kjellid
                    </h1>
                    <div class="flex items-center text-sm leading-5 text-gray-500">
                      <svg class="flex-shrink-0 w-5 h-5 mr-1 text-green-400" fill="currentColor" viewBox="0 0 20 20">
                        <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/>
                      </svg>
                      Verifisert konto
                    </div>
                  </div>
                </div>
              </div>
              <div>
                <tertiary-group
                  :btns="['Send e-post', 'Notat', 'Rediger', 'Eksporter']"
                ></tertiary-group>
                <span class="ml-3">
                  <primary-btn :text="'Logg inn som'"></primary-btn>
                </span>
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
          <core-nav-pagenav :links="pageNav"></core-nav-pagenav>
        </div>
        <div class="col-span-3">
         <div>
            <core-panels-panel :panelTitle="'Oversikt'" :panelSubtitle="'Personlig informasjon om bruker'">
              <template v-slot:panel-content>
                <core-panels-panel-list :data="userData"></core-panels-panel-list>
              </template>
            </core-panels-panel>
            <!-- panel component containing title and subtitle -->
            <core-panels-panel :panelTitle="'Forespørsler'" :panelSubtitle="'Forespørsler brukeren har gjort'" class="mt-12">
              <!-- slot for content inside template, can be list or panel-table -->
              <template v-slot:panel-content>
                <!-- panel-table component setting table head -->
                <core-panels-panel-table :tableHeads="['Produkt', 'Antall', 'Sum', 'Status']">
                  <template v-slot:panel-table-rows>
                    <users-order-rows v-for="index in 5" :key="index"></users-order-rows>
                  </template>
                </core-panels-panel-table>
              </template>
            </core-panels-panel>
            
            <core-panels-panel :panelTitle="'Notater'" :panelSubtitle="'Notater om bruker'" class="mt-12">
              <template v-slot:panel-content>
                <core-panels-panel-notes></core-panels-panel-notes>
              </template>
            </core-panels-panel>

            <core-panels-panel :panelTitle="'Endringslogg'" :panelSubtitle="'Endringer gjort på brukeren'" class="mt-12">
              <template v-slot:panel-content>
                <core-panels-panel-changelog></core-panels-panel-changelog>
              </template>
            </core-panels-panel>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// import UsersOverview from './modules/users/views/UsersOverview.vue'

import Panel from './core/backend/panels/Panel';
import PanelListContent from './core/backend/panels/PanelListContent';
import PanelTableContent from './core/backend/panels/PanelTableContent';
import PanelChangelog from './core/backend/panels/PanelChangelog';
import PanelNotes from './core/backend/panels/PanelNotes';

import PageNav from './core/backend/nav/PageNav';

import DetailOrderRows from './modules/users/components/DetailOrderRows';

import TheHeader from "./core/backend/nav/TheHeader";

import PrimaryBtn from "./core/backend/buttons/PrimaryBtn";
import TertiaryBtnGroup from "./core/backend/buttons/groups/TertiaryBtnGroup";

export default {
  data() {
    return {
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
      pageNav: [
        { title: 'Oversikt', to: '#overview', icon: 'M5.121 17.804A13.937 13.937 0 0112 16c2.5 0 4.847.655 6.879 1.804M15 10a3 3 0 11-6 0 3 3 0 016 0zm6 2a9 9 0 11-18 0 9 9 0 0118 0z' },
        { title: 'Notater', to: '#notes', icon: 'M7 8h10M7 12h4m1 8l-4-4H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-3l-4 4z'  },
        { title: 'Forespørsler', to: '#orders', icon: 'M20 13V6a2 2 0 00-2-2H6a2 2 0 00-2 2v7m16 0v5a2 2 0 01-2 2H6a2 2 0 01-2-2v-5m16 0h-2.586a1 1 0 00-.707.293l-2.414 2.414a1 1 0 01-.707.293h-3.172a1 1 0 01-.707-.293l-2.414-2.414A1 1 0 006.586 13H4' },
        { title: 'Endringslogg', to: '#orders', icon: 'M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z' }
      ]
    }
  },
  components: {
    // 'users-user-overview': UsersOverview,
    "core-header": TheHeader,
    "primary-btn": PrimaryBtn,
    "tertiary-group": TertiaryBtnGroup,
    'core-panels-panel': Panel,
    'core-panels-panel-list': PanelListContent,
    'core-panels-panel-table': PanelTableContent,
    'core-panels-panel-changelog': PanelChangelog,
    'core-nav-pagenav': PageNav,
    'core-panels-panel-notes': PanelNotes,
    'users-order-rows': DetailOrderRows,
  }
};
</script>

<style>
body {
  background-color: #f7fafc;
}
.bg-gray-50 {
  background-color: #f9fafb;
}
</style>
