from moviepy import VideoFileClip
from pydub import AudioSegment
import noisereduce as nr
import scipy.io.wavfile as wav
import numpy as np
import os

def extract_audio_from_video(video_path, audio_path):
    try:
        print(f"Extracting audio from {video_path} to {audio_path}...")
        video = VideoFileClip(video_path)
        video.audio.write_audiofile(audio_path, codec='pcm_s16le')
        print(f"Audio extracted successfully to {audio_path}")

        video.close()
        
    except Exception as e:
        print(f"Error extracting audio: {e}")