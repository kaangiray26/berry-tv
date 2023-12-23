import { createRouter, createWebHistory } from 'vue-router';
import Display from '/components/Display.vue';
import Connect from '/components/Connect.vue';

const routes = [
    {
        path: "/",
        component: Display,
    },
    {
        path: "/connect",
        component: Connect,
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes
});

export default router