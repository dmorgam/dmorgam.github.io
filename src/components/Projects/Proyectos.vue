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
              y las api ajax en laravel, asegurando una experiencia fluida. Todo enlazado con el sqlserver del erp de la empresa.</p>
              <p>Además dispone de varias webapps internas para la gestion de bodega, stock y un sistema de gestión de reservas personalizado con exportación a excel, pdf
                 y generación de reportes.</p>

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

      <div class="card">
        <div class="card-body">
          <h3><span class="badge badge-success">Vue.js 3</span> + <span class="badge badge-info">Typescript</span> - Web personal en github pages</h3>
          <hr>
            <div class="row">
              <div class="col-sm-6">
                 <Carousel :slides="WebSlides"/>
              </div>  
              <div class="col-sm-6">
                <p>En esta web se presentan los proyectos principales que he llevado a cabo y una muestra de mis habilidades en forma de widgets y
                   pequeños proyectos demostrativos</p>
                <p> Puede ver el repositorio <a target="_blank" href="https://github.com/dmorgam/dmorgam.github.io">aquí</a></p>
              </div>  
            </div>
        </div>
      </div>

      <br><br>
      <h1 class="text-light" id="games">
        <span class="badge badge-pill badge-light">
          <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-caret-right-fill" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
            <path d="M12.14 8.753l-5.482 4.796c-.646.566-1.658.106-1.658-.753V3.204a1 1 0 0 1 1.659-.753l5.48 4.796a1 1 0 0 1 0 1.506z"/>
          </svg>
          Juegos
        </span>
      </h1><br><br>

      <div class="card">
        <div class="card-body">
          <h3><span class="badge badge-danger">Vanilla JS</span> - Juego de snake con canvas y vanilla js</h3>
          <hr>
            <div class="row">
              <div class="col-sm-6">
                 <Carousel :slides="SnakeSlides"/>
              </div>  
              <div class="col-sm-6">
                <p>Juego de snake con canvas y js puro, con velocidad ajustable, sonidos, texturas, generacion de comida y puntaje variable,
                   responsivo calculando el tama;o del canvas.</p>
                <p> Puede ver el repositorio <a target="_blank" href="https://github.com/dmorgam/snakejs">aquí</a>, puede probarlo 
                   <a target="_blank" href="https://htmlpreview.github.io/?https://raw.githubusercontent.com/dmorgam/snakejs/master/index.html">aquí</a>.</p>
              </div>  
            </div>
        </div>
      </div>
      


      <br>
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
                    { id: 0, src: "img/caceres/inventario.gif" },   
                    { id: 1, src: "img/caceres/products.gif" },   
                    { id: 2, src: "img/caceres/productos.gif" },   
                    { id: 3, src: "img/caceres/navidad.png" },   
                ]

     let WebSlides = [
                    { id: 0, src: "img/webpersonal/dmorgam.png" },   
                ]

     let SnakeSlides = [
                    { id: 0, src: "img/snakejs.png" },   
                ]


      return {
        CaceresSlides,
        WebSlides,
        SnakeSlides,
      }

   }
}
</script>
