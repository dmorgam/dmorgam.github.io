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
               <Carousel name="Caceres" :slides="CaceresSlides"/>
            </div>  
            <div class="col-sm-6">
              <p>Página web creada con laravel,  Vue js y DB mysql. Es una tienda web que carga todos los productos y maneja la galería con componentes de Vue
              y las API AJAX en laravel, asegurando una experiencia fluida. Todo enlazado con el sqlserver del ERP de la empresa.</p>
              <p>Además, dispone de varias webapps internas para la gestion de bodega, stock y un sistema de gestión de reservas personalizado con exportación a excel, pdf
                 y generación de reportes.</p>

             <a target="_blank" href="https://comercialcaceres.cl/caceres/" >
               Ir a la web
             </a>
            </div>  
          </div>
        </div>
      </div>
      <br>
      <div class="card">
        <div class="card-body">
          <h3><span class="badge badge-info">PHP</span> + <span class="badge badge-warning">Vanilla js</span> - Antigua Web Comercial Caceres (Mejoras)</h3>
          <hr>
          <div class="row">
            <div class="col-sm-6">
               <Carousel name="oldCaceres" :slides="oldCaceresSlides"/>
            </div>  
            <div class="col-sm-6">
              <p>Web creada con php, js y DB mysql. Contribución mejorando la web y añadiendo módulos.</p>
              <p>Generación de hojas de ruta en pdf, trazado de rutas con la API de google maps, sistemas de gestión de permisos,
                 gestión de reservas y estadísticas de venta de los productos.</p>
              <p>Catálogo automatizado conectado al ERP. </p>
              <p>Generación de reportes en pdf con FPDF y hojas excel con PHPexcel. </p>
              <a target="_blank" href="https://comercialcaceres.cl/" >
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
          <h3><span class="badge badge-danger">Laravel</span> + <span class="badge badge-success">Vue.js</span> - Aplicación de Venta mayorista en terreno</h3>
          <hr>
            <div class="row">
              <div class="col-sm-4">
                <video style="height: 30em;" controls>
                    <source src="img/caceres/appMayorista.mp4" type="video/mp4">
                </video>
              </div>  
              <div class="col-sm-8">
                 [ En proceso, proyecto actual ]<br><br>

                  Aplicación de gestión de ventas mayoristas, hecha en vue.js y con la api ajax en laravel.<br><br>

                  Gestiona pedidos y clientes, deudas de clientes, dispone de un catalogo con los últimos precios y stock real
                  con imágenes para la venta directa en terreno.<br><br>

                  Para la comunicación entre la app y el backend, se usa la libreria axios haciendo peticiones get, post y put para obtener
                  los datos, ingresar nuevos y actualizar.<br><br>

                  El front dispone de varios componentes los cuales se van alternando cargando dinamicamente según el modo en el que esté (estado inicial o cliente cargado).
              </div>
            </div>
        </div>
      </div>
      <br>
      <div class="card">
        <div class="card-body">
          <h3><span class="badge badge-info">PHP</span> + <span class="badge badge-warning">Vanilla JS</span> + <span class="badge badge-info">Kotlin</span> - Aplicación de Gestion de horarios de colación</h3>
          <hr>
            <div class="row">
              <div class="col-sm-6">
                 <Carousel name="colacionslides" :slides="colacionSlides"/>
              </div>  
              <div class="col-sm-6">
                <p>Aplicación para administrar el tiempo de colación de los trabajadores con temporizador, ticket de colación y registro de colaciones por cada trabajador.</p>
                <p>El servidor en PHP y DB mysql dispone de una api a la que se conectan los front cliente web y la aplicación android.</p>
                <p>El front web dispone de la pantalla de colación y el formulario que registra las entradas y salidas de trabajadores. El apk android consta de controles con los cuales, 
                   los jefes de tienda pueden ver quien está en colación y liberar los asientos.</p>
              </div>
            </div>
        </div>
      </div>
      <br>
      <div class="card">
        <div class="card-body">
          <h3><span class="badge badge-info">PHP</span> + <span class="badge badge-warning">Vanilla JS</span> - Afiche publicitario automático </h3>
          <hr>
            <div class="row">
              <div class="col-sm-6">
                 <Carousel name="aficheslides" :slides="aficheSlides"/>
              </div>  
              <div class="col-sm-6">
                <p>El afiche consiste en una pantalla en html y js recibiendo mediante AJAX la lista de productos a mostrar, y los descarga de la DB del ERP para mostrarlos.</p>
                <p>El backend en php dispone de un endpoint donde muestra los productos en lista, también dispone de varias categorías para poder mostrar afiches de distinto tipo.</p>
                <p>Dispone de una interfaz de gestión de los productos en cada catagoría para gestionar los productos mostrados.</p>
              <a target="_blank" href="https://comercialcaceres.cl/afiche/rotiseria.php" >
                 Ir a la web
              </a>
              </div>  
            </div>
        </div>
      </div>
      <br>
      <div class="card">
        <div class="card-body">
          <h3><span class="badge badge-success">Vue.js 3</span> + <span class="badge badge-info">Typescript</span> - Web personal en github pages</h3>
          <hr>
            <div class="row">
              <div class="col-sm-6">
                 <Carousel name="webslides" :slides="WebSlides"/>
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
                 <Carousel name="snakeslide" :slides="SnakeSlides"/>
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

     let oldCaceresSlides = [
                    { id: 0, src: "img/caceres/hojasruta.png" },
                    { id: 1, src: "img/caceres/catalogo.png" },
                    { id: 2, src: "img/caceres/mercaderia.png" },
                    { id: 3, src: "img/caceres/reporteventaprod.png" },
                    { id: 4, src: "img/caceres/fallaperm.png" },
                    { id: 5, src: "img/caceres/fallapermpdf.png" },
                    { id: 6, src: "img/caceres/hojasrutapdf.png" },
                    { id: 7, src: "img/caceres/resdiecio.png" },
                ]

     let aficheSlides = [
                    { id: 0, src: "img/caceres/afiche.gif" },
                    { id: 1, src: "img/caceres/aficheCarga.png" },
                ]

     let colacionSlides = [
                    { id: 0, src: "img/caceres/colacion.png" },
                    { id: 1, src: "img/caceres/colacionapk.png" },
                    { id: 2, src: "img/caceres/colacionapk2.png" },
                    { id: 3, src: "img/caceres/colacionSolicita.png" },
                    { id: 4, src: "img/caceres/colacionTicket.png" },
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
        oldCaceresSlides,
        colacionSlides,
        aficheSlides
      }

   }
}
</script>
