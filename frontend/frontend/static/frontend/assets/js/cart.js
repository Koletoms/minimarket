// var mix = {
//     methods: {
//         submitBasket () {
//             this.postData('/api/orders/',
//                 {products: Object.values(this.basket)}, // TODO что за синтаксис payload
//                 { headers: {'X-CSRFToken': this.getCookie('csrftoken'),}} // config
//                 )
//                 .then(data => {
//                     this.order.id = data.id
//                     this.order.products = data.products
//                     this.basket = {}
//                     location.assign('/order')
//                 }).catch(() => {
//                     console.warn('Ошибка при создании заказа')
//                 })
//         }
//     },
//     mounted() {
//     },
// }