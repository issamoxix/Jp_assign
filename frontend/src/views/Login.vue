<template>
    <div class="form-signin w-100 m-auto">
        <form @submit.prevent="">
            <h1 class="h3 mb-3 fw-normal">Please sign in</h1>

            <div class="form-floating">
                <input v-model="state.email" type="email" class="form-control" placeholder="name@example.com">
                <label for="floatingInput">Email</label>
            </div>
            <div class="form-floating">
                <input v-model="state.password" type="password" class="form-control" placeholder="Password">
                <label for="floatingPassword">Password</label>
            </div>
            <button @click="submit" class="btn btn-primary w-100 py-2" type="submit">Sign in</button>
        </form>
    </div>
</template>
<script lang="ts">
import { reactive } from 'vue'
import { useRouter } from 'vue-router'

export default {
    name: "Login",
    setup() {
        const state = reactive({
            email: '',
            password: ''
        })
        const router = useRouter()
        const submit = async () => {
            await fetch('http://localhost:8000/api/users/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                credentials: 'include',
                body: JSON.stringify(state),
            })
            await router.push('/dashboard')
        }
        return { state, submit }
    }
}


</script>