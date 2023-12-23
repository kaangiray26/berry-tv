<template></template>

<script setup>
import { ref, onMounted } from 'vue';
import { io } from "socket.io-client";
import { store } from '/js/store.js';

const socket = ref(null);

defineExpose({
    socket
})

onMounted(() => {
    socket.value = io("http://localhost:8000");

    socket.value.on('connect', () => {
        console.log('websocket connected');
        store.connected = true;
        socket.value.emit('title');
    });

    socket.value.on('title', (data) => {
        store.title = data.title || "Nothing";
    })

    socket.value.on('details', (data) => {
        store.title = data.title;
        store.duration = data.duration;
    })

    socket.value.on('play', () => {
        console.log('play');
        store.isPlaying = true;
    })

    socket.value.on('pause', () => {
        store.isPlaying = false;
    })

    socket.value.on('timeupdate', (data) => {
        store.currentTime = data.currentTime;
        store.duration = data.duration;
        store.paused = data.paused == "true";
        store.title = data.title;
    })
})
</script>