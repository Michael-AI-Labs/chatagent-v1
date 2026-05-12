import requests
import streamlit as st


API_URL = "http://127.0.0.1:8000/chat"
MAX_HISTORY = 30


st.set_page_config(
    page_title="ChatAgentv1",
    page_icon="🤖",
)

st.title("🤖 ChatAgentv1")
st.caption("Streamlit UI → FastAPI → OpenAI Agents SDK")

if st.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.rerun()


if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hello! I'm ChatAgentv1. How can I help you today?"
        }
    ]


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


user_message = st.chat_input("Ask ChatAgentv1 something...")


if user_message:
    st.session_state.messages.append(
        {"role": "user", "content": user_message}
    )
    conversation_history = st.session_state.messages[-MAX_HISTORY:]

    with st.chat_message("user"):
        st.markdown(user_message)

    with st.chat_message("assistant"):
        with st.spinner("ChatAgentv1 is thinking..."):
            try:
                response = requests.post(
                    API_URL,
                    json={
                        "message": user_message,
                        "messages": conversation_history,
                    },
                    timeout=30,
                )
                response.raise_for_status()

                assistant_response = response.json()["response"]
                st.markdown(assistant_response)

                st.session_state.messages.append(
                    {"role": "assistant", "content": assistant_response}
                )

            except requests.exceptions.RequestException as error:
                error_message = f"Request failed: {error}"
                st.error(error_message)

                st.session_state.messages.append(
                    {"role": "assistant", "content": error_message}
                )
