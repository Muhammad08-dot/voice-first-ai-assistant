<div align="center">
  <h1>🎙️ Voice-First AI Assistant (JARVIS)</h1>
  <p><strong>A futuristic, fully voice-driven AI interface for seamless human-computer interaction.</strong></p>
</div>

## 🚀 Overview
**Project JARVIS** is a voice-first AI operating system that bypasses the traditional keyboard interface. You speak to it, it transcribes your voice in real-time using Whisper, processes your intent using an LLM, and responds with hyper-realistic voice synthesis.

![Dashboard Demo](/C:/Users/hp/.gemini/antigravity-ide/brain/fdf49048-b37f-4711-af04-f256131d4933/voice_ai_dashboard_1786417973010.png)

## ✨ Features
- **Speech-to-Text Pipeline:** Ultra-low latency transcription using OpenAI's Whisper API.
- **LLM Brain:** Context-aware conversations powered by GPT-4o or local Llama 3 models.
- **Text-to-Speech Output:** Hyper-realistic, customizable voice profiles via ElevenLabs.
- **Futuristic UI:** An interactive glowing orb that visually responds to audio input in real-time.

## 🛠️ Tech Stack
- **Frontend/UI:** [Streamlit](https://streamlit.io/) with custom CSS animations
- **Audio Processing:** PyAudio, WebRTC
- **AI Models:** Whisper (STT), LangChain (LLM), ElevenLabs (TTS)

## 📦 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Muhammad08-dot/voice-first-ai-assistant.git
   cd voice-first-ai-assistant
   ```

2. **Install dependencies:**
   ```bash
   pip install streamlit langchain
   ```

3. **Run the application:**
   ```bash
   streamlit run streamlit_app.py
   ```

## 📄 License
This project is licensed under the MIT License.
