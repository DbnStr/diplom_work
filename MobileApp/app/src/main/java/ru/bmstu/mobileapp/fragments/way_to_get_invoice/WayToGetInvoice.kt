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
import androidx.activity.result.contract.ActivityResultContracts
import ru.bmstu.mobileapp.R
import ru.bmstu.mobileapp.activities.BarCodeActivity

class WayToGetInvoice : Fragment() {

    private val startForURL = registerForActivityResult(ActivityResultContracts.StartActivityForResult()) { result ->
        if (result.resultCode == Activity.RESULT_OK) {
            val data: Intent? = result.data
            if (data != null) {
                Log.d("QR-code payload", data.getStringExtra("qr_payload")!!)
            } else {
                Log.d("QR-code payload", "null payload")
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
        return view
    }
}