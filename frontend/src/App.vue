<template>
  <div>
    <!--<users-user-overview></users-user-overview>-->
    <users-user-detail></users-user-detail>
  </div>
</template>

<script>
//import UsersOverview from './modules/users/views/UsersOverview.vue'
import UserDetail from './modules/users/views/UserDetail'

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
    //'users-user-overview': UsersOverview,
    'users-user-detail': UserDetail,
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
