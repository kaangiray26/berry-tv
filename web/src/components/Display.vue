<template>
    <div class="d-flex justify-content-center">
        <div class="view">
            <Settings ref="settings" @exit="exit"></Settings>
            <YouTube ref="youtube" @open="openWebsite"></YouTube>
            <div class="d-flex align-items-center mb-3">
                <h1 class="mb-0">Berry-TV</h1>
                <h2 class="bi bi-gear-wide-connected ms-auto mb-0" @click="open_settings"></h2>
            </div>
            <div class="status-card">
                <span class="status-card-title">Now Playing</span>
                <div class="d-flex align-items-center">
                    <img src="/images/youtube.svg" alt="youtube" class="status-card-icon">
                    <span class="ms-3">{{ store.title }}</span>
                </div>
                <div class="d-flex align-items-center">
                    <span class="font-monospace me-3">{{
                        formatDuration(store.currentTime) + '/' + formatDuration(store.duration) }}</span>
                    <div ref="progressbar" class="progress flex-fill" role="progressbar" aria-label="Basic example"
                        aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" @click="seek">
                        <div class="progress-bar" :style="'width:' + getProgress()"></div>
                    </div>
                </div>
            </div>
            <div class="d-flex justify-content-center mt-3">
                <div class="d-flex align-items-center">
                    <button type="button" class="btn-controls" @click="seekBack">
                        <span class="bi bi-skip-backward-circle-fill"></span>
                    </button>
                    <button type="button" class="btn-controls" @click="playPause">
                        <span class="bi"
                            :class="{ 'bi-play-circle-fill': store.paused, 'bi-pause-circle-fill': !store.paused }"></span>
                    </button>
                    <button type="button" class="btn-controls" @click="seekForward">
                        <span class="bi bi-skip-forward-circle-fill"></span>
                    </button>
                </div>
            </div>
            <div class="d-flex flex-column">
                <div class="d-flex justify-content-center align-items-center">
                    <button type="button" class="btn-controls" @click="up">
                        <span class="bi bi-caret-up-square-fill"></span>
                    </button>
                </div>
                <div class="d-flex justify-content-center align-items-center">
                    <button type="button" class="btn-controls" @click="left">
                        <span class="bi bi-caret-left-square-fill"></span>
                    </button>
                    <button type="button" class="btn-controls" @click="middle">
                        <span class="bi bi-square-fill"></span>
                    </button>
                    <button type="button" class="btn-controls" @click="right">
                        <span class="bi bi-caret-right-square-fill"></span>
                    </button>
                </div>
                <div class="d-flex justify-content-center align-items-center">
                    <button type="button" class="btn-controls" @click="down">
                        <span class="bi bi-caret-down-square-fill"></span>
                    </button>
                </div>
            </div>
            <div class="d-flex justify-content-center align-items-center">
                <button type="button" class="btn-controls" @click="previous">
                    <span class="bi bi-skip-start-fill"></span>
                </button>
                <button type="button" class="btn-controls" @click="fullscreen">
                    <span class="bi bi-fullscreen"></span>
                </button>
                <button type="button" class="btn-controls" @click="next">
                    <span class="bi bi-skip-end-fill"></span>
                </button>
            </div>
            <div class="d-flex flex-column">
                <h2>Applications</h2>
                <div class="row g-3 row-cols-3">
                    <div class="col">
                        <div class="application" @click="youtube.show">
                            <span class="text-dark fw-bold">YouTube</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <WebSocket ref="websocket"></WebSocket>
</template>

<script setup>
import { ref } from 'vue';
import WebSocket from './WebSocket.vue';
import YouTube from './YouTube.vue';
import Settings from './Settings.vue';
import { store } from '/js/store.js';

const settings = ref(null);
const youtube = ref(null);

const websocket = ref(null);
const progressbar = ref(null);

async function playPause() {
    if (store.paused) {
        websocket.value.socket.emit('play');
        return
    }
    websocket.value.socket.emit('pause');
}

async function openWebsite(addr) {
    websocket.value.socket.emit('open', {
        "address": addr
    })
    store.title = "Loading..."
}

async function seek(event) {
    let rect = progressbar.value.getBoundingClientRect();
    let percent = (event.clientX - rect.x) / rect.width;
    let time = percent * store.duration;
    websocket.value.socket.emit('seek', {
        "time": time
    })
}

async function seekBack() {
    websocket.value.socket.emit('seekBackward');
}

async function seekForward() {
    websocket.value.socket.emit('seekForward');
}

async function fullscreen() {
    websocket.value.socket.emit('fullscreen');
}

async function previous() {
    websocket.value.socket.emit('previous');
}

async function next() {
    websocket.value.socket.emit('next');
}

async function exit() {
    websocket.value.socket.emit('exit');
}

async function up() {
    websocket.value.socket.emit('up');
}

async function left() {
    websocket.value.socket.emit('left');
}

async function middle() {
    websocket.value.socket.emit('middle');
}

async function right() {
    websocket.value.socket.emit('right');
}

async function down() {
    websocket.value.socket.emit('down');
}

async function open_settings() {
    settings.value.show();
}

function formatDuration(duration) {
    let minutes = Math.floor(duration / 60);
    let seconds = Math.floor(duration % 60);
    return `${minutes}:${seconds.toString().padStart(2, '0')}`
}

function getProgress() {
    return (store.currentTime / store.duration) * 100 + '%';
}
</script>