<template>
  <div class="q-pa-md">
    <div class="q-py-md ">
      <q-btn color="light-blue-6" @click="onAdd">Add Member</q-btn>
    </div>
   <table class="table w-full">
    <thead>
      <tr>
        <th>ID</th>
        <th>Firstname</th>
        <th>Lastname</th>
        <th>Email</th>
        <th>EmployeeType</th>
        <th>Team</th>
        <th></th>
      </tr>
    </thead>

    <tbody>
      <tr v-for="(item,index) in 5">
          <th>{{ index+1 }}</th>
          <td>Firstname</td>
          <td>Lastname</td>
          <td>Email</td>
          <td>EmployeeType</td>
          <td>Team</td>
          <td>
            <q-btn color="amber" glossy label="Edit" />
            <q-btn color="secondary" label="Leave" />
          </td>
      </tr>
    </tbody>
   </table>


  </div>
</template>

<script setup>
import { ref } from "vue";
import router from '../router'



const rows = ref([]);

const fetchData = () => {
  fetch("http://localhost:8000/api/user/me/")
    .then(async (res) => await res.json())
    .then((result) => {
      console.log(result);
      // rows.value = result;
    });
};
fetchData();

const onEdit = (id) => {
  router.push('/edit_member')
};

const onLeave = (id) => {
  alert(firstname+"Leave")
};


const onAdd = () => {
  router.push('/add_member')
};


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
