package ru.bmstu.mobileapp.retrofit

import retrofit2.Call
import retrofit2.http.*
import ru.bmstu.mobileapp.models.Invoice
import ru.bmstu.mobileapp.models.Payment

interface RetrofitServices {
    @GET("invoices")
    fun getInvoice(@Query("basketId") basketId: Int,
                  @Query("consumerId") consumerId: Int): Call<Invoice>
    @POST("paymentInitiation")
    fun paymentInitiation(@Query("invoiceId") invoiceId: Int): Call<Payment>
}