<template>
  <div class="job">
    <strong>{{ job.title }}</strong><br />
    {{ job.description }}<br />
    <div v-if="showSalary && job.salary">
      {{ job.salary }}
    </div>
    <router-link
      :to="`/jobposting/details/${job.id}`"
      class="details-button"
    >
      More Details
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'JobCard',
  props: {
    job: Object,
    showSalary: {
      type: Boolean,
      default: false,
    },
  },
};
</script>

<style scoped>
.job {
  margin-bottom: 15px;
}
.details-button {
  margin-top: 5px;
  display: inline-block;
  background-color: #007bff;
  color: white;
  padding: 4px 8px;
  border-radius: 4px;
  text-decoration: none;
}
.details-button:hover {
  background-color: #0056b3;
}
</style>
