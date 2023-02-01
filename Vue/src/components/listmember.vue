<template>
  <div class="q-pa-md">
    <div class="q-py-md ">
      <q-btn color="light-blue-6" @click="onAdd">Add Member</q-btn>
    </div>
    <q-table
      class="my-sticky-header-table" 
      :rows="rows"
      :columns="columns"
      row-key="name"
    >
      <template v-slot:body-cell-actions="props" class="h-96">
        <q-td :props="props">
          <div class="q-pa-md">
            <q-btn-dropdown color="primary" label="">
              <q-list>
                <q-item  v-close-popup @click="checkin = true">
                  <q-item-section>
                    <q-btn color="positive">Check in</q-btn>
                  </q-item-section>
                </q-item>

                <q-item  v-close-popup @click="onItemClick">
                  <q-item-section>
                    <q-btn color="deep-orange">Check out</q-btn>
                  </q-item-section>
                </q-item>

                <q-item v-close-popup @click="onItemClick">
                  <q-item-section>
                    <q-btn color="warning" @cilck="open('top')">Leave</q-btn>
                  </q-item-section>
                </q-item>

                <q-item  v-close-popup @click="onItemClick">
                  <q-item-section>
                    <q-btn color="info" @click="onEdit(props.row.id)">Edit</q-btn>
                  </q-item-section>
                </q-item>
              </q-list>
            </q-btn-dropdown>
          </div>
        </q-td>

            
      </template>

    </q-table>


  </div>
</template>

<script setup>
import { ref } from "vue";
import router from '../router'


const columns = ref([
  { name: "id", 
    align: "left", 
    label: "id", 
    field: "id", 
    sortable: true 
  },
  {
    name: "firstname",
    align: "center",
    label: "Name",
    field: "firstname",
    sortable: true,
  },
  {
    name: "lastname",
    align: "center",
    label: "Surname",
    field: "lastname",
    sortable: true,
  },
  {
    name: "rank",
    align: "center",
    label: "Job",
    field: "rank_name",
    sortable: true,
  },
  {
    name: "phone",
    align: "center",
    label: "Phone Number",
    field: "phone",
    sortable: true,
  },
  {
    name: "email",
    align: "center",
    label: "Email Address",
    field: "email",
    sortable: true,
  },
  {
    name: "actions",
    align: "center",
    label: " ",
    field: "dropdown",
    sortable: true,
  },
]);

const rows = ref([]);

const fetchData = () => {
  fetch("http://127.0.0.1:8000/api/member/list/")
    .then(async (res) => await res.json())
    .then((result) => {
      rows.value = result;
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
