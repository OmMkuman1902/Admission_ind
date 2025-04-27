import streamlit as st
import time
from datetime import datetime
from Lanchainback import create_vector_db, get_qa_chain

# Page config
st.set_page_config(page_title="College Admission Chatbot", page_icon="🤖", layout="centered")

# --- Custom CSS ---
st.markdown("""
    <style>
    .chat-message {
        padding: 10px 15px;
        margin-bottom: 10px;
        border-radius: 10px;
        max-width: 80%;
        word-wrap: break-word;
        display: inline-block;
    }
    .user-message {
        background-color: #DCF8C6;
        align-self: flex-end;
        margin-left: auto;
    }
    .bot-message {
        background-color: #F1F0F0;
        align-self: flex-start;
        margin-right: auto;
    }
    .chat-container {
        display: flex;
        flex-direction: column;
    }
    div[data-baseweb="input"] > div {
        border: 2px solid #00ccff;
        background-color: #e6f7ff;
        border-radius: 8px;
        padding: 8px;
        box-shadow: 0 0 10px #00ccff;
    }
    .timestamp {
        font-size: 10px;
        color: gray;
        margin-top: 2px;
    }
    .chat-row {
        display: flex;
        align-items: center;
    }
    .chat-avatar {
        width: 30px;
        height: 30px;
        border-radius: 50%;
        margin: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# --- Title ---
st.markdown("<h1 style='text-align: center;'>🎓 College Admission Assistant </h1>", unsafe_allow_html=True)
st.markdown("---")

# --- Initialize session_state ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# --- Clear Chat Button ---
col1, col2 = st.columns([8, 2])
with col2:
    if st.button("🗑️ Clear Chat"):
        st.session_state.chat_history = []

# --- Chat Input Form ---
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("💬 Ask me anything about college admissions:", key="user_input")
    submit_button = st.form_submit_button(label="Send")

# --- Process input ---
if submit_button and user_input:
    current_time = datetime.now().strftime("%I:%M %p")
    st.session_state.chat_history.append({"sender": "user", "message": user_input, "time": current_time})

    # Show Typing...
    typing_placeholder = st.empty()
    with typing_placeholder.container():
        st.markdown(f"""
            <div class='chat-container'>
                <div class='chat-row'>
                    <img src="https://cdn-icons-png.flaticon.com/512/4712/4712109.png" class="chat-avatar">
                    <div class='chat-message bot-message'>🤔 Typing...</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
    time.sleep(2)  # Simulate bot thinking

    # Now get real reply
    chain = get_qa_chain()
    response = chain.invoke(user_input)
    bot_reply = response["result"]

    # Save bot reply
    current_time = datetime.now().strftime("%I:%M %p")
    st.session_state.chat_history.append({"sender": "bot", "message": bot_reply, "time": current_time})

    typing_placeholder.empty()  # Remove Typing message

# --- Display Chat History ---
for chat in st.session_state.chat_history:
    if chat["sender"] == "user":
        st.markdown(f"""
            <div class='chat-container'>
                <div class='chat-row' style="justify-content: flex-end;">
                    <div>
                        <div class='chat-message user-message'>🙋‍♂️ {chat['message']}</div>
                        <div class='timestamp' style="text-align:right;">{chat['time']}</div>
                    </div>
                    <img src="https://cdn-icons-png.flaticon.com/512/1946/1946429.png" class="chat-avatar">
                </div>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
            <div class='chat-container'>
                <div class='chat-row'>
                    <img src="https://cdn-icons-png.flaticon.com/512/4712/4712109.png" class="chat-avatar">
                    <div>
                        <div class='chat-message bot-message'>🤖 {chat['message']}</div>
                        <div class='timestamp'>{chat['time']}</div>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)

# --- Auto-Scroll Script ---
scroll_script = """
<script>
var chatDiv = window.parent.document.querySelector('section.main');
if(chatDiv){
    chatDiv.scrollTo(0, chatDiv.scrollHeight);
}
</script>
"""
st.markdown(scroll_script, unsafe_allow_html=True)
