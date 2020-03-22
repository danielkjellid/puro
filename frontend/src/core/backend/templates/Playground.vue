<template>
  <div>
      <div class="sticky top-0 z-10">
          <core-nav-header></core-nav-header>
      </div>
      <div>
        <div class="pb-32 bg-gray-800">
            <header class="container py-10 m-auto">
              <div class="px-4 px-8 mx-auto max-w-7xl">
                <div class="md:flex md:items-center md:justify-between">
                  <div class="flex-1 min-w-0">
                    <h2 class="text-2xl font-bold leading-7 text-white sm:text-3xl sm:leading-9 sm:truncate">
                      Back End Developer
                    </h2>
                  </div>
                  <div class="flex mt-4 md:mt-0 md:ml-4">
                    <span class="rounded-md shadow-sm">
                      <button type="button" class="inline-flex items-center px-4 py-2 text-sm font-medium leading-5 text-white transition duration-150 ease-in-out bg-gray-600 border border-transparent rounded-md hover:bg-gray-500 focus:outline-none focus:shadow-outline-gray focus:border-gray-700 active:bg-gray-700">
                        Edit
                      </button>
                    </span>
                    <span class="ml-3 rounded-md shadow-sm">
                      <button type="button" class="inline-flex items-center px-4 py-2 text-sm font-medium leading-5 text-white transition duration-150 ease-in-out bg-indigo-500 border border-transparent rounded-md hover:bg-indigo-400 focus:outline-none focus:shadow-outline-indigo focus:border-indigo-600 active:bg-indigo-600">
                        Publish
                      </button>
                    </span>
                  </div>
                </div>
              </div>
            </header>
        </div>
        <main class="container m-auto -mt-32">
          <div class="px-4 px-8 pb-12 mx-auto max-w-7xl">
            <!-- Replace with your content -->
            <div class="pt-2 bg-white rounded-lg shadow">
                <div>
                  <div class="border-b border-gray-200">
                    <nav class="flex px-4 -mb-px">
                      <a href="#" class="px-1 py-4 text-sm font-medium leading-5 text-gray-500 whitespace-no-wrap border-b-2 border-transparent hover:text-gray-700 hover:border-gray-300 focus:outline-none focus:text-gray-700 focus:border-gray-300">
                        My Account
                      </a>
                      <a href="#" class="px-1 py-4 ml-8 text-sm font-medium leading-5 text-gray-500 whitespace-no-wrap border-b-2 border-transparent hover:text-gray-700 hover:border-gray-300 focus:outline-none focus:text-gray-700 focus:border-gray-300">
                        Company
                      </a>
                      <a href="#" class="px-1 py-4 ml-8 text-sm font-medium leading-5 text-indigo-600 whitespace-no-wrap border-b-2 border-indigo-500 focus:outline-none focus:text-indigo-800 focus:border-indigo-700">
                        Team Members
                      </a>
                      <a href="#" class="px-1 py-4 ml-8 text-sm font-medium leading-5 text-gray-500 whitespace-no-wrap border-b-2 border-transparent hover:text-gray-700 hover:border-gray-300 focus:outline-none focus:text-gray-700 focus:border-gray-300">
                        Billing
                      </a>
                    </nav>
                  </div>
                </div>
                <div class="px-4 py-5 border-b border-gray-200">
                   <core-inputs-icon-btn :label="'search'" :iconPath="'M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z'" :placeHolder="'Søk...'" :btnText="'Søk'"></core-inputs-icon-btn> 
                </div>
                <div class="flex flex-col">
                  <div class="px-8 py-2 -mx-8 -my-2 overflow-x-auto">
                    <div class="inline-block min-w-full overflow-hidden align-middle">
                      <table class="min-w-full">
                        <thead>
                          <tr>
                            <th class="px-6 py-3 text-xs font-medium leading-4 tracking-wider text-left text-gray-500 uppercase bg-gray-100 border-b border-gray-200">
                              Test
                            </th>
                            <th class="px-6 py-3 text-xs font-medium leading-4 tracking-wider text-left text-gray-500 uppercase bg-gray-100 border-b border-gray-200">
                              Test
                            </th>
                            <th class="px-6 py-3 text-xs font-medium leading-4 tracking-wider text-left text-gray-500 uppercase bg-gray-100 border-b border-gray-200">
                              Test
                            </th>
                            <th class="px-6 py-3 text-xs font-medium leading-4 tracking-wider text-left text-gray-500 uppercase bg-gray-100 border-b border-gray-200">
                              Test
                            </th>
                            <th class="px-6 py-3 bg-gray-100 border-b border-gray-200"></th>
                          </tr>
                        </thead>
                        <tbody class="bg-white">
                          <tr v-for="index in 5" :key="index">
                            <td class="px-6 py-4 whitespace-no-wrap border-b border-gray-200">
                              <div class="flex items-center">
                                <div class="flex-shrink-0 w-10 h-10">
                                  <span class="inline-flex items-center justify-center w-10 h-10 bg-gray-400 rounded-full">
                                    <span class="font-medium leading-none text-white text-md">TW</span>
                                  </span>
                                </div>
                                <div class="ml-4">
                                  <div class="text-sm font-medium leading-5 text-gray-900">Bernard Lane</div>
                                  <div class="text-sm leading-5 text-gray-500">Utvikler</div>
                                </div>
                              </div>
                            </td>
                            <td class="px-6 py-4 whitespace-no-wrap border-b border-gray-200">
                              <div class="text-sm leading-5 text-gray-900">ted.woods@example.com</div>
                              <div class="text-sm leading-5 text-gray-500">+47 123 45 678</div>
                            </td>
                            <td class="px-6 py-4 whitespace-no-wrap border-b border-gray-200">
                              <div class="text-sm leading-5 text-gray-900">Adressegate 1</div>
                              <div class="text-sm leading-5 text-gray-500">0485 Oslo</div>
                            </td>
                            <td class="px-6 py-4 whitespace-no-wrap border-b border-gray-200">
                              <core-pills-success-pill :text="'Aktiv'"></core-pills-success-pill>
                            </td>
                            <td class="px-6 py-4 text-sm font-medium leading-5 text-right whitespace-no-wrap border-b border-gray-200">
                              <a href="#" class="text-indigo-600 hover:text-indigo-900 focus:outline-none focus:underline">Rediger</a>
                            </td>
                          </tr>
                        </tbody>
                      </table>
                      <div class="px-6 py-4">
                        <core-pagination-pagination></core-pagination-pagination>
                      </div>
                    </div>
                  </div>
                </div>
            </div>
            <!-- /End replace -->
          </div>
        </main>
      </div>
  </div>
</template>

<script>
import Header from '../nav/TheHeader'
import IconAndBtnInput from '../inputs/IconAndBtn'
import Pagination from '../pagination/Pagination'
//import PrimaryBreadcrumbs from '../nav/PrimaryBreadcrumb'

export default {
    components: {
        'core-nav-header': Header,
        'core-inputs-icon-btn': IconAndBtnInput,
        'core-pagination-pagination': Pagination,
        //'core-nav-primary-breadcrumb': PrimaryBreadcrumbs,
    }
}
</script>