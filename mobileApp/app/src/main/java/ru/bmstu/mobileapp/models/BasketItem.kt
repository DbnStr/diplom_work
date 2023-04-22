package ru.bmstu.mobileapp.models

data class BasketItem(
    var itemId: Int? = null,
    var name: String? = null,
    var oneItemCost: String? = null,
    var quantity: String? = null,
    var amount: String? = null
)
