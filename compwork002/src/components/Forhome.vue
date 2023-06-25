<template>
  <div class="column">
    <div class="container row mt-6 ml-4" style="width: 450px">
      <q-card class="my-card col" flat bordered>
        <q-card-section horizontal>
          <q-card-section class="q-pt-xs">
            <div class="text-h5 q-mt-sm q-mb-xs">{{ name }}</div>
            <div class="text-caption text-grey" style="height: 100px">
              Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
            </div>
          </q-card-section>
        </q-card-section>

        <q-separator />

        <q-card-actions class="row">
          <q-btn flat round icon="event" />
          <q-btn flat> 7:30PM </q-btn>
          <q-badge class="" rounded color="green" />
        </q-card-actions>
      </q-card>

      <q-card class="my-card col ml-4" flat bordered>
        <q-card-section horizontal>
          <q-card-section class="q-pt-xs">
            <div class="text-h5 q-mt-sm q-mb-xs">{{ name }}</div>
            <div class="text-caption text-grey" style="height: 100px">
              Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
            </div>
          </q-card-section>
        </q-card-section>

        <q-separator />

        <q-card-actions class="row">
          <q-btn flat round icon="event" />
          <q-btn flat> 7:30PM </q-btn>
          <q-badge class="" rounded color="green" />
        </q-card-actions>
      </q-card>
    </div>

    <div class="container row mt-6 ml-4" style="width: 450px">
      <q-card class="my-card col" flat bordered>
        <q-card-section horizontal>
          <q-card-section class="q-pt-xs">
            <div class="text-h5 q-mt-sm q-mb-xs">Jane</div>
            <div class="text-caption text-grey" style="height: 100px">
              Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
            </div>
          </q-card-section>
        </q-card-section>

        <q-separator />

        <q-card-actions class="row">
          <q-btn flat round icon="event" />
          <q-btn flat> 7:30PM </q-btn>
          <q-badge class="" rounded color="green" />
        </q-card-actions>
      </q-card>

      <q-card class="my-card col ml-4" flat bordered>
        <q-card-section horizontal>
          <q-card-section class="q-pt-xs">
            <div class="text-h5 q-mt-sm q-mb-xs">Jane</div>
            <div class="text-caption text-grey" style="height: 100px">
              Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
            </div>
          </q-card-section>
        </q-card-section>

        <q-separator />

        <q-card-actions class="row">
          <q-btn flat round icon="event" />
          <q-btn flat> 7:30PM </q-btn>
          <q-badge class="" rounded color="red" />
        </q-card-actions>
      </q-card>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";

const Titlename = ref("WorkName");
const name = ref("Marry");
</script>
