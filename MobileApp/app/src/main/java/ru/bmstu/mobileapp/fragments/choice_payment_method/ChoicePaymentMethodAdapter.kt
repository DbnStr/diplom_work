package ru.bmstu.mobileapp.fragments.choice_payment_method

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView
import ru.bmstu.mobileapp.R
import ru.bmstu.mobileapp.models.PaymentMethod

class ChoicePaymentMethodAdapter(private val myDataList: List<PaymentMethod>) : RecyclerView.Adapter<ChoicePaymentMethodAdapter.PaymentMethodViewHolder>() {

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): PaymentMethodViewHolder {
        val view = LayoutInflater.from(parent.context).inflate(R.layout.payment_method, parent, false)
        return PaymentMethodViewHolder(view)
    }

    override fun onBindViewHolder(holder: PaymentMethodViewHolder, position: Int) {
        val item = myDataList[position]
        holder.type.text = item.type
        holder.number.text = item.number
        holder.amount.text = item.amount.toString()
    }

    override fun getItemCount(): Int {
        return myDataList.size
    }

    inner class PaymentMethodViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        val type: TextView = itemView.findViewById(R.id.payment_method_type)
        val number: TextView = itemView.findViewById(R.id.payment_method_number)
        val amount: TextView = itemView.findViewById(R.id.payment_method_amount)
    }
}

