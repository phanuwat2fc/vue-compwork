<template>
  <div class="flex flex-row">
    <Sidebar />
    <div class="px-4 py-4">
      <label class="text-2xl font-bold">Notification</label>
      <Noti/>
      <div class="overflow-y-auto h-42">
        <label for="" class="text-2xl font-bold">Check-in and check-out time</label>
        <Checkin/>
        <Checkout/>
      </div>
      
    </div>
  </div>
</template>
<script setup>
import Sidebar from "../components/Sidebar.vue";
import Checkin from '../components/Checkin.vue'
import Checkout from '../components/Checkout.vue'
import Noti from '../components/Noti.vue'
import {useRouter} from 'vue-router'

</script>
<style lang=""></style>
