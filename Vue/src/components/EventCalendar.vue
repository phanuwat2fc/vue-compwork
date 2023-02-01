<template>
  <div class="mt-6"> 
    <q-btn color="primary" @click="addEvents = true">Add Event</q-btn>
  </div>
  <div class="full-width column">
    <q-splitter class="row" v-model="splitterModel" style="height: 450px">
      <template v-slot:before>
        <div class="q-pa-md">
          <q-date v-model="date" :events="events" event-color="orange" />
        </div>
      </template>

      <template v-slot:after>
        <a-tab-panels
          v-model="date"
          animated
          transition-prev="jump-up"
          transition-next="jump-up"
        >
          <q-tab-panel name="{{iddate}}">
            <div class="text-h4 q-mb-md">{{ iddate }}</div>
            <p>{{ contentevent }}</p>
          </q-tab-panel>
        </a-tab-panels>
      </template>
    </q-splitter>
  </div>

  <q-dialog v-model="addEvents">
    <q-card>
      <q-card-section>
        <div class="text-h6">Add Events</div>
      </q-card-section>

      <q-separator />

      <q-card-section style="max-height: 50vh" class="scroll">
        <div class="q-pa-md" style="max-width: 300px">
          <q-input filled v-model="iddate" mask="date" :rules="['date']">
            <template v-slot:append>
              <q-icon name="event" class="cursor-pointer">
                <q-popup-proxy
                  cover
                  transition-show="scale"
                  transition-hide="scale"
                >
                  <q-date v-model="iddate">
                    <div class="row items-center justify-end">
                      <q-btn v-close-popup label="Close" color="primary" flat />
                    </div>
                  </q-date>
                </q-popup-proxy>
              </q-icon>
            </template>
          </q-input>
        </div>

        <q-card-section class="q-pt-none">
          <p>เนิ้อหา</p>
          <q-input required dense v-model="contentevent" @keyup.enter="prompt = false" />
        </q-card-section>
      </q-card-section>

      <q-separator />

      <q-card-actions align="right">
        <q-btn
          flat
          label="Cancel"
          color="white"
          text-color="black"
          v-close-popup
        />
        <q-btn
          flat
          label="Accept"
          color="primary"
          v-close-popup
          @click="addcontentevent"
        />
      </q-card-actions>
    </q-card>
  </q-dialog>
</template>

<script setup>
import { ref } from "vue";


const addEvents = ref(false);
const date =ref();
const iddate = ref();
const events = iddate;


</script>
