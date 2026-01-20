import streamlit as st
import random
import difflib

CHARACTER_IMAGES = {
    "Michael Scott": "https://upload.wikimedia.org/wikipedia/en/d/dc/MichaelScott.png",
    "Dwight Schrute": "https://upload.wikimedia.org/wikipedia/en/c/cd/Dwight_Schrute.jpg",
    "Jim Halpert": "https://upload.wikimedia.org/wikipedia/en/7/7e/Jim-halpert.jpg",
    "Pam Beesly": "https://upload.wikimedia.org/wikipedia/en/6/67/Pam_Beesley.jpg",
    "Andy Bernard": "https://upload.wikimedia.org/wikipedia/en/4/4f/Andy_Bernard.jpg",
    "Kelly Kapoor": "https://upload.wikimedia.org/wikipedia/en/6/69/Kelly_Kapoor.jpg",
    "Stanley Hudson": "https://upload.wikimedia.org/wikipedia/en/4/4a/Stanley_Hudson.jpg",
}

OFFICE_QUOTES = [
    {"quote": "I'm not superstitious, but I am a little stitious.", "character": "Michael Scott"},
    {"quote": "Identity theft is not a joke, Jim! Millions of families suffer every year.", "character": "Dwight Schrute"},
    {"quote": "I talk a lot, so I've learned to tune myself out.", "character": "Kelly Kapoor"},
    {"quote": "Bears. Beets. Battlestar Galactica.", "character": "Jim Halpert"},
    {"quote": "I wish there was a way to know you're in the good old days before you've actually left them.", "character": "Andy Bernard"},
    {"quote": "I am Beyoncé, always.", "character": "Michael Scott"},
    {"quote": "Sometimes I’ll start a sentence and I don’t even know where it’s going.", "character": "Michael Scott"},
    {"quote": "You miss 100% of the shots you don’t take. – Wayne Gretzky", "character": "Michael Scott"},
    {"quote": "Whenever I'm about to do something, I think, 'Would an idiot do that?' and if they would, I do not do that thing.", "character": "Dwight Schrute"},
    {"quote": "I'm an early bird and I'm a night owl. So I'm wise and I have worms.", "character": "Michael Scott"},
    {"quote": "I feel God in this Chili’s tonight.", "character": "Pam Beesly"},
    {"quote": "If I don't have some cake soon, I might die.", "character": "Stanley Hudson"},
    {"quote": "I declare bankruptcy!", "character": "Michael Scott"},
    {"quote": "I love inside jokes. I hope to be a part of one someday.", "character": "Michael Scott"},
    {"quote": "There’s a lot of beauty in ordinary things. Isn’t that kind of the point?", "character": "Pam Beesly"},
]

def get_random_quote():
    return random.choice(OFFICE_QUOTES)

def split_quote(text, difficulty="Medium"):
    words = text.split()

    if difficulty == "Easy":
        split_point = max(2, len(words) // 3)
    elif difficulty == "Hard":
        split_point = max(5, len(words) * 2 // 3)
    else:  # Medium
        split_point = max(3, len(words) // 2)

    start = " ".join(words[:split_point])
    end = " ".join(words[split_point:])
    return start, end

st.set_page_config(page_title="Finish the Office Quote", page_icon="📺")
st.title("📺 Finish the Office Quote")

difficulty = st.selectbox("Difficulty", ["Easy", "Medium", "Hard"])

if "quote" not in st.session_state:
    quote = get_random_quote()
    start, end = split_quote(quote["quote"], difficulty)

    st.session_state.quote = quote
    st.session_state.start = start
    st.session_state.end = end
    st.session_state.checked = False
    st.session_state.score = None

character = st.session_state.quote["character"]
image_url = CHARACTER_IMAGES.get(character)

# Show character image immediately with the quote
if image_url:
    st.image(image_url, width=220, caption=character)

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
    st.caption(f"— {character}")

if st.button("Next Quote"):
    for key in ["quote", "start", "end", "checked", "score"]:
        st.session_state.pop(key, None)
    st.rerun()
