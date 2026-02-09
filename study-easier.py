import streamlit as st
import google.generativeai as genai
import PyPDF2

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(
    page_title="Study Easier",
    page_icon="🧠",
    layout="wide"
)

# -------------------------
# DARK TECH THEME
# -------------------------
st.markdown("""
<style>
.stApp { background-color: #0f172a; color: #e5e7eb; }
section[data-testid="stSidebar"] {
    background-color: #020617;
    border-right: 1px solid #1e293b;
}
button {
    background-color: #020617 !important;
    color: #38bdf8 !important;
    border: 1px solid #38bdf8 !important;
}
textarea {
    background-color: #020617 !important;
    color: #e5e7eb !important;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# GEMINI CONFIG
# -------------------------
genai.configure(api_key="GOOGLE_API_KEY")
model = genai.GenerativeModel("gemini-2.5-flash")

# -------------------------
# SESSION STATE INIT
# -------------------------
defaults = {
    "student": None,
    "messages": [],
    "mode": "Chat Mode",
    "flashcards": [],
    "notes_text": ""
}

for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

# -------------------------
# SIDEBAR – STUDENT PROFILE
# -------------------------
with st.sidebar:
    st.markdown("## 🧠 Study Easier")

    if not st.session_state.student:
        st.session_state.student = st.text_input("👤 Enter Student Name")
        st.stop()

    st.caption(f"Logged in as **{st.session_state.student}**")
    st.divider()

    st.markdown("### 📚 Study Mode")
    st.session_state.mode = st.radio(
        "",
        ["Chat Mode", "Q&A Mode", "Quiz Mode", "Flashcards Mode"]
    )

    st.divider()

    st.markdown("### 📄 Upload Notes (PDF / TXT)")
    uploaded = st.file_uploader("", type=["pdf", "txt"])

    if uploaded:
        if uploaded.type == "application/pdf":
            reader = PyPDF2.PdfReader(uploaded)
            st.session_state.notes_text = " ".join(
                page.extract_text() for page in reader.pages
            )
        else:
            st.session_state.notes_text = uploaded.read().decode()

        st.success("Notes uploaded successfully")

    st.divider()

    if st.button("➕ New Session"):
        st.session_state.messages = []
        st.rerun()

# -------------------------
# PROMPT BUILDER
# -------------------------
def build_prompt(mode, user_input):
    context = f"\n\nUse these notes if helpful:\n{st.session_state.notes_text[:4000]}" if st.session_state.notes_text else ""

    if mode == "Chat Mode":
        return user_input + context

    if mode == "Q&A Mode":
        return f"Answer clearly for exams:\n{user_input}{context}"

    if mode == "Quiz Mode":
        return f"""
Create 3 MCQs with options A–D.
After questions, write:
Correct Answers:

Topic: {user_input}
{context}
"""

    if mode == "Flashcards Mode":
        return f"""
Create flashcards.
Format:
Term: ...
Explanation: ...

Topic: {user_input}
{context}
"""

# -------------------------
# MAIN UI
# -------------------------
st.markdown("## 🧠 Study Easier")
st.caption(f"Mode: **{st.session_state.mode}**")

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Enter topic or question...")

# -------------------------
# CHAT LOGIC
# -------------------------
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    prompt = build_prompt(st.session_state.mode, user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = model.generate_content(prompt)
            reply = response.text
            st.markdown(reply)

            # Save flashcards
            if st.session_state.mode == "Flashcards Mode":
                if st.button("💾 Save Flashcards"):
                    st.session_state.flashcards.append(reply)
                    st.success("Flashcards saved")

    st.session_state.messages.append({"role": "assistant", "content": reply})

# -------------------------
# FLASHCARDS VIEW
# -------------------------
if st.session_state.flashcards:
    st.divider()
    st.markdown("### 🧩 Saved Flashcards")

    for i, card in enumerate(st.session_state.flashcards, 1):
        with st.expander(f"Flashcard Set {i}"):
            st.markdown(card)
