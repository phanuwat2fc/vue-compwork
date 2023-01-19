<template>
  <div>
    <div class="overflow-y-auto h-42 px-4 py-4">
      <div
        id="alert-additional-content-1"
        class="p-4 mb-4 border border-blue-300 rounded-lg bg-blue-50 dark:bg-blue-300"
        role="alert"
      >
        <div class="flex items-center">
          <svg
            aria-hidden="true"
            class="w-5 h-5 mr-2 text-blue-900"
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
          <h3 class="text-lg font-medium text-blue-900">
            This is a info alert
          </h3>
        </div>
        <div class="mt-2 mb-4 text-sm text-blue-900">
          More info about this info alert goes here. This example text is going
          to run a bit longer so that you can see how spacing within an alert
          works with this kind of content.
        </div>
        <div class="flex">
          <button
            type="button"
            class="text-green-600 bg-transparent border border-green-600 hover:bg-green-600 hover:text-white focus:ring-4 focus:outline-none focus:ring-blue-200 font-medium rounded-lg text-xs px-3 py-1.5 mr-2 text-center inline-flex items-center dark:bg-blue-800 dark:hover:bg-blue-900"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="16"
              height="16"
              fill="currentColor"
              class="bi bi-check-lg "
              viewBox="0 0 16 16"
            >
              <path
                d="M12.736 3.97a.733.733 0 0 1 1.047 0c.286.289.29.756.01 1.05L7.88 12.01a.733.733 0 0 1-1.065.02L3.217 8.384a.757.757 0 0 1 0-1.06.733.733 0 0 1 1.047 0l3.052 3.093 5.4-6.425a.247.247 0 0 1 .02-.022Z"
              />
            </svg>
            Confirm
          </button>
          <button
            data-modal-toggle="popup-modal"
            type="button"
            class="text-red-900 bg-transparent border border-red-900 hover:bg-red-900 hover:text-white focus:ring-4 focus:outline-none focus:ring-red-300 font-medium rounded-lg text-xs px-3 py-1.5 text-center dark:border-red-800 dark:text-red-800 dark:hover:text-white"
            data-dismiss-target="#alert-additional-content-2"
            aria-label="Close"
          >
            Delete
          </button>
        </div>
        
      </div>
      <div
        id="alert-additional-content-2"
        class="p-4 mb-4 border border-red-300 rounded-lg bg-red-50 dark:bg-red-200"
        role="alert"
      >
        <div class="flex items-center">
          <svg
            aria-hidden="true"
            class="w-5 h-5 mr-2 text-red-900 dark:text-red-800"
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
          <h3 class="text-lg font-medium text-red-900 dark:text-red-800">
            This is a danger alert
          </h3>
        </div>
        <div class="mt-2 mb-4 text-sm text-red-900 dark:text-red-800">
          More info about this info danger goes here. This example text is going
          to run a bit longer so that you can see how spacing within an alert
          works with this kind of content.
        </div>
        <div class="flex">
            <button
            type="button"
            class="text-green-600 bg-transparent border border-green-600 hover:bg-green-600 hover:text-white focus:ring-4 focus:outline-none focus:ring-blue-200 font-medium rounded-lg text-xs px-3 py-1.5 mr-2 text-center inline-flex items-center dark:bg-blue-800 dark:hover:bg-blue-900"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="16"
              height="16"
              fill="currentColor"
              class="bi bi-check-lg "
              viewBox="0 0 16 16"
            >
              <path
                d="M12.736 3.97a.733.733 0 0 1 1.047 0c.286.289.29.756.01 1.05L7.88 12.01a.733.733 0 0 1-1.065.02L3.217 8.384a.757.757 0 0 1 0-1.06.733.733 0 0 1 1.047 0l3.052 3.093 5.4-6.425a.247.247 0 0 1 .02-.022Z"
              />
            </svg>
            Confirm
          </button>
          <button
            type="button"
            class="text-red-900 bg-transparent border border-red-900 hover:bg-red-900 hover:text-white focus:ring-4 focus:outline-none focus:ring-red-300 font-medium rounded-lg text-xs px-3 py-1.5 text-center dark:border-red-800 dark:text-red-800 dark:hover:text-white"
            data-dismiss-target="#alert-additional-content-2"
            aria-label="Close"
          >
            Delete
          </button>
        </div>
      </div>
      <div
        id="alert-additional-content-3"
        class="p-4 mb-4 border border-green-300 rounded-lg bg-green-50 dark:bg-green-200"
        role="alert"
      >
        <div class="flex items-center">
          <svg
            aria-hidden="true"
            class="w-5 h-5 mr-2 text-green-700 dark:text-green-800"
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
          <h3 class="text-lg font-medium text-green-700 dark:text-green-800">
            This is a success alert
          </h3>
        </div>
        <div class="mt-2 mb-4 text-sm text-green-700 dark:text-green-800">
          More info about this info success goes here. This example text is
          going to run a bit longer so that you can see how spacing within an
          alert works with this kind of content.
        </div>
        <div class="flex">
            <button
            type="button"
            class="text-green-600 bg-transparent border border-green-600 hover:bg-green-600 hover:text-white focus:ring-4 focus:outline-none focus:ring-blue-200 font-medium rounded-lg text-xs px-3 py-1.5 mr-2 text-center inline-flex items-center dark:bg-blue-800 dark:hover:bg-blue-900"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="16"
              height="16"
              fill="currentColor"
              class="bi bi-check-lg "
              viewBox="0 0 16 16"
            >
              <path
                d="M12.736 3.97a.733.733 0 0 1 1.047 0c.286.289.29.756.01 1.05L7.88 12.01a.733.733 0 0 1-1.065.02L3.217 8.384a.757.757 0 0 1 0-1.06.733.733 0 0 1 1.047 0l3.052 3.093 5.4-6.425a.247.247 0 0 1 .02-.022Z"
              />
            </svg>
            Confirm
          </button>
          <button
            type="button"
            class="text-red-900 bg-transparent border border-red-900 hover:bg-red-900 hover:text-white focus:ring-4 focus:outline-none focus:ring-red-300 font-medium rounded-lg text-xs px-3 py-1.5 text-center dark:border-red-800 dark:text-red-800 dark:hover:text-white"
            data-dismiss-target="#alert-additional-content-2"
            aria-label="Close"
          >
            Delete
          </button>
        </div>
      </div>
    </div>
    
  </div>
</template>
<script setup>

</script>
<style lang=""></style>
