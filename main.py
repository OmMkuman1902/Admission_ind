import streamlit as st
import time
from Lanchainback import create_vector_db, get_qa_chain

# Page configuration
st.set_page_config(page_title="College Admission Assistant", page_icon="🎓", layout="centered")

# Custom CSS for styling
st.markdown(
    """
    <style>
    .big-title {
        font-size: 48px;
        font-weight: bold;
        color: #4CAF50;
        text-align: center;
    }
    .answer-box {
        background-color: #e8f5e9;
        border-left: 5px solid #4CAF50;
        padding: 20px;
        margin-top: 20px;
        border-radius: 8px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .stTextInput>div>div>input {
        background-color: #f1f8e9;
        border: 2px solid #4CAF50;
        border-radius: 8px;
        padding: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.markdown('<div class="big-title">College Admission Assistant 🌱</div>', unsafe_allow_html=True)
st.markdown("---")

# Knowledge base creation button
st.subheader("Create your Knowledgebase")
if st.button("✨ Build Knowledgebase"):
    with st.spinner("Building knowledgebase... ⏳"):
        create_vector_db()
    st.success("Knowledgebase created successfully! ✅")

st.markdown("---")

# Question input area
st.subheader("Ask Your Question")
question = st.text_input("Type your admission-related question here 👇")

if question:
    # Step 1: Show Thank You message for 2 seconds
    with st.spinner('🙏 Thanks for your question!'):
        time.sleep(2)

    # Step 2: Fetch and show the answer
    chain = get_qa_chain()
    with st.spinner('🤔 Fetching the best answer...'):
        response = chain.invoke(question)

    # Step 3: Display the answer
    st.markdown('<div class="answer-box">', unsafe_allow_html=True)
    st.subheader("📚 Answer")
    st.write(response["result"])
    st.markdown('</div>', unsafe_allow_html=True)
