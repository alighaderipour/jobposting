<template>
  <div class="job-details">
    <h1>Job Details</h1>
    <div v-if="job">
      <p><strong>Title:</strong> {{ job.title }}</p>
      <p><strong>Description:</strong> {{ job.description }}</p>
      <p><strong>Company:</strong> {{ job.company }}</p>
      <p><strong>salary:</strong> {{ job.salary }} <b>$</b> </p>
      <p><strong>availability:</strong> {{ job.is_active }}</p>

    </div>
    <div v-else>
      <p>Loading job details...</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'JobPostingDetails',
  data() {
    return {
      job: null,
    };
  },
  mounted() {
    const id = this.$route.params.id;
    fetch(`http://127.0.0.1:8000/jobposting/details/${id}/`)
      .then(res => {
        if (!res.ok) {
          throw new Error("Failed to fetch job details");
        }
        return res.json();
      })
      .then(data => {
        this.job = data;
      })
      .catch(err => {
        console.error("Error fetching job details:", err);
      });
  },
  methods: {
    formatDate(dateStr) {
      const options = { year: 'numeric', month: 'long', day: 'numeric' };
      return new Date(dateStr).toLocaleDateString(undefined, options);
    }
  }
};
</script>

<style scoped>
.job-details {
  max-width: 600px;
  margin: auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 10px;
}
</style>
