<template>
   <div class="container-fluid home-back left-sidebar-margin">
      <br><br><br><br> 
      
      <h1 class="text-light" id="web">
        <span class="badge badge-pill badge-secondary">
          <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-caret-right-fill" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
            <path d="M12.14 8.753l-5.482 4.796c-.646.566-1.658.106-1.658-.753V3.204a1 1 0 0 1 1.659-.753l5.48 4.796a1 1 0 0 1 0 1.506z"/>
          </svg>
          Proyectos Web
        </span>
      </h1><br><br>

      <div class="card">
        <div class="card-body">
          <h3><span class="badge badge-danger">Laravel</span> + <span class="badge badge-success">Vue.js</span> - Web Comercial Caceres</h3>
          <hr>
          <div class="row">
            <div class="col-sm-6">
               <Carousel :slides="CaceresSlides"/>
            </div>  
            <div class="col-sm-6">
              <p>Página web creada con laravel y Vue js, es una tienda web que carga todos los productos y maneja la galería con componentes de vue
              y las api ajax en laravel, asegurando una experiencia fluida. Todo enlazado con la base de datos del erp de la empresa.</p>
              <p>Además dispone de varias webapps internas para la gestion de bodega, stock y un sistema de gestión de reservas personalizado.</p>

             <a target="_blank" href="https://comercialcaceres.cl/caceres/" >
               Ir a la web
             </a>
            </div>  
          </div>
        </div>
      </div>
      <br><br>
      <h1 class="text-light" id="webapps">
        <span class="badge badge-pill badge-info">
          <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-caret-right-fill" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
            <path d="M12.14 8.753l-5.482 4.796c-.646.566-1.658.106-1.658-.753V3.204a1 1 0 0 1 1.659-.753l5.48 4.796a1 1 0 0 1 0 1.506z"/>
          </svg>
          Webapps
        </span>
      </h1><br><br>
      <br><br>
      <h1 class="text-light" id="games">
        <span class="badge badge-pill badge-light">
          <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-caret-right-fill" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
            <path d="M12.14 8.753l-5.482 4.796c-.646.566-1.658.106-1.658-.753V3.204a1 1 0 0 1 1.659-.753l5.48 4.796a1 1 0 0 1 0 1.506z"/>
          </svg>
          Juegos
        </span>
      </h1><br><br>

   </div>
</template>

<script lang="ts">
import { } from 'vue'
import Carousel from '../Carousel.vue'

export default {
  components: {
        Carousel
   },
 
   setup(){
      
     let CaceresSlides = [
                    { id: 0, src: "img/caceres/products.gif" },   
                ]


      return {
        CaceresSlides,
      }

   }
}
</script>
