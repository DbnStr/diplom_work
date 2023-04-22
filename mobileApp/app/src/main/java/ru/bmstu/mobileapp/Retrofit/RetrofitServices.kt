package ru.bmstu.mobileapp.retrofit

import retrofit2.Call
import retrofit2.http.*
import ru.bmstu.mobileapp.models.Basket

interface RetrofitServices {
    @GET("baskets/{basketId}")
    fun getBasket(@Path("basketId") basketId: Int,
                    @Query("consumerId") consumerId: Int): Call<Basket>
}