<template>

    <!-- Sidebar -->
    <div class="bg-light border-right" id="sidebar-wrapper">
      <div class="sidebar-heading">{{ props.title }}</div>
      <div class="list-group list-group-flush">
        <a v-for="i in sections" :key="i.title" :href="i.link" class="list-group-item list-group-item-action bg-light">
          {{ i.title }}
        </a>
      </div>
    </div>
    <!-- /#sidebar-wrapper -->

</template>

<script lang="ts">
import { } from 'vue'

export default {
   props: {
     title: String,
     sections: { required: true },
   },


   setup(props: any){
    
    
     return{
       props,
     }
   }
}
</script>
