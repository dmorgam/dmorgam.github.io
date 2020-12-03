<template>
   <div class="container-fluid home-back">
      <br> 
      <!-- HEADER -->
      <div class="row">

         <div class="col-md-5">
            
               
         </div>

         <div class="col-md-7"> 
            <div class="card mb-3">
                  <div class="row no-gutters">
                    <div class="col-md-8">
                      <div class="card-body">
                        <h5 class="card-title">David Moreno Gámez</h5>
                        <p class="card-text">
                        Administrador de Sistemas y Fullstack Developer
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
              <h1>¿Quien soy?</h1>
              <br>
              <p>
                Desarrollo aplicaciones Web basadas en <b><a href="https://laravel.com/">Laravel</a></b>, php, 
                <b><a href="https://vuejs.org/">Vue.js</a></b> y eventualmente en vanilla js.
                Tambien gestiono el servidor donde se aloja y su stack LAMP.
              </p>
              <p>
                Soy usuario de Arch linux, fan de la terminal, recientemente cambiado al mundo del
                desarroyo web desde la administracion de sistemas.
              </p>
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
              <p><b>Frameworks: </b> Vue.js, Laravel</p>
              <p><b>Tecnologías: </b>Git, Docker, Kubernetes, Virtualización</p>
            </div>
         </div>
      </div>

   </div>
</template>

<script lang="ts">
import {  onMounted } from 'vue'

export default {
   setup(){
      
     onMounted(() => {

     })

   }
}
</script>
