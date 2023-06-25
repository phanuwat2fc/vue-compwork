<template>
    <div class="flex flex-row">
      <div class="px-4 py-4 flex flex-col">
        <label class="text-2xl font-bold">Edit Member</label>
        <div class="q-pa-md" style="max-width: 100%">
          <q-form @submit="onSubmit" class="q-gutter-md">
            <q-input v-model="email" label="Email" />
            <q-input v-model="firstname" label="Firstname" />
            <q-input v-model="lastname" label="Lastname" />
            <q-input v-model="phone" label="Phone" />
            <q-input v-model="rank" label="ตำแหน่งงาน" />

            <q-btn color="white" text-color="black" label="Back" to="/member" />
            <q-btn color="red"  label="delete" />
            <q-btn label="Submit" type="submit" color="primary" />
          </q-form>
        </div>
      </div>
    </div>
  </template>
<script setup>



</script>
<style lang="">
    
</style>