package ru.bmstu.mobileapp.fragments.invoice

import android.annotation.SuppressLint
import android.os.Bundle
import android.util.Log
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Button
import android.widget.TextView
import androidx.navigation.NavController
import androidx.navigation.fragment.findNavController
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response
import ru.bmstu.mobileapp.R
import ru.bmstu.mobileapp.USER_ID
import ru.bmstu.mobileapp.models.Invoice
import ru.bmstu.mobileapp.models.Item
import ru.bmstu.mobileapp.retrofit.Common
import ru.bmstu.mobileapp.retrofit.RetrofitServices
import java.net.URL

class InvoiceFragment : Fragment() {

    private lateinit var recyclerView: RecyclerView
    private lateinit var invoiceAdapter: InvoiceAdapter
    private lateinit var data: MutableList<Item>
    private lateinit var navController: NavController

    lateinit var myService: RetrofitServices

    @SuppressLint("MissingInflatedId")
    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        val view = inflater.inflate(R.layout.fragment_invoice, container, false)
        recyclerView = view.findViewById(R.id.invoice_list)

        data = mutableListOf()
        invoiceAdapter = InvoiceAdapter(data)
        val layoutManager: RecyclerView.LayoutManager = LinearLayoutManager(context)
        recyclerView.layoutManager = layoutManager
        recyclerView.adapter = invoiceAdapter
        navController = this.findNavController()

        myService = Common.retrofitService

        val args: Bundle? = arguments
        val qrCodePayload: String?
        if (args != null) {
            qrCodePayload = args.getString("qrCodePayload")
            if (qrCodePayload == null) {
                Log.e("Invoice Fragment", "qrCodePayload From previous fragment is null")
            }
            val url = URL(qrCodePayload)
            val pathParams = url.path.split("/")
            val basketId = pathParams[2].toInt()

            getInvoice(basketId, USER_ID)
        } else {
            Log.e("Invoice Fragment", "Bundle from previous fragment is null")
        }

        val paymentButton: Button = view.findViewById(R.id.button_pay_invoice)
        paymentButton.setOnClickListener {
            navController.navigate(R.id.action_invoice_to_choice_payment_method)
        }

        val sendHttp: Button = view.findViewById(R.id.http_send_button)
        sendHttp.setOnClickListener {
            getInvoice(1, USER_ID)
        }

        return view
    }

    private fun getInvoice(basketId: Int, consumerId: Int) {
        myService.getInvoice(basketId, consumerId).enqueue(object : Callback<Invoice> {
            override fun onFailure(call: Call<Invoice>, t: Throwable) {
                Log.d("getBasketHttpRequest", "Failure" + t.toString())
            }

            @SuppressLint("NotifyDataSetChanged")
            override fun onResponse(call: Call<Invoice>, response: Response<Invoice>) {
                Log.d("getBasketHttpRequest", "Success " + response.body())
                val items = response.body()?.items
                if (items != null) {
                    Log.d("getBasketHttpRequest", items.toString())
                    data.addAll(items)

                    view!!.findViewById<TextView>(R.id.invoice_total_amount).text = response.body()?.totalAmount.toString()
                    view!!.findViewById<TextView>(R.id.invoice_total_amount_with_discounts).text = response.body()?.totalAmountWithDiscounts.toString()
                }
                invoiceAdapter.notifyDataSetChanged()
            }
        })
    }
}