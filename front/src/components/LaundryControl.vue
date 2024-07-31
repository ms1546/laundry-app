<template>
  <v-app>
    <v-main>
      <v-container>
        <v-row justify="center">
          <v-col cols="12" md="8">
            <v-card class="mx-auto" max-width="400">
              <v-card-title class="headline">
                <v-icon class="mr-2">mdi-washing-machine</v-icon>
                洗濯コントロール
              </v-card-title>
              <v-card-text>
                <v-btn color="primary" @click="startLaundry">
                  <v-icon class="mr-2">mdi-play-circle</v-icon>
                  洗濯開始
                </v-btn>
                <v-alert v-if="dryingTime !== null" type="info" class="mt-4">
                  予測乾燥時間: {{ dryingTime }} 時間
                </v-alert>
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
    <v-footer app color="primary" dark>
      <span class="white--text">&copy; 2024 洗濯物アプリ</span>
    </v-footer>
  </v-app>
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
        this.dryingTime = data.dryingTime;
      } catch (error) {
        console.error('Error starting laundry:', error);
      }
    },
  },
};
</script>

<style scoped>
.laundry-control {
  margin-top: 20px;
}
.v-icon {
  vertical-align: middle;
}
</style>
