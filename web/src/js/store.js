// store.js
import { reactive } from 'vue';

const store = reactive({
    title: 'Nothing',
    paused: true,
    connected: false,
    duration: 0,
    currentTime: 0,
});

export { store }
