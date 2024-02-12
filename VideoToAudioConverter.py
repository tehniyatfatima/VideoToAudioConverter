import streamlit as st
import os
from moviepy.editor import VideoFileClip

def video_to_audio(video_path):
    # Load the video file
    video_clip = VideoFileClip(video_path)
    
    # Extract the audio from the video
    audio_clip = video_clip.audio
    
    # Create the audio file path
    audio_file = os.path.splitext(video_path)[0] + ".wav"
    
    # Write the audio to a new file
    audio_clip.write_audiofile(audio_file)
    
    # Close the video and audio clips
    video_clip.close()
    audio_clip.close()
    
    return audio_file

st.title("Video to Audio Converter")

uploaded_file = st.file_uploader("Upload a video file", type=["mp4"])

if uploaded_file is not None:
    st.write("File uploaded successfully!")
    
    # Save the uploaded file to disk
    with open("temp_video.mp4", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # Process the uploaded video file
    audio_file = video_to_audio("temp_video.mp4")
    
    # Display download link for the audio file
    st.write("### Converted Audio")
    st.audio(audio_file, format='audio/wav', start_time=0)
    st.success("Audio file created successfully! You can download it by  clicking on three dots.")
