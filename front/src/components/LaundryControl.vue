<template>
  <v-app>
    <!-- サイドバー -->
    <v-navigation-drawer app v-model="drawer" class="navigation-drawer">
      <v-list dense class="settings-list">
        <v-list-item class="pt-0">
          <v-list-item-content>
            <v-list-item-title class="list-title">設定</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item>
          <v-list-item-content>
            <v-select
              v-model="notificationMethod"
              :items="notificationMethods"
              label="通知方法"
              class="select-item"
            ></v-select>
          </v-list-item-content>
        </v-list-item>
        <v-list-item v-if="notificationMethod === 'Email'">
          <v-list-item-content>
            <v-text-field
              v-model="emailAddress"
              label="メールアドレス"
              type="email"
              class="input-item"
            ></v-text-field>
          </v-list-item-content>
        </v-list-item>
        <v-list-item v-if="notificationMethod === 'LINE'">
          <v-list-item-content>
            <v-text-field
              v-model="lineId"
              label="LINE ID"
              class="input-item"
            ></v-text-field>
          </v-list-item-content>
        </v-list-item>
        <v-list-item>
          <v-text-field
            v-model="location"
            label="住んでいる地域"
            class="input-item"
          ></v-text-field>
        </v-list-item>
        <v-divider class="my-2"></v-divider>
        <v-list-item>
          <v-list-item-content>
            <v-list-item-title class="list-title">洗濯履歴</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item v-for="history in laundryHistory" :key="history.id">
          <v-list-item-content>
            <v-list-item-title>{{ history.date }}</v-list-item-title>
            <v-list-item-subtitle>{{ history.details }}</v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar app color="primary" dark>
      <v-toolbar-title class="header-title">洗濯物アプリ</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn icon @click.stop="drawer = !drawer">
        <v-icon>mdi-menu</v-icon>
      </v-btn>
    </v-app-bar>

    <v-main>
      <v-container class="d-flex align-center justify-center fill-height">
        <v-card class="mx-auto pa-5" max-width="500" min-width="350">
          <v-card-text class="text-center" v-if="!isWashing">
            <v-icon size="64" class="icon-centered">mdi-washing-machine</v-icon>
            <v-btn
              color="secondary"
              @click="startLaundry"
              large
              class="ma-2"
              max-width="100%"
            >
              <v-icon left>mdi-play-circle</v-icon>
              洗濯開始
            </v-btn>
          </v-card-text>
          <v-card-text v-else class="d-flex align-center justify-center flex-column">
            <v-icon size="64" class="mr-4">mdi-washing-machine</v-icon>
            <div class="text-left">
              <p>残り時間: {{ remainingTime }}</p>
              <p>完了予測時間: {{ completionTime }}</p>
            </div>
            <div class="action-buttons mt-4">
              <v-btn color="error" @click="cancelLaundry">中止</v-btn>
              <v-btn color="success" @click="completeLaundry">完了</v-btn>
            </div>
          </v-card-text>
        </v-card>
      </v-container>
    </v-main>

    <v-footer app color="primary" dark>
      <v-col class="text-center white--text" cols="12">
        &copy; 2024 洗濯物アプリ
      </v-col>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  data() {
    return {
      drawer: false,
      completionTime: null,
      remainingTime: null,
      notificationMethod: null,
      notificationMethods: ['LINE', 'Email'],
      emailAddress: '',
      lineId: '',
      location: '',
      isWashing: false,
      laundryHistory: [
        { id: 1, date: '2024-07-01', details: '洗濯完了 - 10:00' },
        { id: 2, date: '2024-07-02', details: '洗濯完了 - 11:00' },
      ],
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
        this.remainingTime = data.remainingTime;
      } catch (error) {
        console.error('Error starting laundry:', error);
        this.isWashing = false;
      }
    },
    cancelLaundry() {
      this.isWashing = false;
      this.completionTime = null;
      this.remainingTime = null;
    },
    completeLaundry() {
      this.isWashing = false;
      this.completionTime = null;
      this.remainingTime = null;
    },
  },
};
</script>

<style scoped>
body {
  font-family: 'Roboto', sans-serif;
  background-color: #f5f5f5;
  color: #333;
  margin: 0;
  padding: 0;
}

.header-title {
  font-weight: bold;
}

.navigation-drawer {
  background-color: #fafafa;
}

.settings-list {
  margin-top: 0;
  padding-top: 0;
}

.list-title {
  font-size: 1.2rem;
  font-weight: 500;
}

.select-item,
.input-item {
  margin-bottom: 16px;
}

.mx-auto {
  margin-left: auto;
  margin-right: auto;
}

.v-card-text .v-icon.icon-centered {
  font-size: 64px;
  margin-bottom: 20px;
}

.v-card-text .v-btn {
  font-size: 18px;
  width: 100%;
  max-width: 250px;
}

.v-card-text .v-btn .v-icon {
  font-size: 32px;
}

.v-card-text .text-left {
  text-align: left;
}

.action-buttons {
  display: flex;
  gap: 10px;
}

.mt-4 {
  margin-top: 16px;
}

.my-2 {
  margin-top: 8px;
  margin-bottom: 8px;
}

.pt-0 {
  padding-top: 0;
}
</style>
