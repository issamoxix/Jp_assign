<template>
    <nav class="navbar navbar-expand-md navbar-dark bg-dark mb-4">
        <div class="container-fluid">
            <router-link to="/" class="navbar-brand">JP</router-link>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarCollapse"
                aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarCollapse">
                <ul class="navbar-nav me-auto mb-2 mb-md-0">
                    <li class="nav-item">
                        <router-link to="/" class="nav-link">Home</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link to="/DashBoard" class="nav-link">Dashboard</router-link>
                    </li>
                </ul>
            </div>
            <div>
                <ul class="navbar-nav me-auto mb-2 mb-md-0" v-if="!auth">
                    <li class="nav-item">
                        <router-link to="/login" class="nav-link">Login</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link to="/register" class="nav-link">Register</router-link>
                    </li>
                </ul>
                <ul class="navbar-nav me-auto mb-2 mb-md-0" v-if="auth">
                    <li class="nav-item">
                        <router-link to="/login" @click="logout" class="nav-link">Logout</router-link>
                    </li>

                </ul>
            </div>
        </div>
    </nav>
</template>

<script lang="ts" >

import { useStore } from 'vuex'
import { computed } from 'vue'

export default {
    name: "Nav",
    setup() {
        const store = useStore()
        const auth = computed(() => store.state.auth)
        const logout = async () => {
            await fetch('http://localhost:8000/api/users/logout', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                credentials: 'include'
            })
            await store.dispatch('setAuth', false)
        }

        return { auth, logout }
    }
}


</script>
<style></style>
