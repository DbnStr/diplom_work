package ru.bmstu.mobileapp.fragments.choice_payment_method

import android.annotation.SuppressLint
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.RadioButton
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView
import ru.bmstu.mobileapp.R
import ru.bmstu.mobileapp.models.PaymentMethod

class ChoicePaymentMethodAdapter(private val myDataList: List<PaymentMethod>) : RecyclerView.Adapter<ChoicePaymentMethodAdapter.PaymentMethodViewHolder>() {

    private var selectedPaymentMethod = -1

    @SuppressLint("NotifyDataSetChanged")
    fun setSelectedPaymentMethod(position: Int) {
        selectedPaymentMethod = position
        notifyDataSetChanged()
    }

    fun getSelectedPaymentMethod(): Int {
        return selectedPaymentMethod
    }


    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): PaymentMethodViewHolder {
        val view = LayoutInflater.from(parent.context).inflate(R.layout.payment_method, parent, false)
        return PaymentMethodViewHolder(view, this)
    }

    @SuppressLint("SetTextI18n")
    override fun onBindViewHolder(holder: PaymentMethodViewHolder, position: Int) {
        val item = myDataList[position]
        holder.number.text = item.number!!.substring(item.number!!.length - 4, item.number!!.length)
        holder.amount.text = "%.2f".format(item.amount)
        holder.radioButton.isChecked = position == selectedPaymentMethod
    }

    override fun getItemCount(): Int {
        return myDataList.size
    }

    inner class PaymentMethodViewHolder(itemView: View, private val adapter: ChoicePaymentMethodAdapter) : RecyclerView.ViewHolder(itemView) {
        val number: TextView = itemView.findViewById(R.id.payment_method_number)
        val amount: TextView = itemView.findViewById(R.id.payment_method_amount)
        val radioButton: RadioButton = itemView.findViewById(R.id.radioButton)

        init {
            radioButton.setOnClickListener {
                val position = adapterPosition
                if (position != RecyclerView.NO_POSITION) {
                    adapter.setSelectedPaymentMethod(position)
                }
            }
        }
    }
}

