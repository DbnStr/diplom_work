package ru.bmstu.mobileapp

import android.app.Activity
import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.widget.Button
import androidx.activity.result.contract.ActivityResultContracts
import androidx.activity.result.registerForActivityResult
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response
import ru.bmstu.mobileapp.databinding.ActivityMainBinding
import ru.bmstu.mobileapp.models.Basket
import ru.bmstu.mobileapp.retrofit.Common
import ru.bmstu.mobileapp.retrofit.RetrofitServices

class MainActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMainBinding

    lateinit var myService: RetrofitServices

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

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        Log.d("MainActivity", "OnCreate")
        binding = ActivityMainBinding.inflate(layoutInflater)
        val view = binding.root
        setContentView(view)

        myService = Common.retrofitService

        val qrCodeButton = findViewById<Button>(R.id.qr_code_button)
        qrCodeButton.setOnClickListener {
            val intent = Intent(this, BarCodeActivity::class.java)
            startForURL.launch(intent)
            startActivity(intent)
        }
    }

    private fun getBasket() {
        myService.getBasket(1, 1).enqueue(object : Callback<Basket> {
            override fun onFailure(call: Call<Basket>, t: Throwable) {
                Log.d("getBasketHttpRequest", "Failure" + t.toString())
            }

            override fun onResponse(call: Call<Basket>, response: Response<Basket>) {
                Log.d("getBasketHttpRequest", "Success " + response.body())
            }
        })
    }
}