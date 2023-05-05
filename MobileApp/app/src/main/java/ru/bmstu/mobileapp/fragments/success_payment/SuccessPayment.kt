package ru.bmstu.mobileapp.fragments.success_payment

import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Button
import androidx.navigation.NavController
import androidx.navigation.fragment.findNavController
import ru.bmstu.mobileapp.R

class SuccessPayment : Fragment() {

    private lateinit var navController: NavController

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        val view = inflater.inflate(R.layout.fragment_success_payment, container, false)

        navController = this.findNavController()
        val backToMainMenuButton : Button = view.findViewById(R.id.back_to_main_menu_button)

        backToMainMenuButton.setOnClickListener {
            navController.navigate(R.id.action_success_payment_to_way_to_get_invoice)
        }

        return view
    }
}