import streamlit as st
from transformers import pipeline
from youtube_transcript_api import YouTubeTranscriptApi

# Title of the app
st.title('YouTube Video Summarizer')

# Prompt the user to enter the YouTube video URL
youtube_video = st.text_input("Enter YouTube video URL:")

# Submit button
if st.button('Submit'):
    if youtube_video:
        try:
            # Extract the video ID from the URL
            video_id = youtube_video.split("=")[1]
            
            # Fetch the transcript
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
            
            # Combine the transcript into a single string
            result = " ".join([i['text'] for i in transcript])
            st.write(f"Transcript length: {len(result)} characters")

            # Initialize the summarization pipeline
            summarizer = pipeline('summarization')

            # Summarize the transcript in chunks
            num_iters = len(result) // 1000
            summarized_text = []

            for i in range(num_iters + 1):
                start = i * 1000
                end = (i + 1) * 1000
                chunk = result[start:end]
                
                summary = summarizer(chunk)
                summary_text = summary[0]['summary_text']
                
                summarized_text.append(summary_text)

            # Display the summarized text
            st.subheader('Summary')
            for text in summarized_text:
                st.write(text)

        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.error("Please enter a valid YouTube video URL.")
