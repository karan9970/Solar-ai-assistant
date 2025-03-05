import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# ✅ Load Gemini API Key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY") or "YOUR_GEMINI_API_KEY"

if not api_key or "YOUR_GEMINI_API_KEY" in api_key:
    st.error("❌ API Key not found! Please check your .env file or manually set it.")

# ✅ Configure Gemini API
genai.configure(api_key=api_key)

# ✅ Function to Get AI Response from Gemini
def get_gemini_response(question):
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(question)
        return response.text
    except Exception as e:
        return f"❌ Error: {str(e)}"
    

# ✅ Streamlit UI
st.set_page_config(page_title="🌞 Solar Industry AI Assistant", layout="wide")
st.title("🌞 Solar Industry AI Assistant")
st.markdown("**🔹 Ask me anything about solar energy!**")

# ✅ User Input
input_text = st.text_input("💡 Enter your question here:")

# ✅ Button to Get Answer
if st.button("🔍 Get Answer"):
    if input_text:
        with st.spinner("🔄 Thinking..."):
            response = get_gemini_response(input_text)
        st.subheader("📢 AI Response:")
        st.write(response)
    else:
        st.warning("⚠️ Please enter a question first!")

# ✅ Sidebar: Setup & Deployment Instructions
st.sidebar.header("⚙️ Setup & Instructions")
st.sidebar.header("Install requirements :: pip install -r requirements.txt")
st.sidebar.header("execute : streamlit run app.py")
