<template>
  <div class="background">
    <v-app id="clear">

      <v-app-bar color="transparent" absolute flat>
        <v-text class="tb-text ml-5">Skoolit.</v-text>
        <v-spacer></v-spacer>

        <v-btn color="transparent" depressed>
          <v-text class="tb-btn-text">Home</v-text>
        </v-btn>

        <v-btn color="transparent" depressed>
          <v-text class="tb-btn-text">Sobre</v-text>
        </v-btn>

        <v-btn class="mr-5" color="transparent" depressed>
          <v-text class="tb-btn-text">Contato</v-text>
        </v-btn>
      </v-app-bar>

    </v-app>
  </div>
</template>

<script>

export default {
  name: 'App',

  components: {
  },

  data: () => ({
    //
  }),
};
</script>

<style>
  .background {
    background-image: url('./assets/login-background.svg');
    background-size: cover;
    background-position: center center;
    background-repeat: no-repeat;
    background-attachment: fixed;
  }

  .tb-text {
    font-family: Segoe UI,Frutiger,Frutiger Linotype,Dejavu Sans,Helvetica Neue,Arial,sans-serif;
    font-weight: bold;
    color: white
  }

  .tb-btn-text {
    font-family: Segoe UI,Frutiger,Frutiger Linotype,Dejavu Sans,Helvetica Neue,Arial,sans-serif;
    font-weight: bold;
    font-size: 12px;
    color:gray
  }

  /*esvazia o background de v-app pra poder mostrar a imagem de fundo*/
  #clear {
    background: none;
  }
</style>
