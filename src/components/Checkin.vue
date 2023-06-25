<template>
  <div v-for="(check, index) in check">
    <template v-if="check.check_status === true">
      <div>
        <div
          class="flex p-4 mb-4 text-base text-green-700 bg-green-100 rounded-lg"
          role="alert"
        >
          <svg
            aria-hidden="true"
            class="flex-shrink-0 inline w-5 h-5 mr-3"
            fill="currentColor"
            viewBox="0 0 20 20"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              fill-rule="evenodd"
              d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z"
              clip-rule="evenodd"
            ></path>
          </svg>
          <span class="sr-only">Info</span>
          <div class="flex flex-row justify-between">
            <span class="font-medium">Check in!</span>
            <span class="font-medium pl-4">Name:{{ check.owner_name }} {{ check.owner_lname }}</span>
            <span class="font-medium pl-8">ตำแหน่งงาน:{{check.owner_employee}}</span>
            <span class="font-medium pl-8">Time:{{ check.check_in_time }}</span>
          </div>
        </div>
      </div>
    </template>

    <template v-else>
      <div>
        <div
          class="flex p-4 mb-4 text-base text-red-700 bg-red-100 rounded-lg dark:bg-red-200 dark:text-red-800"
          role="alert"
        >
          <svg
            aria-hidden="true"
            class="flex-shrink-0 inline w-5 h-5 mr-3"
            fill="currentColor"
            viewBox="0 0 20 20"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              fill-rule="evenodd"
              d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z"
              clip-rule="evenodd"
            ></path>
          </svg>
          <span class="sr-only">Info</span>
          <div>
            <div class="flex flex-row justify-between">
              <span class="font-medium">Check out!</span>
              <span class="font-medium pl-4">Name:{{ check.owner_name }} {{ check.owner_lname }}</span>
              <span class="font-medium pl-8">ตำแหน่งงาน:{{check.owner_employee}}</span>
              <span class="font-medium pl-8"
                >Time:{{ check.check_out_time }}</span
              >
            </div>
          </div>
        </div>
      </div>
    </template>
  </div>
</template>

<script setup>
import { ref, onMounted,} from "vue";
import axios from "axios";

const token = localStorage.getItem("Token");

// axios
const config = {
  headers: {
    Authorization: `Token ${token}`,
  },
};

const check = ref();


const fetch_check = async () => {
  await axios
    .get("http://localhost:8000/api/check/", config)
    .then((response) => {
      check.value = response.data;
    })
    .catch((err) => {
      console.log("Check", err);
    });
};


onMounted(() => {
  fetch_check();
});
</script>
<style></style>
