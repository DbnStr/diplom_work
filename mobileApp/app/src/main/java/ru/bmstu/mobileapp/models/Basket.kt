package ru.bmstu.mobileapp.models

data class Basket(
    var id: Int? = null,
    var idInShop: Int? = null,
    var shopId: Int? = null,
    var items: ArrayList<BasketItem>? = null
)
