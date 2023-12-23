<template>
    <div v-if="visible" class="youtube-modal">
        <div class="d-flex justify-content-between">
            <h1>YouTube</h1>
            <span class="dialog-close material-symbols-outlined" @click="hide">
                close
            </span>
        </div>
        <div class="input-group mb-3">
            <span class="input-group-text" id="basic-addon1">URL</span>
            <input v-model="addr" type="text" class="form-control" placeholder="https://youtu.be/" aria-label="url"
                aria-describedby="basic-addon1">
            <button class="btn btn-dialog" type="button" @click="open_address">Open</button>
        </div>
        <div>
            <span class="text-danger" :class="{ 'opacity-0': !invalid_addr }">Invalid address</span>
        </div>
    </div>
</template>

<script setup>
import { ref, nextTick } from 'vue';

const emit = defineEmits(['open']);

const addr = ref('');
const visible = ref(false);
const invalid_addr = ref(false);
const hostnames = [
    'youtube.com',
    'youtu.be',
    'www.youtube.com',
    'www.youtu.be',
    'm.youtube.com',
]

async function open_address() {
    invalid_addr.value = false;
    let url = new URL(addr.value);
    if (!hostnames.includes(url.hostname)) {
        invalid_addr.value = true;
        return;
    }

    emit('open', addr.value);
    hide();
}

async function show() {
    visible.value = true;
    await nextTick();
    document.querySelector(' input').focus();
}

async function hide() {
    addr.value = '';
    visible.value = false;
}

defineExpose({
    show,
    hide
})
</script>