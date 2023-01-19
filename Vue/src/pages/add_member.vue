<template>
  <div class="flex flex-row">
    <Sidebar />
    <div class="px-4 py-4 flex flex-col">
      <label class="text-2xl font-bold">Create Member</label>

      <div class="w-full pt-6 pl-12">
        <div class="border-2 p-8 w-96 bg-[#06283D] w-[36rem] opacity-75">
          <form @submit="onSubmit">
            <div class="relative z-0 w-full mb-6 group">
              <input
                v-model="email"
                type="email"
                class="block py-2.5 px-0 w-full text-sm text-white bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-400 peer"
                placeholder=" "
                required
              />
              <label
                for="floating_email"
                class="peer-focus:font-medium absolute text-sm text-white duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:left-0 peer-focus:text-blue-400 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6"
                >Email address</label
              >
            </div>

            <div class="relative z-0 w-full mb-6 group">
              <input
                v-model="fname"
                type="text"
                class="block py-2.5 px-0 w-full text-sm text-white bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-400 peer"
                placeholder=" "
                required
              />
              <label
                for=""
                class="peer-focus:font-medium absolute text-sm text-white duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:left-0 peer-focus:text-blue-400 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6"
                >Frist Name</label
              >
            </div>

            <div class="relative z-0 w-full mb-6 group">
              <input
                v-model="lname"
                type="text"
                class="block py-2.5 px-0 w-full text-sm text-white bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-400 peer"
                placeholder=" "
                required
              />
              <label
                for=""
                class="peer-focus:font-medium absolute text-sm text-white duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:left-0 peer-focus:text-blue-400 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6"
                >Last name</label
              >
            </div>


            <div class="relative z-0 w-full mb-6 group">
              <input
                v-model="phone"
                type="tel"
                class="block py-2.5 px-0 w-full text-sm text-white bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-400 peer"
                placeholder=" "
                required
              />
              <label
                for=""
                class="peer-focus:font-medium absolute text-sm text-white duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:left-0 peer-focus:text-blue-400 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6"
                >Phone number</label
              >
            </div>

            <div class="relative z-0 w-full mb-6 group">
              <input
                v-model="rank"
                type="text"
                class="block py-2.5 px-0 w-full text-sm text-white bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-400 peer"
                placeholder=" "
                required
              />
              <label
                for=""
                class="peer-focus:font-medium absolute text-sm text-white duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:left-0 peer-focus:text-blue-400 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6"
                >ตำแหน่ง</label
              >
            </div>
          </form>
        </div>

        <div class="flex mt-6">
          <q-btn color="red-7">Back</q-btn>
          <q-btn class="q-pl-md" color="primary" type="submit" @click="onSubmit">Submit</q-btn>
        </div>

      </div>

    </div>
  </div>
</template>
<script setup>
import Sidebar from "../components/Sidebar.vue";
import listmember from "../components/listmember.vue";
import { ref } from "vue";
import router from "../router";


const fname = ref('Phanuwat')
const lname = ref('Seawaka')
const rank = ref('Front-End')
const phone = ref('0987571386')
const email = ref('big@gmail.com')


const onSubmit = () =>{
  var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");

var raw = JSON.stringify({
  "fname": fname.value,
  "lname": lname.value,
  "rank": rank.value,
  "phone": phone.value,
  "email": email.value
});

var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};

fetch("https://project-se-api.biglove1.repl.co/members", requestOptions)
  .then(response => response.json())
  .then(result => {
    alert(result.message)
    if (result.status === 'ok'){
      router.push('/member')
    }
  })

  .catch(error => console.log('error', error));
}
</script>
<style lang=""></style>
