<template>
  <div>
    <h2>Add jobs</h2>
    <form @submit.prevent="submit">
      <input v-model="title" placeholder="title" required />
      <input v-model="description" placeholder="description" required />
      <input v-model="company" placeholder="company" required />
      <input v-model="salary" placeholder="salary" required />
      <input v-model="is_active" placeholder="is_active" required />
      <button type="submit">Add</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return { title: '', description: '' , company:'', salary:'', is_active:'' }
  },
  methods: {
    submit() {
      fetch('http://127.0.0.1:8000/jobposting/add/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title: this.title, description: this.description, company :this.company,
          salary :this.salary, is_active:this.is_active })
      })
      .then(res => res.json())
      .then(() => {
        this.title = ''
        this.description = ''
        this.company = ''
        this.salary = ''
        this.is_active = ''

        alert('job added')
      })
    }
  }
}
</script>
