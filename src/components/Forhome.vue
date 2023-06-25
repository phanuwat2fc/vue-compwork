<template>
  <div class="column" v-for="(task , index) in task">
    <div class="container row mt-6 ml-4" style="width: 450px" >
      <q-card class="my-card col" flat bordered  >
        <q-card-section horizontal>
          <q-card-section class="q-pt-xs">
            <div class="text-h5 q-mt-sm q-mb-xs">{{ task.title}}</div>
            <div class="text-caption text-grey" style="height: 100px">
              {{task.content}}
            </div>
          </q-card-section>
        </q-card-section>

        <q-separator />

        <q-card-actions class="row">
          <q-btn flat round icon="event" />
          <q-btn flat> Date end:{{ task.date_end }} </q-btn>
          <q-btn flat> Time end:{{ task.time_end }} </q-btn>
          <q-badge v-if="task.task_status === true" class="" rounded color="green" />
          <q-badge v-else class="" rounded color="red" />
        </q-card-actions>
      </q-card>

    </div>
  </div>
</template>

<script setup>
import { ref , onMounted} from "vue";
import axios from "axios";

const task = ref({})

const token = localStorage.getItem('Token')

// axios
const config = {
  headers: {
    Authorization: `Token ${token}`,
  }
}


const fetch_task = async () => {
  await axios.get('http://localhost:8000/api/task/',config)
  .then((response) =>{
        task.value = response.data
    }
    ).catch((err)=>{
    console.log("Task",err);
  })
}

onMounted(()=>fetch_task())

</script>
