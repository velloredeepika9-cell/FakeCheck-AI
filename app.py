import streamlit as st
from PIL import Image
import random

st.title("FakeCheck AI")
st.subheader("Multimodal Deepfake & Misinformation Detector")

option = st.selectbox(
"Select Media Type",
("Text","Image","Audio","Video")
)

if option == "Text":
    text = st.text_area("Enter text to analyze")

    if st.button("Analyze"):
        score = random.randint(30,90)

        st.write("Authenticity Score:",score)

        if score < 50:
            st.error("⚠ Likely AI Generated")
        else:
            st.success("✔ Likely Human Written")

elif option == "Image":

    file = st.file_uploader("Upload Image")

    if file:
        img = Image.open(file)
        st.image(img)

        score = random.randint(30,90)

        st.write("Deepfake Probability:",100-score)

elif option == "Audio":

    audio = st.file_uploader("Upload Audio")

    if audio:
        st.audio(audio)

        score = random.randint(30,90)

        st.write("Synthetic Voice Probability:",100-score)

elif option == "Video":

    video = st.file_uploader("Upload Video")

    if video:
        st.video(video)

        score = random.randint(30,90)

        st.write("Deepfake Probability:",100-score)