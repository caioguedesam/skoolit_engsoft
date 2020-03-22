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

      <v-content class="pa-12" fluid>
        <v-row class="ml-12 pb-12" style="height:100%" dense align-content="end">
          <v-col cols=12>
            <v-text class="row-h-text" style="font-size: 40px">Skoolit.</v-text>
          </v-col>

          <v-col cols=12>
            <v-text class="row-h-text" style="font-size: 20px">
              A reformulacao de ser escola
            </v-text><br>
          </v-col>

          <v-col cols=12>
            <v-text class="row-text">
              Uma nova forma de aprender, uma nova maneira de educar
            </v-text>
          </v-col>

          <v-col cols=12>
            <v-btn color="#575A89" dark>Matricule-se</v-btn>
            <v-text class="ml-4 row-text">ou</v-text>
            <v-btn color="transparent" depressed>
                <v-text class="row-btn-text">entrar</v-text>
            </v-btn>
          </v-col>
        </v-row>
      </v-content>

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

  .row-h-text {
    font-family: Segoe UI,Frutiger,Frutiger Linotype,Dejavu Sans,Helvetica Neue,Arial,sans-serif;
    font-weight: bold;
    color: gray;
  }

  .row-text {
    font-family: Segoe UI,Frutiger,Frutiger Linotype,Dejavu Sans,Helvetica Neue,Arial,sans-serif;
    color:gray;
  }

  .row-btn-text {
    font-size: 12px;
    color: #575A89;
  }

  /*esvazia o background de v-app pra poder mostrar a imagem de fundo*/
  #clear {
    background: none;
  }
</style>
