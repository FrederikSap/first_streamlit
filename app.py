import streamlit as st
import requests
import random
import difflib

API_URL = "https://officeapi.dev/api/quotes/random"

def get_random_quote():
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()
        data = response.json()

        # API returns: { "data": { "content": "...", "character": { "firstname": "...", "lastname": "..." } } }
        quote_text = data["data"]["content"]
        character = (
            data["data"]["character"]["firstname"]
            + " "
            + data["data"]["character"]["lastname"]
        )

        return {
            "quote": quote_text,
            "character": character.strip()
        }

    except Exception as e:
        # Fallback quotes if API fails
        fallback_quotes = [
            {
                "quote": "I'm not superstitious, but I am a little stitious.",
                "character": "Michael Scott"
            },
            {
                "quote": "Identity theft is not a joke, Jim! Millions of families suffer every year.",
                "character": "Dwight Schrute"
            },
            {
                "quote": "I talk a lot, so I've learned to tune myself out.",
                "character": "Kelly Kapoor"
            }
        ]
        return random.choice(fallback_quotes)

def split_quote(text):
    words = text.split()
    split_point = max(3, len(words) // 2)
    start = " ".join(words[:split_point])
    end = " ".join(words[split_point:])
    return start, end

st.set_page_config(page_title="Finish the Office Quote", page_icon="📺")
st.title("📺 Finish the Office Quote")

if "quote" not in st.session_state:
    quote = get_random_quote()
    start, end = split_quote(quote["quote"])

    st.session_state.quote = quote
    st.session_state.start = start
    st.session_state.end = end
    st.session_state.checked = False
    st.session_state.score = None

st.subheader("Complete this quote:")
st.markdown(f"**“{st.session_state.start} ...”**")

user_input = st.text_input("Your guess:")

if st.button("Check Answer"):
    if user_input.strip():
        similarity = difflib.SequenceMatcher(
            None,
            user_input.lower().strip(),
            st.session_state.end.lower().strip()
        ).ratio() * 100

        st.session_state.score = similarity
        st.session_state.checked = True

if st.session_state.checked:
    st.divider()
    st.subheader("Results")

    if st.session_state.score >= 80:
        st.success("🎉 Nailed it!")
    elif st.session_state.score >= 50:
        st.warning("😬 Close enough!")
    else:
        st.error("❌ Not quite!")

    st.write("**Your answer:**")
    st.write(user_input)

    st.write("**Correct ending:**")
    st.write(st.session_state.end)

    st.caption(f"Similarity score: {int(st.session_state.score)}%")
    st.caption(f"— {st.session_state.quote['character']}")

if st.button("Next Quote"):
    for key in ["quote", "start", "end", "checked", "score"]:
        st.session_state.pop(key, None)
    st.rerun()
