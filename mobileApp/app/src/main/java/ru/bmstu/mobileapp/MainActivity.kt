package ru.bmstu.mobileapp

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.widget.Button
import ru.bmstu.mobileapp.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {
    private lateinit var binding: ActivityMainBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        Log.d("MainActivity", "OnCreate")
        binding = ActivityMainBinding.inflate(layoutInflater)
        val view = binding.root
        setContentView(view)

        val qrCodeButton = findViewById<Button>(R.id.qr_code_button)
        qrCodeButton.setOnClickListener {
            val intent = Intent(this, BarCodeActivity::class.java)
            startActivity(intent)
        }
    }
}