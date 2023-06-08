var mix = {
    methods: {
        submitPayment() {
            const paymentId = location.pathname.startsWith('/payment/') // Получаем id заказа из url
            ? Number(location.pathname.replace('/payment/', ''))
            : null
            this.postData(
                `/api/payment/${paymentId}`,
                {
                    name: this.name,
                    number: this.number,
                    year: this.year,
                    month: this.month,
                    code: this.code
                },
                { headers: {'X-CSRFToken': this.getCookie('csrftoken'),}}
            )
            .then(() => {
                alert('Успешная оплата')
                this.number = ''
                this.name = ''
                this.year = ''
                this.month = ''
                this.code = ''
            })
            .catch(() => {
                console.warn('Ошибка при оплате')
            })
        }
    },
    data () {
        return {
            number: '',
            month: '',
            year: '',
            name: '',
            code: ''
        }
    }
}