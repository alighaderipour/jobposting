<template>
  <div>
    <h2>Add jobs</h2>
    <form @submit.prevent="submit">
      <input v-model="title" placeholder="title" required />
      <input v-model="description" placeholder="description" required />
      <button type="submit">Add</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return { title: '', description: '' }
  },
  methods: {
    submit() {
      fetch('http://127.0.0.1:8000/jobposting/add/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title: this.title, description: this.description })
      })
      .then(res => res.json())
      .then(() => {
        this.title = ''
        this.description = ''
        alert('job added')
      })
    }
  }
}
</script>
