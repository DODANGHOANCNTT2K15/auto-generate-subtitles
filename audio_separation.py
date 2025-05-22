from moviepy import VideoFileClip
import os

def extract_audio_from_video(video_path, audio_path):
    try:
        print(f"Extracting audio from {video_path} to {audio_path}...")
        video = VideoFileClip(video_path)
        audio = video.audio
        audio.write_audiofile(audio_path, codec='mp3')
        print(f"Audio extracted successfully to {audio_path}")

        video.close()
        audio.close()
        
    except Exception as e:
        print(f"Error extracting audio: {e}")


if __name__ == "__main__":
    video_path = r"C:/Users/dodan/Downloads/01 Cướp Biển Vùng Caribê- Lời Nguyền Của Tàu Ngọc Trai Đen - Pirates of the Caribbean- The Curse of the Black Pearl Full HD Vietsub online - BluPhim.mp4"
    audio_path = r"C:/Users/dodan/Downloads/audio.mp3"

    if not os.path.exists(video_path):
        print(f"Video file does not exist: {video_path}")

    extract_audio_from_video(
        video_path,
        audio_path
    )
