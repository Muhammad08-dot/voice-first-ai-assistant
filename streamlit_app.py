import streamlit as st
import time
import base64

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Project JARVIS - Voice OS",
    page_icon="🎙️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- CUSTOM CSS ---
st.markdown("""
<style>
    .stApp { background-color: #050510; color: #00ffff; }
    h1, h2, h3 { color: #00ffff; font-family: 'Courier New', Courier, monospace; text-align: center; }
    
    .orb-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 40px 0;
    }
    
    /* Glowing Orb CSS */
    .orb {
        width: 150px;
        height: 150px;
        background: radial-gradient(circle, #00ffff 0%, #0088ff 50%, #000033 100%);
        border-radius: 50%;
        box-shadow: 0 0 40px #00ffff, 0 0 80px #0088ff;
        animation: pulse 2s infinite ease-in-out;
    }
    
    .orb.listening {
        background: radial-gradient(circle, #ff00ff 0%, #8800ff 50%, #330033 100%);
        box-shadow: 0 0 50px #ff00ff, 0 0 100px #8800ff;
        animation: fast-pulse 0.5s infinite alternate;
    }
    
    @keyframes pulse {
        0% { transform: scale(0.95); opacity: 0.8; }
        50% { transform: scale(1.05); opacity: 1; }
        100% { transform: scale(0.95); opacity: 0.8; }
    }
    
    @keyframes fast-pulse {
        0% { transform: scale(0.9); box-shadow: 0 0 20px #ff00ff; }
        100% { transform: scale(1.2); box-shadow: 0 0 80px #ff00ff; }
    }
    
    .chat-bubble-user {
        background-color: #1a1a2e;
        border: 1px solid #00ffff;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 10px;
        text-align: right;
    }
    
    .chat-bubble-ai {
        background-color: #0f3460;
        border: 1px solid #0088ff;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 10px;
        text-align: left;
    }
    
    .status-text { text-align: center; font-family: monospace; color: #5555ff; margin-bottom: 20px;}
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR SETTINGS ---
with st.sidebar:
    st.header("⚙️ System Preferences")
    st.selectbox("Voice Persona", ["JARVIS (British Male)", "FRIDAY (Irish Female)", "GLaDOS (Robotic)"])
    st.selectbox("LLM Backend", ["GPT-4o", "Claude 3.5", "Llama 3 Local"])
    st.slider("Speech Speed", 0.5, 2.0, 1.0)
    st.markdown("---")
    st.info("Uses Whisper API for STT and ElevenLabs for TTS.")

# --- MAIN APP ---
st.title("P R O J E C T : J A R V I S")

# State Management
if "listening" not in st.session_state:
    st.session_state.listening = False
if "conversation" not in st.session_state:
    st.session_state.conversation = [
        {"role": "ai", "text": "Online and ready. How may I assist you today, sir?"}
    ]

# Orb Visualizer
orb_class = "orb listening" if st.session_state.listening else "orb"
st.markdown(f'<div class="orb-container"><div class="{orb_class}"></div></div>', unsafe_allow_html=True)

# Status
status_msg = "Listening to microphone input..." if st.session_state.listening else "System Idle. Awaiting voice command."
st.markdown(f'<div class="status-text">{status_msg}</div>', unsafe_allow_html=True)

# Controls
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if not st.session_state.listening:
        if st.button("🎙️ Initialize Voice Command", use_container_width=True):
            st.session_state.listening = True
            st.rerun()
    else:
        if st.button("🛑 Stop Recording", type="primary", use_container_width=True):
            st.session_state.listening = False
            # Simulate processing
            with st.spinner("Transcribing via Whisper..."):
                time.sleep(1)
            with st.spinner("Processing via LLM..."):
                time.sleep(1.5)
            with st.spinner("Synthesizing Voice..."):
                time.sleep(1)
            
            # Add to conversation
            st.session_state.conversation.append({"role": "user", "text": "Can you summarize my unread emails from Tony Stark?"})
            st.session_state.conversation.append({"role": "ai", "text": "Right away. You have 3 unread messages from Mr. Stark regarding the new arc reactor schematics. Would you like me to read them out loud?"})
            st.rerun()

st.markdown("---")

# Conversation Transcript
st.subheader("Transcript Log")
for msg in reversed(st.session_state.conversation):
    if msg["role"] == "user":
        st.markdown(f'<div class="chat-bubble-user"><strong>You:</strong><br>{msg["text"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="chat-bubble-ai"><strong>JARVIS:</strong><br>{msg["text"]}</div>', unsafe_allow_html=True)
