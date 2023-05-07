package ru.bmstu.mobileapp.fragments.choice_payment_method

import android.annotation.SuppressLint
import android.os.Bundle
import android.util.Log
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Button
import android.widget.TextView
import android.widget.Toast
import androidx.navigation.fragment.findNavController
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response
import ru.bmstu.mobileapp.R
import ru.bmstu.mobileapp.USER_ID
import ru.bmstu.mobileapp.models.Invoice
import ru.bmstu.mobileapp.models.Payment
import ru.bmstu.mobileapp.models.PaymentMethod
import ru.bmstu.mobileapp.retrofit.Common
import ru.bmstu.mobileapp.retrofit.RetrofitServices
import java.net.URL

class ChoicePaymentMethod : Fragment() {

    private lateinit var recyclerView: RecyclerView
    private lateinit var choicePaymentMethodAdapter: ChoicePaymentMethodAdapter
    private lateinit var data: MutableList<PaymentMethod>

    lateinit var myService: RetrofitServices

    private var paymentsMethods: ArrayList<PaymentMethod> = ArrayList()
    private var amount = 0.0f
    private var invoiceId: Int = 0

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        val view = inflater.inflate(R.layout.fragment_choice_payment_method, container, false)
        recyclerView = view.findViewById(R.id.invoice_list)

        val args: Bundle? = arguments
        if (args != null) {
            amount = args.getFloat("amount")
            invoiceId = args.getInt("invoiceId")
            paymentsMethods.add(PaymentMethod("MIR", "5678", 0.9f * amount))
            paymentsMethods.add(PaymentMethod("MIR", "5697", 0.95f * amount))
        } else {
            Log.e("PaymentMethod Fragment", "Bundle from previous fragment is null")
        }

        data = mutableListOf()
        data.addAll(paymentsMethods)
        choicePaymentMethodAdapter = ChoicePaymentMethodAdapter(data)
        val layoutManager: RecyclerView.LayoutManager = LinearLayoutManager(context)
        recyclerView.layoutManager = layoutManager
        recyclerView.adapter = choicePaymentMethodAdapter

        myService = Common.retrofitService

        val paymentButton : Button = view.findViewById(R.id.button_pay_invoice)
        paymentButton.setOnClickListener {
            val selectedPaymentMethod : Int = choicePaymentMethodAdapter.getSelectedPaymentMethod()
            if (selectedPaymentMethod != -1) {
                paymentInitiation(invoiceId)
            } else {
                Toast.makeText(activity, "Выберите способ оплаты", Toast.LENGTH_LONG).show()
            }
        }

        return view
    }

    private fun paymentInitiation(invoiceId: Int) {
        myService.paymentInitiation(invoiceId).enqueue(object : Callback<Payment> {
            override fun onFailure(call: Call<Payment>, t: Throwable) {
                Log.d("paymentInitiation", "Failure" + t.toString())
            }

            override fun onResponse(call: Call<Payment>, response: Response<Payment>) {
                Log.d("getBasketHttpRequest", "Success " + response.body()!!.paymentId)
                findNavController().navigate(R.id.action_choice_payment_method_to_success_payment)
            }
        })
    }
}