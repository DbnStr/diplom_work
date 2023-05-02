package ru.bmstu.mobileapp

import android.app.Activity
import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.widget.Button
import androidx.activity.result.contract.ActivityResultContracts
import androidx.activity.result.registerForActivityResult
import androidx.navigation.NavController
import androidx.navigation.fragment.NavHostFragment
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response
import ru.bmstu.mobileapp.databinding.ActivityMainBinding
import ru.bmstu.mobileapp.models.Basket
import ru.bmstu.mobileapp.retrofit.Common
import ru.bmstu.mobileapp.retrofit.RetrofitServices

class MainActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMainBinding
    private lateinit var navController: NavController

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

        val navHostFragment =
            supportFragmentManager.findFragmentById(R.id.main_fragment_container)
                    as NavHostFragment
        navController = navHostFragment.navController

        val qrCodeButton = findViewById<Button>(R.id.qr_code_button)
        qrCodeButton.setOnClickListener {
            val intent = Intent(this, BarCodeActivity::class.java)
            startForURL.launch(intent)
            startActivity(intent)
        }
    }
}