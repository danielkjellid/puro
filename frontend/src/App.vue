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
                      >Oversikt</a
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
          <nav>
            <a href="#" class="flex items-center px-3 py-2 text-sm font-medium leading-5 text-gray-600 transition duration-150 ease-in-out rounded-md group hover:text-gray-900 hover:bg-gray-100 focus:outline-none focus:text-gray-900 focus:bg-gray-200">
              <svg class="flex-shrink-0 w-6 h-6 mr-3 -ml-1 text-gray-400 transition duration-150 ease-in-out group-hover:text-gray-500 group-focus:text-gray-600" stroke="currentColor" fill="none" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5.121 17.804A13.937 13.937 0 0112 16c2.5 0 4.847.655 6.879 1.804M15 10a3 3 0 11-6 0 3 3 0 016 0zm6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
              </svg>
              <span class="truncate">
                Overikt
              </span>
            </a>
            <a href="#" class="flex items-center px-3 py-2 mt-1 text-sm font-medium leading-5 text-gray-600 transition duration-150 ease-in-out rounded-md group hover:text-gray-900 hover:bg-gray-100 focus:outline-none focus:text-gray-900 focus:bg-gray-200">
              <svg class="flex-shrink-0 w-6 h-6 mr-3 -ml-1 text-gray-400 transition duration-150 ease-in-out group-focus:text-gray-500" stroke="currentColor" fill="none" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 8h10M7 12h4m1 8l-4-4H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-3l-4 4z"/>
              </svg>
              <span class="truncate">
                Notater
              </span>
            </a>
            <a href="#" class="flex items-center px-3 py-2 mt-1 text-sm font-medium leading-5 text-gray-600 transition duration-150 ease-in-out rounded-md group hover:text-gray-900 hover:bg-gray-50 focus:outline-none focus:text-gray-900 focus:bg-gray-200">
              <svg class="flex-shrink-0 w-6 h-6 mr-3 -ml-1 text-gray-400 transition duration-150 ease-in-out group-focus:text-gray-500" stroke="currentColor" fill="none" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 13V6a2 2 0 00-2-2H6a2 2 0 00-2 2v7m16 0v5a2 2 0 01-2 2H6a2 2 0 01-2-2v-5m16 0h-2.586a1 1 0 00-.707.293l-2.414 2.414a1 1 0 01-.707.293h-3.172a1 1 0 01-.707-.293l-2.414-2.414A1 1 0 006.586 13H4"/>
              </svg>
              <span class="truncate">
                Forespørsler
              </span>
            </a>
            <a href="#" class="flex items-center px-3 py-2 mt-1 text-sm font-medium leading-5 text-gray-600 transition duration-150 ease-in-out rounded-md group hover:text-gray-900 hover:bg-gray-100 focus:outline-none focus:text-gray-900 focus:bg-gray-200">
              <svg class="flex-shrink-0 w-6 h-6 mr-3 -ml-1 text-gray-400 transition duration-150 ease-in-out group-focus:text-gray-500" stroke="currentColor" fill="none" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"/>
              </svg>
              <span class="truncate">
                Endringslogg
              </span>
            </a>
          </nav>
        </div>
        <div class="col-span-3">
         <div>
            <core-panels-panel :panelTitle="'Oversikt'" :panelSubtitle="'Personlig informasjon om bruker'">
              <template v-slot:panel-content>
                <core-panels-panel-list :data="userData"></core-panels-panel-list>
              </template>
            </core-panels-panel>
          </div>
          <div class="mt-12">
            <div class="overflow-hidden bg-white shadow sm:rounded-lg ">
              <div class="px-4 py-5 bg-white border-b border-gray-200 sm:px-6">
                <div class="-mt-4 -ml-4">
                  <div class="mt-4 ml-4">
                    <h3 class="text-lg font-medium leading-6 text-gray-900">
                      Notater
                    </h3>
                    <p class="mt-1 text-sm leading-5 text-gray-500">
                      Notater om bruker
                    </p>
                  </div>
                </div>
              </div>
              <div>
                <div class="flex px-4 py-5">
                  <div>
                    <span class="inline-flex items-center justify-center w-10 h-10 bg-gray-400 rounded-full">
                      <span class="font-medium leading-none text-white text-md">TW</span>
                    </span>
                  </div>
                  <div class="ml-4">
                    <h2 class="text-sm font-medium text-gray-900">Emilia Gates</h2>
                    <p class="mt-2 text-sm text-gray-600">Tailwind includes a generous palette of great-looking, well-balanced colors that are perfect for prototyping or for kicking off a brand new project.</p>
                    <span class="block mt-2 text-xs text-gray-600">4 days ago &#8226; Rediger &#8226; Slett</span>
                  </div>
                </div>
                <div class="flex px-4 py-5 border-t border-gray-300">
                  <div>
                    <span class="inline-flex items-center justify-center w-10 h-10 bg-gray-400 rounded-full">
                      <span class="font-medium leading-none text-white text-md">TW</span>
                    </span>
                  </div>
                  <div class="ml-4">
                    <h2 class="text-sm font-medium text-gray-900">Emilia Gates</h2>
                    <p class="mt-2 text-sm text-gray-600">Tailwind includes a generous palette of great-looking, well-balanced colors that are perfect for prototyping or for kicking off a brand new project.</p>
                    <span class="block mt-2 text-xs text-gray-600">4 days ago &#8226; Rediger &#8226; Slett</span>
                  </div>
                </div>
                <div class="px-4 py-5 bg-gray-50">
                  <div>
                    <label for="add-note" class="block text-sm font-medium leading-5 text-gray-700">Add a note</label>
                    <div class="relative mt-1 rounded-md shadow-sm">
                      <textarea id="add-note" class="block w-full form-input sm:text-sm sm:leading-5" rows="3"/>
                    </div>
                    <div class="flex justify-end mt-4">
                      <primary-btn :text="'Legg til notat'"></primary-btn>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="mt-12">
            <div class="overflow-hidden bg-white shadow sm:rounded-lg">
              <div class="px-4 py-5 bg-white border-b border-gray-200 sm:px-6">
                <div class="-mt-4 -ml-4">
                  <div class="mt-4 ml-4">
                    <h3 class="text-lg font-medium leading-6 text-gray-900">
                      Forespørsler
                    </h3>
                    <p class="mt-1 text-sm leading-5 text-gray-500">
                      Forespørsler brukeren har gjort
                    </p>
                  </div>
                </div>
              </div>
              <div>
                <div class="flex flex-col">
                  <div class="py-2 -my-2 sm:-mx-6 sm:px-6 lg:-mx-8 lg:px-8">
                    <div class="inline-block min-w-full overflow-hidden align-middle shadow sm:rounded-lg">
                      <table class="min-w-full">
                        <thead>
                          <tr>
                            <th class="px-6 py-3 text-xs font-medium leading-4 tracking-wider text-left text-gray-500 uppercase border-b border-gray-200 bg-gray-50">
                              Produkt
                            </th>
                            <th class="px-6 py-3 text-xs font-medium leading-4 tracking-wider text-left text-gray-500 uppercase border-b border-gray-200 bg-gray-50">
                              Antall
                            </th>
                            <th class="px-6 py-3 text-xs font-medium leading-4 tracking-wider text-left text-gray-500 uppercase border-b border-gray-200 bg-gray-50">
                              Sum
                            </th>
                            <th class="px-6 py-3 text-xs font-medium leading-4 tracking-wider text-left text-gray-500 uppercase border-b border-gray-200 bg-gray-50">
                              Status
                            </th>
                            <th class="px-6 py-3 border-b border-gray-200 bg-gray-50"></th>
                          </tr>
                        </thead>
                        <tbody class="bg-white">
                          <tr>
                            <td class="px-6 py-4 whitespace-no-wrap">
                              <div class="flex items-center">
                                <div class="flex-shrink-0 w-10 h-10">
                                  <img class="w-10 h-10 rounded-full" src="https://images.unsplash.com/photo-1532910404247-7ee9488d7292?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="" />
                                </div>
                                <div class="ml-4">
                                  <div class="text-sm font-medium leading-5 text-gray-900">Ikon</div>
                                  <div class="text-sm leading-5 text-gray-500">Sky gray</div>
                                </div>
                              </div>
                            </td>
                            <td class="px-6 py-4 whitespace-no-wrap">
                              <div class="text-sm leading-5 text-gray-900">20x1m2</div>
                              <div class="text-sm leading-5 text-gray-500">120x100cm</div>
                            </td>
                            <td class="px-6 py-4 text-sm leading-5 text-gray-900 whitespace-no-wrap">
                              9980,00kr
                            </td>
                            <td class="px-6 py-4 whitespace-no-wrap">
                              <span class="inline-flex px-2 text-xs font-semibold leading-5 text-green-800 bg-green-100 rounded-full">
                                Tilbud sendt
                              </span>
                            </td>
                            <td class="px-6 py-4 text-sm font-medium leading-5 text-right whitespace-no-wrap">
                              <a href="#" class="text-indigo-600 hover:text-indigo-900 focus:outline-none focus:underline">Behandle</a>
                            </td>
                          </tr>
                          <tr class="bg-gray-50">
                            <td class="px-6 py-4 whitespace-no-wrap">
                              <div class="flex items-center">
                                <div class="flex-shrink-0 w-10 h-10">
                                  <img class="w-10 h-10 rounded-full" src="https://images.unsplash.com/photo-1532910404247-7ee9488d7292?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="" />
                                </div>
                                <div class="ml-4">
                                  <div class="text-sm font-medium leading-5 text-gray-900">Ikon</div>
                                  <div class="text-sm leading-5 text-gray-500">Sky gray</div>
                                </div>
                              </div>
                            </td>
                            <td class="px-6 py-4 whitespace-no-wrap">
                              <div class="text-sm leading-5 text-gray-900">20x1m2</div>
                              <div class="text-sm leading-5 text-gray-500">120x100cm</div>
                            </td>
                            <td class="px-6 py-4 text-sm leading-5 text-gray-900 whitespace-no-wrap">
                              9980,00kr
                            </td>
                            <td class="px-6 py-4 whitespace-no-wrap">
                              <span class="inline-flex px-2 text-xs font-semibold leading-5 text-red-800 bg-red-100 rounded-full">
                                Mottatt
                              </span>
                            </td>
                            <td class="px-6 py-4 text-sm font-medium leading-5 text-right whitespace-no-wrap">
                              <a href="#" class="text-indigo-600 hover:text-indigo-900 focus:outline-none focus:underline">Behandle</a>
                            </td>
                          </tr>
                          <tr>
                            <td class="px-6 py-4 whitespace-no-wrap">
                              <div class="flex items-center">
                                <div class="flex-shrink-0 w-10 h-10">
                                  <img class="w-10 h-10 rounded-full" src="https://images.unsplash.com/photo-1532910404247-7ee9488d7292?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="" />
                                </div>
                                <div class="ml-4">
                                  <div class="text-sm font-medium leading-5 text-gray-900">Ikon</div>
                                  <div class="text-sm leading-5 text-gray-500">Sky gray</div>
                                </div>
                              </div>
                            </td>
                            <td class="px-6 py-4 whitespace-no-wrap">
                              <div class="text-sm leading-5 text-gray-900">20x1m2</div>
                              <div class="text-sm leading-5 text-gray-500">120x100cm</div>
                            </td>
                            <td class="px-6 py-4 text-sm leading-5 text-gray-900 whitespace-no-wrap">
                              9980,00kr
                            </td>
                            <td class="px-6 py-4 whitespace-no-wrap">
                              <span class="inline-flex px-2 text-xs font-semibold leading-5 text-green-800 bg-green-100 rounded-full">
                                Tilbud sendt
                              </span>
                            </td>
                            <td class="px-6 py-4 text-sm font-medium leading-5 text-right whitespace-no-wrap">
                              <a href="#" class="text-indigo-600 hover:text-indigo-900 focus:outline-none focus:underline">Behandle</a>
                            </td>
                          </tr>
                          <tr class="bg-gray-50">
                            <td class="px-6 py-4 whitespace-no-wrap">
                              <div class="flex items-center">
                                <div class="flex-shrink-0 w-10 h-10">
                                  <img class="w-10 h-10 rounded-full" src="https://images.unsplash.com/photo-1532910404247-7ee9488d7292?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="" />
                                </div>
                                <div class="ml-4">
                                  <div class="text-sm font-medium leading-5 text-gray-900">Ikon</div>
                                  <div class="text-sm leading-5 text-gray-500">Sky gray</div>
                                </div>
                              </div>
                            </td>
                            <td class="px-6 py-4 whitespace-no-wrap">
                              <div class="text-sm leading-5 text-gray-900">20x1m2</div>
                              <div class="text-sm leading-5 text-gray-500">120x100cm</div>
                            </td>
                            <td class="px-6 py-4 text-sm leading-5 text-gray-900 whitespace-no-wrap">
                              9980,00kr
                            </td>
                            <td class="px-6 py-4 whitespace-no-wrap">
                              <span class="inline-flex px-2 text-xs font-semibold leading-5 text-red-800 bg-red-100 rounded-full">
                                Mottatt
                              </span>
                            </td>
                            <td class="px-6 py-4 text-sm font-medium leading-5 text-right whitespace-no-wrap">
                              <a href="#" class="text-indigo-600 hover:text-indigo-900 focus:outline-none focus:underline">Behandle</a>
                            </td>
                          </tr>
                          <tr>
                            <td class="px-6 py-4 whitespace-no-wrap">
                              <div class="flex items-center">
                                <div class="flex-shrink-0 w-10 h-10">
                                  <img class="w-10 h-10 rounded-full" src="https://images.unsplash.com/photo-1532910404247-7ee9488d7292?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="" />
                                </div>
                                <div class="ml-4">
                                  <div class="text-sm font-medium leading-5 text-gray-900">Ikon</div>
                                  <div class="text-sm leading-5 text-gray-500">Sky gray</div>
                                </div>
                              </div>
                            </td>
                            <td class="px-6 py-4 whitespace-no-wrap">
                              <div class="text-sm leading-5 text-gray-900">20x1m2</div>
                              <div class="text-sm leading-5 text-gray-500">120x100cm</div>
                            </td>
                            <td class="px-6 py-4 text-sm leading-5 text-gray-900 whitespace-no-wrap">
                              9980,00kr
                            </td>
                            <td class="px-6 py-4 whitespace-no-wrap">
                              <span class="inline-flex px-2 text-xs font-semibold leading-5 text-orange-800 bg-orange-100 rounded-full">
                                Behandler
                              </span>
                            </td>
                            <td class="px-6 py-4 text-sm font-medium leading-5 text-right whitespace-no-wrap">
                              <a href="#" class="text-indigo-600 hover:text-indigo-900 focus:outline-none focus:underline">Behandle</a>
                            </td>
                          </tr>
                        </tbody>
                      </table>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="mt-12">
            <div class="overflow-hidden bg-white shadow sm:rounded-lg">
              <div class="px-4 py-5 bg-white border-b border-gray-200 sm:px-6">
                <div class="-mt-4 -ml-4">
                  <div class="mt-4 ml-4">
                    <h3 class="text-lg font-medium leading-6 text-gray-900">
                      Endringslogg
                    </h3>
                    <p class="mt-1 text-sm leading-5 text-gray-500">
                      Endringer gjort på brukeren
                    </p>
                  </div>
                </div>
              </div>
              <div>
                <div class="flex flex-col">
                  <div class="py-2 -my-2 sm:-mx-6 sm:px-6 lg:-mx-8 lg:px-8">
                    <div class="inline-block min-w-full overflow-hidden align-middle shadow sm:rounded-lg">
                      <table class="min-w-full">
                        <thead>
                          <tr>
                            <th class="px-6 py-3 text-xs font-medium leading-4 tracking-wider text-left text-gray-500 uppercase border-b border-gray-200 bg-gray-50">
                              Bruker
                            </th>
                            <th class="px-6 py-3 text-xs font-medium leading-4 tracking-wider text-left text-gray-500 uppercase border-b border-gray-200 bg-gray-50">
                              Endring
                            </th>
                            <th class="px-6 py-3 text-xs font-medium leading-4 tracking-wider text-left text-gray-500 uppercase border-b border-gray-200 bg-gray-50">
                              Dato
                            </th>
                          </tr>
                        </thead>
                        <tbody>
                          <tr class="bg-white">
                            <td class="px-6 py-4 text-sm leading-5 text-gray-900 whitespace-no-wrap">
                              Daniel Kjellid
                            </td>
                            <td class="px-6 py-4 text-sm leading-5 text-gray-900">
                              <span class="px-1 py-1 text-red-800 bg-red-100">first_name</span> endret fra <span class="px-1 py-1 text-red-800 bg-red-100">Test</span> til <span class="px-1 py-1 text-red-800 bg-red-100">Test123</span>
                            </td>
                            <td class="px-6 py-4 text-sm leading-5 text-gray-900 whitespace-no-wrap">
                              28. Desember 2019 21:15
                            </td>
                          </tr>
                          <tr class="bg-gray-50">
                            <td class="px-6 py-4 text-sm leading-5 text-gray-900 whitespace-no-wrap">
                              Daniel Kjellid
                            </td>
                            <td class="px-6 py-4 text-sm leading-5 text-gray-900">
                              <span class="px-1 py-1 text-red-800 bg-red-100">first_name</span> endret fra <span class="px-1 py-1 text-red-800 bg-red-100">Test</span> til <span class="px-1 py-1 text-red-800 bg-red-100">Test123</span>
                            </td>
                            <td class="px-6 py-4 text-sm leading-5 text-gray-900 whitespace-no-wrap">
                              28. Desember 2019 21:15
                            </td>
                          </tr>
                          <tr class="bg-white">
                            <td class="px-6 py-4 text-sm leading-5 text-gray-900 whitespace-no-wrap">
                              Daniel Kjellid
                            </td>
                            <td class="px-6 py-4 text-sm leading-5 text-gray-900">
                              <span class="px-1 py-1 text-red-800 bg-red-100">first_name</span> endret fra <span class="px-1 py-1 text-red-800 bg-red-100">Test</span> til <span class="px-1 py-1 text-red-800 bg-red-100">Test123</span>
                            </td>
                            <td class="px-6 py-4 text-sm leading-5 text-gray-900 whitespace-no-wrap">
                              28. Desember 2019 21:15
                            </td>
                          </tr>
                          <tr class="bg-gray-50">
                            <td class="px-6 py-4 text-sm leading-5 text-gray-900 whitespace-no-wrap">
                              Daniel Kjellid
                            </td>
                            <td class="px-6 py-4 text-sm leading-5 text-gray-900">
                              <span class="px-1 py-1 text-red-800 bg-red-100">first_name</span> endret fra <span class="px-1 py-1 text-red-800 bg-red-100">Test</span> til <span class="px-1 py-1 text-red-800 bg-red-100">Test123</span>
                            </td>
                            <td class="px-6 py-4 text-sm leading-5 text-gray-900 whitespace-no-wrap">
                              28. Desember 2019 21:15
                            </td>
                          </tr>
                          <tr class="bg-white">
                            <td class="px-6 py-4 text-sm leading-5 text-gray-900 whitespace-no-wrap">
                              Daniel Kjellid
                            </td>
                            <td class="px-6 py-4 text-sm leading-5 text-gray-900">
                              <span class="px-1 py-1 text-red-800 bg-red-100">first_name</span> endret fra <span class="px-1 py-1 text-red-800 bg-red-100">Test</span> til <span class="px-1 py-1 text-red-800 bg-red-100">Test123</span>
                            </td>
                            <td class="px-6 py-4 text-sm leading-5 text-gray-900 whitespace-no-wrap">
                              28. Desember 2019 21:15
                            </td>
                          </tr>
                        </tbody>
                      </table>
                    </div>
                  </div>
                </div>
              </div>
            </div>
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
