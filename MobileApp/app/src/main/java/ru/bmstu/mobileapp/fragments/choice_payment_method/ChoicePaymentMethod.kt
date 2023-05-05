package ru.bmstu.mobileapp.fragments.choice_payment_method

import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Button
import androidx.navigation.fragment.findNavController
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import ru.bmstu.mobileapp.R
import ru.bmstu.mobileapp.models.PaymentMethod

class ChoicePaymentMethod : Fragment() {

    private lateinit var recyclerView: RecyclerView
    private lateinit var choicePaymentMethodAdapter: ChoicePaymentMethodAdapter
    private lateinit var data: MutableList<PaymentMethod>

    private var paymentsMethods: ArrayList<PaymentMethod> = arrayListOf(
        PaymentMethod("MIR", "12345678", 200.0f),
        PaymentMethod("MIR", "12345697", 50.0f),
    )

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        val view = inflater.inflate(R.layout.fragment_choice_payment_method, container, false)
        recyclerView = view.findViewById(R.id.invoice_list)

        data = mutableListOf()
        data.addAll(paymentsMethods)
        choicePaymentMethodAdapter = ChoicePaymentMethodAdapter(data)
        val layoutManager: RecyclerView.LayoutManager = LinearLayoutManager(context)
        recyclerView.layoutManager = layoutManager
        recyclerView.adapter = choicePaymentMethodAdapter

        val paymentButton : Button = view.findViewById(R.id.button_pay_invoice)
        paymentButton.setOnClickListener {
            findNavController().navigate(R.id.action_choice_payment_method_to_success_payment)
        }

        return view
    }
}