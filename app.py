import os
import streamlit as st

from graph.finance_graph import finance_graph
from streamlit_mic_recorder import mic_recorder

from voice import VoiceAssistant
from config.settings import GROQ_API_KEY


# ==========================================================
# Initialization
# ==========================================================

voice = VoiceAssistant(GROQ_API_KEY)

st.set_page_config(
    page_title="💰 AI Personal Finance Coach",
    page_icon="💰",
    layout="wide"
)

st.title("💰 AI Personal Finance Coach")

st.caption(
    "Expense Analysis • Budget Planning • Financial Goals • Voice Assistant"
)


# ==========================================================
# Session State
# ==========================================================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "income" not in st.session_state:
    st.session_state.income = 0

if "expenses" not in st.session_state:
    st.session_state.expenses = {}

if "goal" not in st.session_state:
    st.session_state.goal = ""

if "history" not in st.session_state:
    st.session_state.history = []


# ==========================================================
# Chat History
# ==========================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


# ==========================================================
# Voice Input
# ==========================================================

st.subheader("🎤 Speak")

audio = mic_recorder(

    start_prompt="🎙 Start Recording",

    stop_prompt="⏹ Stop Recording",

    key="voice",

    use_container_width=True

)

typed_input = st.chat_input(
    "Ask about your finances..."
)

user_input = None


# ==========================================================
# Voice → Text
# ==========================================================

if audio:

    audio_path = "temp.wav"

    with open(audio_path, "wb") as file:

        file.write(audio["bytes"])

    try:

        user_input = voice.speech_to_text(
            audio_path
        )

        st.success("✅ Voice Recognized")

        st.write(user_input)

    except Exception as e:

        st.error(e)


# ==========================================================
# Typed Input
# ==========================================================

if typed_input:

    user_input = typed_input
# ==========================================================
# Process User Message
# ==========================================================

if user_input:

    # ----------------------------
    # Display User Message
    # ----------------------------

    st.session_state.messages.append(

        {

            "role": "user",

            "content": user_input

        }

    )

    with st.chat_message("user"):

        st.markdown(user_input)

    # ----------------------------
    # Build Initial State
    # ----------------------------

    state = {

        "user_query": user_input,

        "monthly_income":
        st.session_state.income,

        "expenses":
        st.session_state.expenses,

        "financial_goal":
        st.session_state.goal,

        "history":
        st.session_state.history

    }

    # ----------------------------
    # Execute LangGraph
    # ----------------------------

    with st.chat_message("assistant"):

        with st.spinner("Analyzing your finances..."):

            result = finance_graph.invoke(state)

    # ----------------------------
    # Update Session State
    # ----------------------------

    st.session_state.income = result.get(

        "monthly_income",

        st.session_state.income

    )

    st.session_state.expenses = result.get(

        "expenses",

        st.session_state.expenses

    )

    st.session_state.goal = result.get(

        "financial_goal",

        st.session_state.goal

    )

    st.session_state.history = result.get(

        "history",

        st.session_state.history

    )

    response = result.get(

        "final_response",

        "Sorry, I couldn't generate a response."

    )

    # ----------------------------
    # Display Assistant Message
    # ----------------------------

    with st.chat_message("assistant"):

        st.markdown(response)

    st.session_state.messages.append(

        {

            "role": "assistant",

            "content": response

        }

    )

    # ----------------------------
    # Voice Response
    # ----------------------------

    try:

        audio_file = voice.speak(response)

        if os.path.exists(audio_file):

            with open(audio_file, "rb") as file:

                st.audio(

                    file.read(),

                    format="audio/mp3"

                )

    except Exception as e:

        st.warning(

            f"Voice unavailable : {e}"

        )
# ==========================================================
# Sidebar
# ==========================================================

with st.sidebar:

    st.header("📊 Financial Profile")

    st.metric(

        label="Monthly Income",

        value=f"₹{st.session_state.income:,.2f}"

    )

    st.divider()

    st.subheader("💸 Expenses")

    if st.session_state.expenses:

        total = 0

        for category, amount in st.session_state.expenses.items():

            st.write(
                f"**{category}** : ₹{amount:,.2f}"
            )

            total += amount

        st.divider()

        st.metric(
            "Total Expenses",
            f"₹{total:,.2f}"
        )

        st.metric(
            "Remaining Balance",
            f"₹{st.session_state.income-total:,.2f}"
        )

    else:

        st.info(
            "No expenses available."
        )

    st.divider()

    st.subheader("🎯 Financial Goal")

    if st.session_state.goal:

        st.success(
            st.session_state.goal
        )

    else:

        st.info(
            "No financial goal added."
        )

    st.divider()

    if st.button(
        "🗑 Clear Conversation",
        use_container_width=True
    ):

        st.session_state.messages = []

        st.session_state.history = []

        st.session_state.expenses = {}

        st.session_state.goal = ""

        st.session_state.income = 0

        if os.path.exists("response.mp3"):

            os.remove("response.mp3")

        if os.path.exists("temp.wav"):

            os.remove("temp.wav")

        st.rerun()