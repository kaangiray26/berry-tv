<template>
    <div class="h-100 d-flex justify-content-center align-items-center">
        <div class="view">
            <div class="row g-5 align-items-center">
                <div class="col">
                    <h1>Scan the QR code with your phone to connect to Berry-TV</h1>
                </div>
                <div class="col">
                    <div class="border-theme">
                        <img :src="url" alt="qr-code" class="qr-code">
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import QRCode from 'qrcode'

const url = ref('')

onMounted(() => {
    QRCode.toDataURL('http://192.168.1.2:8000', {
        errorCorrectionLevel: 'H',
        type: 'image/jpeg',
        width: 512,
        margin: 0,
        color: {
            dark: '#000000',
            light: '#ffffff'
        }
    }, (err, data_url) => {
        url.value = data_url
    })
})
</script>