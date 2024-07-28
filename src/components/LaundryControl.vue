<template>
    <div class="laundry-control">
      <button @click="startLaundry">洗濯中</button>
      <p v-if="dryingTime !== null">予測乾燥時間: {{ dryingTime }} 時間</p>
    </div>
  </template>

  <script>
  export default {
    data() {
      return {
        dryingTime: null,
      };
    },
    methods: {
      async startLaundry() {
        try {
          const response = await fetch('https://your-backend-api/start-laundry', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
          });
          const data = await response.json();
          this.dryingTime = data.dryingTime; // 予測時間を表示
        } catch (error) {
          console.error('Error starting laundry:', error);
        }
      },
    },
  };
  </script>

  <style scoped>
  .laundry-control {
    text-align: center;
    margin-top: 20px;
  }

  button {
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
  }
  </style>
