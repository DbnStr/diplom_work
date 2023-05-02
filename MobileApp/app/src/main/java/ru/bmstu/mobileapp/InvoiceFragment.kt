package ru.bmstu.mobileapp

import android.annotation.SuppressLint
import android.content.Intent
import android.os.Bundle
import android.util.Log
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Button
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response
import ru.bmstu.mobileapp.models.Basket
import ru.bmstu.mobileapp.models.BasketItem
import ru.bmstu.mobileapp.retrofit.Common
import ru.bmstu.mobileapp.retrofit.RetrofitServices

class InvoiceFragment : Fragment() {

    private lateinit var recyclerView: RecyclerView
    private lateinit var invoiceAdapter: InvoiceAdapter
    private lateinit var data: MutableList<BasketItem>

    lateinit var myService: RetrofitServices

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
    }

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

        myService = Common.retrofitService

        val sendHttp: Button = view.findViewById(R.id.http_send_button)
        sendHttp.setOnClickListener {
            getBasket()
        }

        return view
    }

    private fun getBasket() {
        myService.getBasket(1, 1).enqueue(object : Callback<Basket> {
            override fun onFailure(call: Call<Basket>, t: Throwable) {
                Log.d("getBasketHttpRequest", "Failure" + t.toString())
            }

            @SuppressLint("NotifyDataSetChanged")
            override fun onResponse(call: Call<Basket>, response: Response<Basket>) {
                Log.d("getBasketHttpRequest", "Success " + response.body())
                val items = response.body()?.items
                if (items != null) {
                    data.addAll(items)
                }
                invoiceAdapter.notifyDataSetChanged()
            }
        })
    }
}