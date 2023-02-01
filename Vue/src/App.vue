<template>
  <q-layout view="hHh lpR fFf">
    <q-header elevated class="bg-[#06283D] text-white">
      <q-toolbar>
        <q-btn dense flat round icon="menu" @click="toggleLeftDrawer" />

        <q-toolbar-title>
          <q-avatar>
            <img src="https://sv1.picz.in.th/images/2022/12/14/GmGSbN.png" />
          </q-avatar>
          COMPWORK
        </q-toolbar-title>
        <q-btn flat color="red" label="Log out" glossy to="/" />
      </q-toolbar>
    </q-header>

    <q-drawer
      show-if-above
      v-model="leftDrawerOpen"
      side="left"
      class="bg-[#06283D]"
      bordered
      :breakpoint="400"
    >
      <div class="q-pa-md" style="height: calc(100% - 150px); margin-top: 150px; border-right: 1px solid #ddd">
        <div class="q-pa-md q-gutter-md column justify-start">
          <q-btn
            color="#06283D"
            class="full-width size-xl"
            label="Dashboard"
            to="/index"
          />
          <q-btn
            color="#06283D"
            class="full-width"
            label="Member"
            to="/member"
          />
          <q-btn
            color="#06283D"
            class="full-width"
            label="Work From Home"
            to="/workhome"
          />
          <q-btn
            color="#06283D"
            class="full-width"
            label="Calendar"
            to="/calendar"
          />
        </div>

      </div>

          <q-img class="absolute-top" src="https://cdn.quasar.dev/img/material.png" style="height: 150px">
          <div class="absolute-bottom bg-transparent">
            <q-avatar size="56px" class="q-mb-sm">
              <img src="https://cdn.quasar.dev/img/boy-avatar.png">
            </q-avatar>
            <div class="text-weight-bold">Razvan Stoenescu</div>
            <div>@rstoenescu</div>
          </div>
        </q-img>
        

    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import { ref } from "vue";

export default {
  setup() {
    const leftDrawerOpen = ref(false);
    return {
      leftDrawerOpen,
      toggleLeftDrawer() {
        leftDrawerOpen.value = !leftDrawerOpen.value;
      },
    };
  },
};
</script>
