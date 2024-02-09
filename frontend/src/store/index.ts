import { createStore } from "vuex";

type LegalRequest = {
    id: number;
    submission_date: string;
    case_type: string;
    case_description: string;
    status: string;
};


export const store = createStore({
    state: {
        auth: false,
        // item: null
    },
    mutations: {
        setAuth: (state: { auth: boolean }, auth: boolean) => state.auth = auth,
        // setItem: (state: { item: LegalRequest }, item: LegalRequest) => state.item = item
    },
    actions: {
        // setAuth: ({ state }, auth:boolean) => {
        //     state.auth = auth;
        // }
        setAuth: ({ commit }: { commit: any }, auth: boolean) => commit('setAuth', auth),
        // setItem: ({ commit }, { commit: any }, item: LegalRequest) => commit('setItem', item)
    },
    modules: {
    }
});
