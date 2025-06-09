<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'

const job = ref(null)
const route = useRoute()
const router = useRouter()

onMounted(async () => {
  const jobId = route.params.id

  // Simulate fetching job
  const jobData = await fetchJobById(jobId)

  if (!jobData) {
    router.replace('/jobposting/not_found')
  } else {
    job.value = jobData
  }
})

// 🔧 Simulate fake DB
async function fetchJobById(id) {
  const jobs = [
    { id: '1', title: 'Frontend Dev', description: 'Build UI', company: 'Tech Co', salary: 3000, is_active: true },
    { id: '2', title: 'Backend Dev', description: 'Build APIs', company: 'API Co', salary: 4000, is_active: false },
  ]

  return jobs.find(j => j.id === id)
}
</script>

<template>
  <div class="job-details">
    <h1>Job Details</h1>
    <div v-if="job">
      <p><strong>Title:</strong> {{ job.title }}</p>
      <p><strong>Description:</strong> {{ job.description }}</p>
      <p><strong>Company:</strong> {{ job.company }}</p>
      <p><strong>Salary:</strong> {{ job.salary }} <b>$</b></p>
      <p><strong>Availability:</strong> {{ job.is_active }}</p>
    </div>
  </div>
</template>



<style scoped>
.job-details {
  max-width: 600px;
  margin: auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 10px;
}
</style>
