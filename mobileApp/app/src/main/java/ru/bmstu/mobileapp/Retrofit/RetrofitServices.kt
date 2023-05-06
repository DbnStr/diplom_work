package ru.bmstu.mobileapp.retrofit

import retrofit2.Call
import retrofit2.http.*
import ru.bmstu.mobileapp.models.Basket
import ru.bmstu.mobileapp.models.Invoice

interface RetrofitServices {
    @GET("baskets/{basketId}")
    fun getBasket(@Path("basketId") basketId: Int,
                    @Query("consumerId") consumerId: Int): Call<Basket>

    @GET("invoices")
    fun getInvoice(@Query("basketId") basketId: Int,
                  @Query("consumerId") consumerId: Int): Call<Invoice>
}