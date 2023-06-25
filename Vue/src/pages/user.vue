<template>
    <div class="q-pa-md">
        <q-layout view="lHh lpr lFf" container style="height: 700px" class="shadow-2 rounded-borders">
                <q-header elevated class="bg-[#06283D] text-white">
                    <q-toolbar>
                        <q-toolbar-title>
                        <q-avatar>
                            <img src="https://sv1.picz.in.th/images/2022/12/14/GmGSbN.png" />
                        </q-avatar>
                        COMPWORK
                        </q-toolbar-title>
                        <q-btn flat color="red" label="Log out" glossy to="/" />
                    </q-toolbar>
                </q-header>

                <div class="q-pa-md" >
                    <h1>User </h1>
                    <q-btn-group spread>
                        <q-btn  color="green" label="Checkin" @click="check_in()"  />
                        <q-btn  color="red" label="Checkout"  />
                        <q-btn color="purple" label="Leave"  />
                    </q-btn-group>
                </div>

        </q-layout>
    </div>
</template>


<script setup>
import axios from 'axios';
import {ref , onMounted} from 'vue'


const token = localStorage.getItem("Token");
const user = ref({})

// axios
const config = {
  headers: {
    Authorization: `Token ${token}`,
  },
};

const check_user = async() =>{
    await axios.get(`http://localhost:8000/api/user/me/`,config)
    .then((response)=>{
        user.value = response.data
        console.log(user);
    }).catch((err)=>{
        console.log(err);
    })
}

const check_in = async()=>{
    await axios.post(`http://localhost:8000/api/check/`,{
        "check_status": true
    },config)
    .then((response)=>{
        console.log(response);
    }).catch((err)=>{
        console.log(err);
    })
}

onMounted(()=>check_user())


</script>