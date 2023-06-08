var mix = {
    methods: {
        getOrder(pk) {
            this.getData(`/api/orders/` + pk).then(data => {
                // console.log('data =>>> ', data);
                this.order = data
                // this.orderId = data.orderId
                // this.createdAt = data.createdAt
                // this.fullName = data.fullName
                // this.phone = data.phone
                // this.email = data.email
                // this.deliveryType = data.deliveryType
                // this.city = data.city
                // this.address = data.address
                // this.paymentType = data.paymentType
                // this.status = data.status
                // this.totalCost = data.totalCost
                // this.orderProducts = data.products
                // console.log('this.orderdetail =>>> ', this.orderdetail);
                // console.log('this.fullName =>>> ', this.fullName);
                if (typeof data.paymentError !== 'undefined'){
                    this.paymentError = data.paymentError
                }
            })
        },
        confirmOrder() {
            if (this.order) {
                this.postData('/api/orders/', {
                   ...this.order
                })
                    .then(() => {
                        alert('Заказ подтвержден')
                        location.replace('/payment')
                    })
                    .catch(() => {
                        console.warn('Ошибка при подтверждения заказа')
                    })
            }
        }
    },
    mounted() {
        this.getOrder(pk);

    },
    data() {
        return {
            order: {},
            // orderId: null,
            // createdAt: null,
            // fullName: null,
            // phone: null,
            // email: null,
            // deliveryType: null,
            // city: null,
            // address: null,
            // paymentType: null,
            // status: null,
            // totalCost: null,
            // orderProducts: [],
            paymentError: null,
        }
    },
}