package ru.bmstu.mobileapp.retrofit

import retrofit2.Call
import retrofit2.http.*
import ru.bmstu.mobileapp.models.Basket

interface RetrofitServices {
    @GET("baskets/{basket_id}")
    fun getBasket(@Path("basket_id") basket_id: String,
                    @Query("user_id") user_id: String): Call<Basket>
}