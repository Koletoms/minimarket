var mix = {
    methods: {
        getUserAccount() {
            this.getData("/api/account/").then(data => {
                this.fullName = data.fullName
                this.avatar = data.avatar
            })
        },
    },
    mounted() {
        this.getUserAccount();
    },
    data() {
        return {
            fullName: "",
            avatar: {},
        }
    },
}