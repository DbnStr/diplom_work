package ru.bmstu.mobileapp.fragments.invoice

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView
import ru.bmstu.mobileapp.R
import ru.bmstu.mobileapp.models.Item

class InvoiceAdapter(private val myDataList: List<Item>) : RecyclerView.Adapter<InvoiceAdapter.ItemViewHolder>() {

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ItemViewHolder {
        val view = LayoutInflater.from(parent.context).inflate(R.layout.invoice_item, parent, false)
        return ItemViewHolder(view)
    }

    override fun onBindViewHolder(holder: ItemViewHolder, position: Int) {
        val item = myDataList[position]
        holder.name.text = item.name
        holder.oneItemCost.text = item.oneItemCost
        holder.quantity.text = item.quantity
        holder.amount.text = item.amount
    }

    override fun getItemCount(): Int {
        return myDataList.size
    }

    inner class ItemViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        val name: TextView = itemView.findViewById(R.id.invoice_item_name)
        val oneItemCost: TextView = itemView.findViewById(R.id.invoice_item_one_item_cost)
        val quantity: TextView = itemView.findViewById(R.id.invoice_item_quantity)
        val amount: TextView = itemView.findViewById(R.id.invoice_item_total_amount)
    }
}

