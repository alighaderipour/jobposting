<script>
import JobCard from '@/components/JobCard.vue';

export default {
  components: { JobCard },
  data() {
    return {
      jobposting: [],
      activeJobs: [],
      notActiveJobs: [],
    };
  },
  mounted() {
    fetch('http://127.0.0.1:8000/jobposting/')
      .then(res => res.json())
      .then(data => {
        this.jobposting = data.all;
        this.activeJobs = data.active;
        this.notActiveJobs = data.inactive;
      });
  },
};
</script>
<template>
  <h1 style="text-align: center">Job Board</h1>
  <div class="container">
    <!-- All Job Postings -->
    <div class="column">
      <h2>All Job Postings</h2>
      <div v-if="jobposting.length">
        <JobCard v-for="(job, index) in jobposting" :key="index" :job="job" />
      </div>
      <p v-else>No job postings found.</p>
    </div>

    <!-- Active Job Postings -->
    <div class="column">
      <h2>Active Job Postings</h2>
      <div v-if="activeJobs.length">
        <JobCard
          v-for="(job, index) in activeJobs"
          :key="index"
          :job="job"
          :showSalary="true"
        />
      </div>
      <p v-else>No active job postings.</p>
    </div>

    <!-- Not Active Job Postings -->
    <div class="column">
      <h2>Not Active Job Postings</h2>
      <div v-if="notActiveJobs.length">
        <JobCard
          v-for="(job, index) in notActiveJobs"
          :key="index"
          :job="job"
        />
      </div>
      <p v-else>No inactive job postings.</p>
    </div>
  </div>
</template>
<style scoped>
.container {
  display: flex;
  gap: 20px;
}
.column {
  flex: 1;
  border: 1px solid #ccc;
  padding: 10px;
}
</style>
