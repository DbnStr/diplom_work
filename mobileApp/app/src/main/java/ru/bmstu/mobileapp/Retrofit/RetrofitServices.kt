package ru.bmstu.mobileapp.retrofit

import okhttp3.RequestBody
import retrofit2.Call
import retrofit2.http.*
import ru.bmstu.mobileapp.models.Invoice
import ru.bmstu.mobileapp.models.PaymentRequestBody
import ru.bmstu.mobileapp.models.PaymentResponseBody

interface RetrofitServices {
    @GET("invoices")
    fun getInvoice(@Query("basketId") basketId: Int,
                  @Query("consumerId") consumerId: Int): Call<Invoice>

    @Headers("Content-Type: application/json")
    @POST("paymentInitiation")
    fun paymentInitiation(
        @Body paymentRequestBody: PaymentRequestBody,
        @Query("invoiceId") invoiceId: Int): Call<PaymentResponseBody>
}