package ru.bmstu.mobileapp.fragments.way_to_get_invoice

import android.app.Activity
import android.content.Intent
import android.os.Bundle
import android.util.Log
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Button
import android.widget.Toast
import androidx.activity.result.contract.ActivityResultContracts
import androidx.navigation.NavController
import androidx.navigation.fragment.findNavController
import ru.bmstu.mobileapp.R
import ru.bmstu.mobileapp.SERVER_HOST_NAME
import ru.bmstu.mobileapp.activities.BarCodeActivity

class WayToGetInvoice : Fragment() {

    private lateinit var navController: NavController

    private val startForURL = registerForActivityResult(ActivityResultContracts.StartActivityForResult()) { result ->
        if (result.resultCode == Activity.RESULT_OK) {
            val data: Intent? = result.data
            if (data != null) {
                val qrCodePayload : String = data.getStringExtra("qr_payload")!!
                Log.d("QR-code payload", qrCodePayload)

                if (qrCodePayload.startsWith(SERVER_HOST_NAME)) {
                    val bundle = Bundle()
                    bundle.putString("qrCodePayload", qrCodePayload)
                    navController.navigate(R.id.action_way_to_get_invoice_to_invoice, bundle)
                } else {
                    Toast.makeText(activity, "Некорректный QR-код", Toast.LENGTH_LONG).show()
                }
            } else {
                Log.d("QR-code payload", "null payload")
                Toast.makeText(activity, "Некорректный QR-код", Toast.LENGTH_LONG).show()
            }
        }
    }

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        val view =  inflater.inflate(R.layout.fragment_way_to_get_invoice, container, false)
        val qrScannerButton: Button = view.findViewById(R.id.qr_scanner_button)
        qrScannerButton.setOnClickListener {
            val intent = Intent(activity, BarCodeActivity::class.java)
            startForURL.launch(intent)
            startActivity(intent)
        }
        navController = this.findNavController()
        return view
    }
}