<template>
    <div>
      <div class="flex flex-col justify-between">
        <aside class="w-64" aria-label="Sidebar">
          <div class="h-screen py-4 px-4 bg-[#06283D] dark:bg-sky-300">
            <ul class="space-y-2">
              <li>
                <a
                  href="#"
                  class="flex items-center p-2 text-base font-normal text-gray-900 rounded-lg  hover:bg-sky-300 "
                >
                  <svg
                    aria-hidden="true"
                    class="w-6 h-6 text-white transition duration-75  group-hover:text-black "
                    fill="currentColor"
                    viewBox="0 0 20 20"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <path d="M2 10a8 8 0 018-8v8h8a8 8 0 11-16 0z"></path>
                    <path d="M12 2.252A8.014 8.014 0 0117.748 8H12V2.252z"></path>
                  </svg>
                  <span class="ml-3 text-white"><router-link to="/index">Dashboard</router-link></span>
                </a>
              </li>
              <li >
                <a class="flex items-center p-2 text-base font-normal text-gray-900 rounded-lg  hover:bg-sky-300 "><svg aria-hidden="true" class="flex-shrink-0 w-6 h-6 text-white transition duration-75  group-hover:text-gray-900 " fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                    <path
                      fill-rule="evenodd"
                      d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z"
                      clip-rule="evenodd"
                    ></path>
                  </svg>
                  <span class="flex-1 ml-3 text-white whitespace-nowrap"
                    ><router-link to="/member">Member</router-link></span
                  >
                </a>
              </li>
              <li>
                <a
                  href="#"
                  class="flex items-center p-2 text-base font-normal text-gray-900 rounded-lg  hover:bg-sky-300 "
                >
                  <svg
                    aria-hidden="true"
                    class="flex-shrink-0 w-6 h-6 text-white transition duration-75  group-hover:text-gray-900 "
                    fill="currentColor"
                    viewBox="0 0 20 20"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <path
                      d="M8.707 7.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l2-2a1 1 0 00-1.414-1.414L11 7.586V3a1 1 0 10-2 0v4.586l-.293-.293z"
                    ></path>
                    <path
                      d="M3 5a2 2 0 012-2h1a1 1 0 010 2H5v7h2l1 2h4l1-2h2V5h-1a1 1 0 110-2h1a2 2 0 012 2v10a2 2 0 01-2 2H5a2 2 0 01-2-2V5z"
                    ></path>
                  </svg>
                  <span class="flex-1 ml-3 text-white whitespace-nowrap"
                    ><router-link to="/workhome">Work From Home</router-link></span
                  >
                </a>
              </li>
              <li>
                <a
                  class="flex items-center p-2 text-base font-normal text-gray-900 rounded-lg  hover:bg-sky-300 "
                >
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="16"
                    height="16"
                    fill="currentColor"
                    class="flex-shrink-0 w-6 h-6 text-white transition duration-75  group-hover:text-gray-900 "
                    viewBox="0 0 16 16"
                  >
                    <path
                      d="M3.5 0a.5.5 0 0 1 .5.5V1h8V.5a.5.5 0 0 1 1 0V1h1a2 2 0 0 1 2 2v11a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V3a2 2 0 0 1 2-2h1V.5a.5.5 0 0 1 .5-.5zM1 4v10a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V4H1z"
                    />
                  </svg>
                  <span class="flex-1 ml-3 text-white whitespace-nowrap"
                    ><router-link to="/calendar">Calendar</router-link></span
                  >
                </a>
              </li>
            </ul>
            <div class="flex flex-row mt-96">
              <img
                class="w-10 h-10 rounded-full"
                src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png"
                alt=""
              />
              <label for="" class="px-4  text-white font-lg">Name : Phanuwat Seawaka</label>
            </div>
            <li>
              <a
                class="flex items-center p-2 text-base font-normal  rounded-lg  hover:bg-red-300 "
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="flex-shrink-0 w-6 h-6 text-white transition duration-75  group-hover:text-gray-900 "
                  fill="currentColor"
                  viewBox="0 0 16 16"
                >
                  <path
                    fill-rule="evenodd"
                    d="M6 12.5a.5.5 0 0 0 .5.5h8a.5.5 0 0 0 .5-.5v-9a.5.5 0 0 0-.5-.5h-8a.5.5 0 0 0-.5.5v2a.5.5 0 0 1-1 0v-2A1.5 1.5 0 0 1 6.5 2h8A1.5 1.5 0 0 1 16 3.5v9a1.5 1.5 0 0 1-1.5 1.5h-8A1.5 1.5 0 0 1 5 12.5v-2a.5.5 0 0 1 1 0v2z"
                  />
                  <path
                    fill-rule="evenodd"
                    d="M.146 8.354a.5.5 0 0 1 0-.708l3-3a.5.5 0 1 1 .708.708L1.707 7.5H10.5a.5.5 0 0 1 0 1H1.707l2.147 2.146a.5.5 0 0 1-.708.708l-3-3z"
                  />
                </svg>
                <span class="ml-3 text-white"><router-link to="/" >Logout</router-link></span>
              </a>
            </li>
          </div>
        </aside>
      </div>
    </div>
  </template>
  
<script setup>

</script>

  <style scoped></style>
  