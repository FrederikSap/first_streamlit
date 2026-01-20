import streamlit as st
import random

# Page config
st.set_page_config(page_title="Creed Bratton Quote Generator", page_icon="🧔")

# Title
st.title("🧔 Creed Bratton Quote Generator")
st.write("Click the button to get a random quote from Creed Bratton.")

# Display Creed image
# You can replace this URL with any Creed image you prefer
creed_image_url = "https://upload.wikimedia.org/wikipedia/en/8/80/CreedBratton.jpg"
st.image(creed_image_url, caption="Creed Bratton – The Office", use_container_width=True)

# Creed-only quotes
creed_quotes = [
    "I run a small fake ID company from my car with a laminating machine that I swiped from the sheriff’s station.",
    "Nobody steals from Creed Bratton and gets away with it. The last person to do this disappeared. His name? Creed Bratton.",
    "If I can't scuba, then what's this all been about? What am I working toward?",
    "I’ve been involved in a number of cults, both as a leader and a follower. You have more fun as a follower, but you make more money as a leader.",
    "I’d like to see a machine that puts out candy for everyone.",
    "Just pretend like we’re talking until the cops leave.",
    "There is no difference between a murderer and a rapist. They both take what they want.",
    "I already won the lottery. I was born in the U.S.A., baby.",
    "I sprout mung beans on a damp paper towel in my desk drawer. Very nutritious, but they smell like death.",
    "When Pam gets Michael’s old chair, I get Pam’s old chair. Then I’ll have two chairs. Only one to go.",
]

# Button to generate a quote
if st.button("Generate Creed Quote"):
    quote = random.choice(creed_quotes)
    st.markdown("---")
    st.markdown(f"### 💬 \"{quote}\"")
    st.markdown("**— Creed Bratton**")
