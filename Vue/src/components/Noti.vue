<template>
  
    <div class="q-pa-md q-gutter-md" v-for="(leave,index) in leaves">
    <template v-if="leave.event_status === false">
      <q-card class="my-card" >
      <q-card-section class="bg-[#06283D] text-white">
        <div class="text-h6">{{leave.event_title}}</div>
        <div class="text-subtitle2">Name:{{ leave.owner_name }} {{ leave.owner_lname }}  Description: {{ leave.event_description }}  ลาวันที่: {{ leave.event_date }} </div>
      </q-card-section>

      <q-card-actions  class="justify-around q-px-md">
        <q-btn flat color="primary" @click="confirm_leave(leave.id)">ยอมรับ</q-btn>
        <q-btn flat color="red" @click="delete_leave(leave.id)">ปฏิเสธ</q-btn>
      </q-card-actions>
    </q-card>

    </template>

  </div>
</template>

<script setup>
import { ref , onMounted } from 'vue'
import axios from 'axios';


const leaves = ref({})
const token = localStorage.getItem('Token')

// axios
const config = {
  headers: {
    Authorization: `Token ${token}`,
  }
}


const fetch_leave = async () => {
  await axios.get('http://localhost:8000/api/leave/',config)
  .then((response) =>{
    leaves.value = response.data
    }
    ).catch((err)=>{
    console.log("leaves",err);
  })
}

const delete_leave = async (id) => {
  console.log('delete ' , id);
  await axios.delete(`http://localhost:8000/api/leave/${id}`,config)
  .then((response) => {
    confirm("You Want to Delete")
    window.location.reload()
    }).catch((err)=>{
    console.log(err);
  })
}

const confirm_leave = async(id) => {
  console.log('confirm', id);
  await axios.patch(`http://localhost:8000/api/leave/${id}/`,{
    event_status:true
  },config)
  .then((response)=>{
    confirm('You want to confirm')
    window.location.reload()
  }).catch((err)=>{
    console.log(err);
  })
  
}


onMounted(()=>fetch_leave())
</script>