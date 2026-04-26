package com.digitaltrustshield.publicshell

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Button
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.NavigationBar
import androidx.compose.material3.NavigationBarItem
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            MaterialTheme {
                DigitalTrustShieldShell()
            }
        }
    }
}

private enum class Tab(val label: String) {
    Verify("Verification"),
    Chat("Chatbot")
}

@Composable
fun DigitalTrustShieldShell() {
    var tab by remember { mutableStateOf(Tab.Verify) }

    Scaffold(
        bottomBar = {
            NavigationBar {
                NavigationBarItem(
                    selected = tab == Tab.Verify,
                    onClick = { tab = Tab.Verify },
                    icon = { Text("DTS") },
                    label = { Text(Tab.Verify.label) },
                )
                NavigationBarItem(
                    selected = tab == Tab.Chat,
                    onClick = { tab = Tab.Chat },
                    icon = { Text("AI") },
                    label = { Text(Tab.Chat.label) },
                )
            }
        }
    ) { padding ->
        when (tab) {
            Tab.Verify -> VerificationShell(padding)
            Tab.Chat -> ChatbotShell(padding)
        }
    }
}

@Composable
private fun VerificationShell(padding: PaddingValues) {
    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(padding)
            .padding(24.dp),
        verticalArrangement = Arrangement.spacedBy(16.dp),
    ) {
        Text("Digital Trust Shield", style = MaterialTheme.typography.headlineMedium, fontWeight = FontWeight.Black)
        Text("Public UI shell. The private build lets users select an image and verify it through the backend.")
        Button(onClick = { /* Private build opens image picker and calls /api/verify. */ }, modifier = Modifier.fillMaxWidth()) {
            Text("Select Image")
        }
        Button(onClick = { /* Private build uploads the image and displays AUTHENTIC/TAMPERED. */ }, modifier = Modifier.fillMaxWidth()) {
            Text("Verify")
        }
    }
}

@Composable
private fun ChatbotShell(padding: PaddingValues) {
    var question by remember { mutableStateOf("") }

    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(padding)
            .padding(24.dp),
        verticalArrangement = Arrangement.spacedBy(16.dp),
    ) {
        Text("DTS Sahayak", style = MaterialTheme.typography.headlineMedium, fontWeight = FontWeight.Black)
        Text("Public UI shell. The private build supports Tavily + Groq answers, voice input, English, Kannada, and Hindi.")
        OutlinedTextField(
            value = question,
            onValueChange = { question = it },
            label = { Text("Ask a question") },
            modifier = Modifier.fillMaxWidth(),
        )
        Button(onClick = { /* Private build calls /api/chat. */ }, modifier = Modifier.fillMaxWidth()) {
            Text("Ask Chatbot")
        }
    }
}
