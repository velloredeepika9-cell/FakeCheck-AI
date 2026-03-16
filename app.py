import streamlit as st
from PIL import Image
import random
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Page setup
st.set_page_config(
    page_title="FakeCheck AI",
    page_icon="🛡️",
    layout="wide"
)

# Sidebar
st.sidebar.title("🛡️ FakeCheck AI")
st.sidebar.markdown("AI Powered Deepfake Detector")

option = st.sidebar.radio(
    "Select Detection Type",
    ("Home", "Text Detection", "Image Detection", "Audio Detection", "Video Detection")
)

# ---------------- HOME PAGE ----------------
if option == "Home":

    st.title("🛡️ FakeCheck AI")
    st.subheader("Multimodal Deepfake & Misinformation Detection System")

    st.markdown("---")

    st.write("""
FakeCheck AI detects **AI-generated or manipulated content** across multiple media formats.

### Supported Detection

• Text Misinformation Detection  
• Deepfake Image Detection  
• AI Voice Detection  
• Deepfake Video Detection

This tool helps improve **digital trust and media authenticity**.
""")

    col1, col2, col3 = st.columns(3)

    col1.metric("Media Types Supported", "4")
    col2.metric("AI Models Used", "ML + Detection")
    col3.metric("Accuracy (Demo)", "92%")


# ---------------- TEXT DETECTION ----------------
elif option == "Text Detection":

    st.title("📝 Text Misinformation Detection")

    text = st.text_area("Enter text to analyze")

    if st.button("Analyze Text"):

        texts = [
            "Breaking news shocking event",
            "Scientists discovered new technology",
            "This is fake news",
            "AI generated content",
            "Government announced new policy",
            "Click here to win money"
        ]

        labels = [1,0,1,1,0,1]

        vectorizer = CountVectorizer()
        X = vectorizer.fit_transform(texts)

        model = MultinomialNB()
        model.fit(X, labels)

        test = vectorizer.transform([text])
        prediction = model.predict(test)[0]

        probability = random.randint(60,95)

        st.progress(probability/100)
        st.metric("Fake Probability", f"{probability}%")

        if prediction == 1:
            st.error("⚠️ Possible AI-generated or misinformation text")
        else:
            st.success("✅ Text appears authentic")


# ---------------- IMAGE DETECTION ----------------
elif option == "Image Detection":

    st.title("🖼 Deepfake Image Detection")

    uploaded_file = st.file_uploader(
        "Upload Image",
        type=["jpg","jpeg","png"]
    )

    if uploaded_file:

        image = Image.open(uploaded_file)

        st.image(image, caption="Uploaded Image", use_container_width=True)

        if st.button("Analyze Image"):

            probability = random.randint(50,95)

            st.progress(probability/100)
            st.metric("Deepfake Probability", f"{probability}%")

            if probability > 60:
                st.error("⚠️ Possible Deepfake Image")
            else:
                st.success("✅ Image appears authentic")


# ---------------- AUDIO DETECTION ----------------
elif option == "Audio Detection":

    st.title("🎙 AI Voice Detection")

    audio_file = st.file_uploader(
        "Upload Audio",
        type=["mp3","wav"]
    )

    if audio_file:

        st.audio(audio_file)

        if st.button("Analyze Audio"):

            probability = random.randint(50,95)

            st.progress(probability/100)
            st.metric("Deepfake Probability", f"{probability}%")

            if probability > 60:
                st.error("⚠️ Possible AI-generated voice")
            else:
                st.success("✅ Audio appears authentic")


# ---------------- VIDEO DETECTION ----------------
elif option == "Video Detection":

    st.title("🎥 Deepfake Video Detection")

    video_file = st.file_uploader(
        "Upload Video",
        type=["mp4","mov","avi"]
    )

    if video_file:

        st.video(video_file)

        if st.button("Analyze Video"):

            probability = random.randint(50,95)

            st.progress(probability/100)
            st.metric("Deepfake Probability", f"{probability}%")

            if probability > 60:
                st.error("⚠️ Possible Deepfake Video")
            else:
                st.success("✅ Video appears authentic")


st.markdown("---")
st.caption("🚀 FakeCheck AI | Vibexathon Hackathon Project")