<template>
  <div class="flex flex-row">
    <div class="px-4 py-4 flex flex-col">
      <label class="text-2xl font-bold">Create Member</label>
      <div class="q-pa-md" style="max-width: 100%">
        <q-form @submit="onSubmit" class="q-gutter-md">
          <q-input v-model="email" label="Email" />
          <q-input v-model="firstname" label="Firstname" />
          <q-input v-model="lastname" label="Lastname" />
          <q-input v-model="phone" label="Phone" />
          <q-input v-model="rank" label="ตำแหน่งงาน" />

          <q-btn color="white" text-color="black" label="Back" to="/member" />
          <q-btn label="Submit" type="submit" color="primary" />
        </q-form>
      </div>
    </div>
  </div>
</template>

<script setup>


import listmember from "../components/listmember.vue";
import { ref } from "vue";
import router from "../router";

const email = ref("");
const firstname = ref("");
const lastname = ref("");
const phone = ref("");
const rank = ref("");

const onSubmit = () => {
  var myHeaders = new Headers();
  myHeaders.append("Content-Type", "text/plain");

  var raw = JSON.stringify({
    "email":email.value,
    "firstname":firstname.value,
    "lastname":lastname.value,
    "phone":phone.value,
    "rank":rank.value

  });
    

  var requestOptions = {
    method: "POST",
    headers: myHeaders,
    body: raw,
    redirect: "follow",
  };

  fetch("http://127.0.0.1:8000/api/member/list/create/", requestOptions)
    .then((response) => response.json())
    .then(result => console.log(result))
    .catch((error) => console.log("error", error));
};
</script>

<style lang=""></style>
