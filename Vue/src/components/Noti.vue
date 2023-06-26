<template>
  <div class="q-pa-md q-gutter-md">
    <q-card class="my-card ">
      <q-card-section class="bg-[#06283D] text-white">
        <div class="text-h6">Leave</div>
        <div class="text-subtitle2">By: {{name}} ตำแหน่งงาน: {{ rank }} ลาวันที่: {{ dateleave }}</div>
      </q-card-section>

      <q-card-actions  class="justify-around q-px-md">
        <q-btn flat color="primary" @click="confirm = true">Confirm</q-btn>
        <q-btn flat color="red">Delete</q-btn>
      </q-card-actions>
    </q-card>

    <q-card class="my-card ">
      <q-card-section class="bg-[#06283D] text-white">
        <div class="text-h6">Leave</div>
        <div class="text-subtitle2">By: {{name}} ตำแหน่งงาน: {{ rank }} ลาวันที่: {{ dateleave }}</div>
      </q-card-section>

      <q-card-actions  class="justify-around q-px-md">
        <q-btn flat color="primary" @click="confirm = true">Confirm</q-btn>
        <q-btn flat color="red">Delete</q-btn>
      </q-card-actions>
    </q-card>

    <q-dialog v-model="confirm" persistent>
        <q-card>
            <q-card-section>
              <span class="q-ml-sm">You want {{name}} to leave.</span>
            </q-card-section>
            <q-card-actions  align="center">
              <q-btn flat label="Yes" color="primary" v-close-popup />
              <q-btn flat label="Cancel" color="primary" v-close-popup />
            </q-card-actions>
        </q-card>
    </q-dialog>

  </div>
</template>

<script setup>
import { ref } from 'vue'

const confirm =ref(false)

const name = ref('QWEWQEQWRQWR')
const rank = ref('Front-End')
const dateleave = ref('2023/02/01')

</script>