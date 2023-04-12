package ru.bmstu.mobileapp.retrofit

import ru.bmstu.mobileapp.SERVER_HOST_NAME

object Common {
    val retrofitService: RetrofitServices
        get() = RetrofitClient.getClient(SERVER_HOST_NAME).create(RetrofitServices::class.java)
}