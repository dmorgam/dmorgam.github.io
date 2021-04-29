<template>
   <div class="container-fluid home-back left-sidebar-margin">
      <br><br><br><br>
      <!-- HEADER -->
      <div class="row">

         <div class="col-md-5">

         </div>

         <div class="col-md-7">
            <div class="card mb-3">
                  <div class="row no-gutters">
                    <div class="col-md-8">
                      <div class="card-body">
                        <h5 class="card-title font-weight-bold">David Moreno Gámez</h5>
                        <p class="card-text">
                           Desarrollador Web y Administrador de Sistemas
                        </p>
                        <p>
                          <small class="text-muted">
                            Autodidacta, siempre con ganas de aprender nuevas tecnologías que
                            aporten valor y avance tecnológico.
                          </small>
                        </p>
                      </div>
                    </div>
                    <div class="col-md-4">
                     <img src="img/dmorgam.png" class="card-img-top" alt="">
                    </div>
                  </div>
                </div>
            </div>

         </div>
      <br>
      <div class="row">
         <div class="col" id="who">
            <div class="alert alert-info text-center" role="alert">
              <h1>¿A qué me dedico?</h1>
              <br>
              <p>
                Desarrollo aplicaciones Web <b><a href="https://laravel.com/">Laravel</a></b>, php,
                <b><a href="https://vuejs.org/">Vue.js</a></b> y Javascript.
                También, gestiono servidores LAMP con apache y Nginx.
              </p>
              <p>
                Soy usuario habitual de Gnu/Linux. Usando la terminal, zsh, tmux y vim para
                trabajar, he ido aprendiendo desde el mundo de los sistemas al desarrollo Web.
              </p>
              <p>Puede ver algunos de mis proyectos <router-link to="projects">aquí</router-link>.</p>
            </div>
         </div>
      </div>
      <br>
      <div class="row">
         <div class="col" id="tech">
            <div class="alert alert-success text-center" role="alert">
              <h1>Tecnologías</h1>
              <br>
              <p><b>Lenguajes: </b> PHP, Javascript, Typescript (en desarrollo), Shell Scripting</p>
              <p><b>Frameworks: </b> Vue.js, Laravel, Bootstrap</p>
              <p><b>Tecnologías: </b>Git, Docker, Kubernetes,Linux, Virtualización</p>
              <p><b>Herramientas: </b>Vim, npm, composer, zsh, Android Studio(básico)</p>
            </div>
         </div>
      </div>

   </div>
</template>

<script lang="ts">
import { onMounted } from 'vue'

export default {
  setup () {
    onMounted(() => {

    })
  }
}
</script>
