<template>
  <div class="q-pa-md">
    <div class="q-py-md ">
      <q-btn color="light-blue-6" @click="onAdd">Add Member</q-btn>
    </div>
   

    
<div class="relative overflow-x-auto shadow-md sm:rounded-lg">
    <table class="w-full text-sm text-left text-gray-500 dark:text-gray-400">
        <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
            <tr>
                <th scope="col" class="px-6 py-3">
                    
                </th>
                <th scope="col" class="px-6 py-3">
                    Firstname
                </th>
                <th scope="col" class="px-6 py-3">
                    Lastname
                </th>
                <th scope="col" class="px-6 py-3">
                    Email
                </th>
                <th scope="col" class="px-6 py-3">
                  Position
                </th>
                <th scope="col" class="px-6 py-3">
                  Team
                </th>
                <th scope="col" class="px-6 py-3">
                    <span class="sr-only">Edit</span>
                </th>
                <th scope="col" class="px-6 py-3">
                    <span class="sr-only">Leave</span>
                </th>
            </tr>
        </thead>
        <tbody v-for="(user , index) in users">
            <tr class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600">
                <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                    {{ index+1 }}
                </th>
                <td class="px-6 py-4">
                    {{user.name}}
                </td>
                <td class="px-6 py-4">
                    {{user.l_name}}
                </td>
                <td class="px-6 py-4">
                    {{user.email}}
                </td>
                <td class="px-6 py-4">
                    {{user.employee_type}}
                </td>
                <td class="px-6 py-4">
                    {{user.team}}
                </td>
                <td class="px-6 py-4 text-right">
                    <a href="#" class="font-medium text-blue-600 dark:text-blue-500 hover:underline" @click="delete_users(user.id)">Delete</a>
                </td>
                <td class="px-6 py-4 text-right">
                    <a href="#" class="font-medium text-blue-600 dark:text-blue-500 hover:underline">Leave</a>
                </td>
            </tr>
        
        </tbody>
    </table>
</div>





  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import router from '../router'
import axios from "axios";

const users = ref({});
const token = localStorage.getItem('Token')

// axios
const config = {
  headers: {
    Authorization: `Token ${token}`,
  }
}




const fetch_users = async () => {
  await axios.get('http://localhost:8000/api/user/',config)
  .then((response) => {
    users.value = response.data
  }).catch((err) =>{
    console.log("User",err);
  })
}

const delete_users = async (id) => {
  console.log('delete ' , id);
  await axios.delete(`http://localhost:8000/api/user/${id}`,config)
  .then((response) => {
    console.log(response);
    window.location.reload()
    }).catch((err)=>{
    console.log(err);
  })
}


onMounted(() => fetch_users())

const onAdd = () =>{
  router.push('/add_member')
}

</script>

<style lang="sass">
.my-sticky-header-table
  /* height or max-height is important */
  height: 750px

  .q-table__top,
  .q-table__bottom,
  thead tr:first-child th
    /* bg color is important for th; just specify one */
    color:$red-1
    background-color: #06283D


  thead tr th
    position: sticky
    z-index: 1
  thead tr:first-child th
    top: 0

  /* this is when the loading indicator appears */
  &.q-table--loading thead tr:last-child th
    /* height of all previous header rows */
    top: 48px
</style>
