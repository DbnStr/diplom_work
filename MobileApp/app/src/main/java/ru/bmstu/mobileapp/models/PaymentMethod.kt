package ru.bmstu.mobileapp.models

data class PaymentMethod(
    var type: String? = null,
    var number: String? = null,
    var amount: Float? = null
)
