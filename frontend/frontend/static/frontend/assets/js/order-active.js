var mix = {
    methods: {
        getDelivery() {
            this.getData('/api/delivery/').then(data => {
                this.allDelivery = {
                    ...this.allDelivery,
                    ...data
                }
            }).catch(() => {
                console.warn('Ошибка при способов доставок заказа')
                this.allDelivery = {
                    ...this.allDelivery,
                }
            })
        },
        getLastOrder() {
            this.getData('/api/orders/active').then(data => {
                this.order = {
                    ...this.order,
                    ...data
                }
            }).catch(() => {
                console.warn('Ошибка при получении активного заказа')
                this.order = {
                    ...this.order,
                }
            })
        },
        confirmOrder() {
            const id = this.order.orderId
            if (this.order) {
                this.postData(
                    '/api/orders/' + id,
                    {...this.order},
                    { headers: {'X-CSRFToken': this.getCookie('csrftoken'),}}
                )
                .then(() => {
                    alert('Заказ подтвержден')
                    location.replace(`/payment/${id}`) // Добавлено id заказа для привязки оплаты к заказу
                })
                .catch(() => {
                    console.warn('Ошибка при подтверждения заказа')
                })
            }
        },
        setDeliveryPrice(price_delivery, limit, above_price_limit) {

            if (this.order.totalCost > limit) {
                this.order.deliveryPrice = above_price_limit
            }
            else {
                this.order.deliveryPrice = price_delivery
            }
            console.log("1", this.order.deliveryPrice)
        }


    },
    mounted() {
        this.getLastOrder();
        this.getDelivery();
    },
    data() {
        return {
            order: {},
            allDelivery: [],
            paymentError: null,
        }
    },
}