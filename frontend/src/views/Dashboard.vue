<template>
    <div class="container" v-if="!auth">
        <div class="row">
            <div class="col-12">
                <h1>You are not Logged In</h1>
                <h4>
                    <router-link to="/login">Login</router-link>
                </h4>
            </div>
        </div>
    </div>
    <div class="container" v-if="auth">
        <div class="row">

            <div class="col-12">
                <table class="table table-bordered">
                    <thead>
                        <tr>
                            <th scope="col">ID</th>
                            <th scope="col">Date</th>
                            <th scope="col">Case Type</th>
                            <th scope="col">Description</th>
                            <th scope="col">Status</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="item in data" :key="item.id">
                            <th scope="row">{{ item.id }}</th>
                            <td>{{ item.submission_date }}</td>
                            <td>{{ item.case_type }}</td>
                            <td>{{ item.case_description }}</td>
                            <td>
                                <button data-bs-toggle="modal" data-bs-target="#staticBackdrop" type="button"
                                    class="btn btn-primary">{{ item.status }}</button>

                            </td>
                        </tr>

                    </tbody>
                </table>
                <nav class="col-12">
                    <ul class="pagination pagination-lg">
                        <li class="page-item " style="cursor: pointer;" v-for="page in pages" :key="page">
                            <span class="page-link">{{ page }}</span>
                        </li>

                    </ul>
                </nav>
            </div>
        </div>
    </div>
    <!-- Modal -->
    <div class="modal fade" id="staticBackdrop" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1"
        aria-labelledby="staticBackdropLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="staticBackdropLabel">Modal title</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    ...
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                    <button type="button" class="btn btn-primary">Understood</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import { onMounted, ref } from 'vue';
import { useStore } from 'vuex'
import { computed } from 'vue'

type LegalRequest = {
    id: number;
    submission_date: string;
    case_type: string;
    case_description: string;
    status: string;
};

export default {
    name: "DashBoard",
    setup() {
        const store = useStore()
        const auth = computed(() => store.state.auth)

        const data = ref(Array<LegalRequest>());
        const pages = ref<number[]>([]);

        const fetchData = async () => {
            try {
                const response = await fetch('http://localhost:8000/api/clients/requests', {
                    method: 'GET',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    credentials: 'include',
                });
                const responseData = await response.json();
                if (responseData.legal_requests && responseData.pages) {
                    data.value = responseData.legal_requests;
                    pages.value = Array.from({ length: responseData.pages }, (_, i) => i + 1);
                } else {
                    // Handle cases where the expected properties are missing in the response
                    console.error('API response missing required properties');
                }
            } catch (error) {
                console.error('Error fetching data:', error);
                // Handle network or other errors gracefully
            }
        };
        fetchData()
        onMounted(async () => {
            try {
                const response = await fetch('http://localhost:8000/api/users/', {
                    method: 'GET',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    credentials: 'include',
                });
                if (response.status === 200) {
                    await store.dispatch('setAuth', true)
                } else {
                    await store.dispatch('setAuth', false)
                }

            } catch (error) {
                await store.dispatch('setAuth', false)
                // Handle network or other errors gracefully
            }
        })

        return { auth, data, pages }
    },

}

</script>

<style>
.hide {
    /* display:none; */
}
</style>