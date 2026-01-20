# office_quotes_app.py
import streamlit as st
import random

# Title
st.title("📺 The Office Quote Generator")

st.write("Click the button to get a random quote from *The Office*.")

# Quote database (you can expand this list)
quotes = [
    ("I'm not superstitious, but I am a little stitious.", "Michael Scott"),
    ("Bears. Beets. Battlestar Galactica.", "Jim Halpert"),
    ("I talk a lot, so I've learned to tune myself out.", "Kelly Kapoor"),
    ("Sometimes I’ll start a sentence and I don’t even know where it’s going. I just hope I find it along the way.", "Michael Scott"),
    ("Identity theft is not a joke, Jim! Millions of families suffer every year!", "Dwight Schrute"),
    ("I declare bankruptcy!", "Michael Scott"),
    ("Why are you the way that you are?", "Michael Scott"),
    ("I’m not a hero. I just put my bra on one boob at a time like everyone else.", "Phyllis Lapin-Vance"),
    ("You miss 100% of the shots you don’t take. – Wayne Gretzky", "Michael Scott"),
    ("Fact: Bears eat beets. Bears. Beets. Battlestar Galactica.", "Jim Halpert"),
]

# Button to generate a quote
if st.button("Generate Quote"):
    quote, character = random.choice(quotes)
    st.markdown(f"### 💬 \"{quote}\"")
    st.markdown(f"**— {character}**")

# Optional: Allow user to add their own quotes
st.markdown("---")
st.subheader("Add Your Own Quote")

new_quote = st.text_input("Quote")
new_character = st.text_input("Character")

if st.button("Add Quote"):
    if new_quote and new_character:
        quotes.append((new_quote, new_character))
        st.success("Quote added! (Note: This resets when the app reloads.)")
    else:
        st.error("Please enter both a quote and a character name.")
