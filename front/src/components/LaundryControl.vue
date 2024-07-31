<template>
  <v-app>
    <v-main>
      <v-container>
        <v-row justify="center">
          <v-col cols="12" md="8">
            <v-card class="mx-auto" max-width="500">
              <v-card-title class="headline">
                <v-icon class="mr-2">mdi-washing-machine</v-icon>
                洗濯操作
              </v-card-title>
              <v-card-text>
                <v-btn color="primary" @click="startLaundry" :disabled="isWashing">
                  <v-icon class="mr-2">mdi-play-circle</v-icon>
                  {{ isWashing ? '洗濯中...' : '洗濯開始' }}
                </v-btn>
                <v-alert v-if="completionTime" type="info" class="mt-4">
                  完了予測時間: {{ completionTime }}
                </v-alert>
                <v-form>
                  <v-select
                    v-model="notificationMethod"
                    :items="notificationMethods"
                    label="通知方法を選択"
                    class="mt-4"
                  ></v-select>
                  <v-text-field
                    v-if="notificationMethod === 'Email'"
                    v-model="emailAddress"
                    label="メールアドレス"
                    class="mt-4"
                    type="email"
                  ></v-text-field>
                  <v-text-field
                    v-if="notificationMethod === 'LINE'"
                    v-model="lineId"
                    label="LINE ID"
                    class="mt-4"
                  ></v-text-field>
                </v-form>
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {
  data() {
    return {
      completionTime: null,
      notificationMethod: null,
      notificationMethods: ['LINE', 'Email'],
      emailAddress: '',
      lineId: '',
      isWashing: false,
    };
  },
  methods: {
    async startLaundry() {
      this.isWashing = true;
      try {
        const backendUrl = '';
        const response = await fetch(backendUrl, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
        });
        const data = await response.json();
        this.completionTime = data.completionTime;
        setTimeout(() => {
          this.isWashing = false;
        }, data.estimatedDuration);
      } catch (error) {
        console.error('Error starting laundry:', error);
        this.isWashing = false;
      }
    },
  },
};
</script>
