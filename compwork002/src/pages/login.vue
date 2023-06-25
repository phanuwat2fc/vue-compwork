<template>
    <div>
      
      <div class="container mx-auto bg-[#06283D] border-2 border-white h-[36rem] mt-20">
        <div class="flex flex-col text-center m-14">
          <label class="text-4xl font-mono font-bold mt-16 text-white" >COMPWORK</label>
        
          <form class="mt-8 text-center" @submit="onLogin">
            <div class="relative z-0 mb-6 w-full group">
              <input
                required
                v-model="email"
                type="user"
                class="block py-2.5 px-0 w-full text-lg text-white bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-cyan-400 peer"
                placeholder=" "
              />
              <label
                for="floating_email"
                class="peer-focus:font-medium absolute left-6 text-base text-white dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:left-0 peer-focus:text-white peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6"
                >Email</label
              >
            </div>
            <div class="relative z-0 mb-6 w-full group">
              <input
                required
                v-model="password"
                type="password"
                placeholder=" "
                class="block py-2.5 px-0 w-full text-lg text-white bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-cyan-400 peer"
              />
              <label
                for="floating_password"
                class="peer-focus:font-medium absolute left-6 text-base text-white dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:left-0 peer-focus:text-white peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6"
                >Password</label
              >
            </div>
            <div class="flex justify-between items-center mt-4 mb-4">
              <div>
                <input
                v-model="remember"
                  id="default-checkbox"
                  type="checkbox"
                  value=""
                  class="w-4 h-4 mt-2 text-blue-600 bg-gray-100 rounded border-gray-300 focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600"
                />
                <label
                  for="default-checkbox"
                  class="ml-2 mb-2 text-sm font-medium text-white dark:text-gray-300"
                  >Remember me</label
                >
              </div>
              
            </div>
  
            <button
              type="submit"
              class="relative sm:px-26 md:px-30 inline-flex items-center justify-center p-0.5 mb-2 mr-2 overflow-hidden text-sm font-medium text-gray-900 rounded-lg group bg-gradient-to-br from-cyan-500 to-blue-500 group-hover:from-cyan-500 group-hover:to-blue-500 hover:text-blue  focus:ring-4 focus:outline-none focus:ring-cyan-200"
            >
              <p
                class="relative px-40 min-w-min py-2.5 transition-all ease-in duration-75 bg-white  rounded-md group-hover:bg-opacity-0"
                >Login</p>
            </button>
          </form>
        </div>
      </div>
    </div>
  </template>
  
<script >
import { useRouter } from 'vue-router'

</script>
  
<style>
  
</style>
  