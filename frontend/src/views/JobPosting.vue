<template>
  <div>
    <h2>job List</h2>
    <ul>
      <li v-for="job in jobposting" :key="job.id">
        {{ job.title }} {{ job.description }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return { jobposting: [] }
  },
  mounted() {
    fetch('http://127.0.0.1:8000/jobposting/')
      .then(res => res.json())
      .then(data => { this.jobposting = data })
  }
}
</script>
