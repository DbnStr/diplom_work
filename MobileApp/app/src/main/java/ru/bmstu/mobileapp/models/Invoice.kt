package ru.bmstu.mobileapp.models

data class Invoice(
    var invoiceId: Int? = null,
    var basketId: Int? = null,
    var consumerId: Int? = null,
    var paymentMethods: String? = null,
    var expiredDateTime: String? = null,
    var items: ArrayList<Item>? = null,
    var totalAmount: Float? = null,
    var totalAmountWithDiscounts: Float? = null
)
