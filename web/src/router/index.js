import { createRouter, createWebHistory } from 'vue-router';
import Display from '/components/Display.vue';

const routes = [
    {
        path: "/",
        component: Display,
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes
});

export default router