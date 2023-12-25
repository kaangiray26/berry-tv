<template>
    <div v-if="visible" class="theme-modal">
        <div class="d-flex justify-content-between">
            <h1>Settings</h1>
            <span class="dialog-close material-symbols-outlined" @click="hide">
                close
            </span>
        </div>
        <div class="theme-list">
            <div class="theme-list-item" @click="exit">
                <span>Exit</span>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue';

const emit = defineEmits(['open', 'exit']);
const visible = ref(false);

async function show() {
    visible.value = true;
}

async function hide() {
    visible.value = false;
}

async function exit() {
    emit('exit');
}

defineExpose({
    show,
    hide
})
</script>