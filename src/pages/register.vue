<template>
    <div class="">
      <div class="px-4 py-4 flex flex-col ">
        <div class="q-pa-md" style="max-width: 100%">
          <q-form  class="q-gutter-md">
            <label class="text-2xl font-bold ">สมัครใช้งาน</label>
            <q-input v-model="register.email" label="Email" />
            <q-input v-model="register.password" type="password"  label="Password" />
            <q-input v-model="register.firstname" label="Firstname" />
            <q-input v-model="register.lastname" label="Lastname" />
            <q-input v-model="register.team" label="Team" />
            <q-input v-model="register.rank" label="ตำแหน่งงาน" />
            <!-- <q-input v-model="confirmpassword" type="password"  label="Confirmpassword" /> -->
            <q-btn color="white" text-color="black" label="Back" to="/" />
            <q-btn label="Submit" @click="add_users" color="primary" />
          </q-form>
        </div>
      </div>
    </div>
  </template>

<script setup>
import { ref } from 'vue';
import axios  from 'axios';
import router from '../router';

const register = ref({
  email: '',
  password: '',
  firstname: '',
  lastname: '',
  team: '',
  rank: '',
})

const add_users = async () => {
  await axios.post('http://localhost:8000/api/user/create/',{
    "email":register.value.email,
    "password":register.value.password,
    "name":register.value.firstname,
    "l_name":register.value.lastname,
    "employee_type":register.value.rank,
    "team":register.value.team,
  })
  .then((res) => {
    alert ('Succeed')
     router.push('/')
    console.log(res);
  }).catch((err) => {
    console.log(err);
  })
}




</script>