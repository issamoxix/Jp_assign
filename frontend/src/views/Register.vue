<template>
    <div class="form-signin w-100 m-auto">
        <form @submit.prevent="">
            <h1 class="h3 mb-3 fw-normal">Register</h1>

            <input v-model="state.name" type="name" class="form-control" placeholder="Name" required>
            <input v-model="state.email" type="email" class="form-control" placeholder="Email" required>
            <input v-model="state.password" type="password" class="form-control" placeholder="Password" required>
            <button @click="submit" class="btn btn-primary w-100 py-2" type="submit">Submit</button>
        </form>
    </div>
</template>
<script lang="ts" >
import { reactive } from 'vue'
import { useRouter } from 'vue-router'

export default {
    name: "Register",
    setup() {
        const state = reactive({
            name: '',
            email: '',
            password: ''
        })

        const router = useRouter()

        const submit = async () => {
            await fetch('http://localhost:8000/api/users/register', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(state)
            })
            await router.push('/login')
            return 1
        }
        return { state, submit }
    }
}




</script>