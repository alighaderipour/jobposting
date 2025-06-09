<template>
  <div class="not-found">
    <div class="container">
      <div class="content">
        <h1 class="status-code">404</h1>
        <h2 class="title">Page Not Found</h2>
        <p class="message">
          The page you're looking for doesn't exist or has been moved.
        </p>
        <div class="actions">
          <router-link to="/" class="btn primary">
            Go to Homepage
          </router-link>
          <button @click="goBack" class="btn secondary">
            Go Back
          </button>
        </div>
      </div>
      <div class="illustration">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
          <path fill="#e6e6e6" d="M256,16C123.452,16,16,123.452,16,256S123.452,496,256,496,496,388.548,496,256,388.548,16,256,16ZM236,76h40V116H236ZM256,436a180,180,0,1,1,180-180A180,180,0,0,1,256,436ZM236,396h40v40H236Z"/>
          <path fill="#6c63ff" d="M256,106a30,30,0,1,0,30,30A30,30,0,0,0,256,106Zm0,290a30,30,0,1,0,30,30A30,30,0,0,0,256,396Z"/>
          <path fill="#ff6584" d="M346,256a90,90,0,1,1-90-90A90,90,0,0,1,346,256Z"/>
          <path fill="#6c63ff" d="M256,196a60,60,0,1,0,60,60A60,60,0,0,0,256,196Z"/>
        </svg>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'NotFound',
  methods: {
    goBack() {
      this.$router.go(-1);
    }
  }
}
</script>

<style scoped>
.not-found {
  min-height: 100vh;
  display: flex;
  align-items: center;
  background-color: #f9f9f9;
  padding: 2rem;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 2rem;
}

.content {
  flex: 1;
  min-width: 300px;
}

.status-code {
  font-size: 6rem;
  font-weight: 700;
  color: #2c3e50;
  margin-bottom: 1rem;
  line-height: 1;
}

.title {
  font-size: 2.5rem;
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 1.5rem;
}

.message {
  font-size: 1.25rem;
  color: #7f8c8d;
  margin-bottom: 2.5rem;
  max-width: 500px;
  line-height: 1.6;
}

.actions {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
}

.btn {
  padding: 0.75rem 1.5rem;
  border-radius: 6px;
  font-weight: 500;
  font-size: 1rem;
  text-decoration: none;
  cursor: pointer;
  transition: all 0.3s ease;
}

.primary {
  background-color: #6c63ff;
  color: white;
  border: 2px solid #6c63ff;
}

.primary:hover {
  background-color: #564fd1;
  border-color: #564fd1;
}

.secondary {
  background-color: transparent;
  color: #6c63ff;
  border: 2px solid #6c63ff;
}

.secondary:hover {
  background-color: #f0efff;
}

.illustration {
  flex: 1;
  min-width: 300px;
  max-width: 500px;
}

.illustration svg {
  width: 100%;
  height: auto;
}

@media (max-width: 768px) {
  .container {
    flex-direction: column;
    text-align: center;
  }

  .message {
    margin-left: auto;
    margin-right: auto;
  }

  .actions {
    justify-content: center;
  }
}
</style>