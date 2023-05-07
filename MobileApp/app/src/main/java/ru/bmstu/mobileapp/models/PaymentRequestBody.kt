package ru.bmstu.mobileapp.models

data class PaymentRequestBody(
    var paymentMethod: String,
    var cardNumber: String
)
