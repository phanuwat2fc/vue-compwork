<template>

    <div class="flex flex-row ">
        <Navbar/>
        <div class="px-4 py-4 flex flex-col">
            <label class="text-2xl font-bold">Member</label>
            <listMember/>
            
            
        </div>
    </div>
</template>
<script setup>

import Navbar from '../components/Navbar.vue';
import listMember from '../components/listmember.vue';

</script>
<style lang="">
    
</style>